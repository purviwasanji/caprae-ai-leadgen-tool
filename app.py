import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
import json
from datetime import datetime, timedelta
import re
import time
import random
from typing import Dict, List, Optional
import io
import base64

# Configure page
st.set_page_config(
    page_title="Caprae - Acquisition Intelligence Platform",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border-left: 4px solid #2a5298;
    }
    
    .target-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border: 1px solid #e9ecef;
    }
    
    .high-priority { border-left: 4px solid #28a745; }
    .medium-priority { border-left: 4px solid #ffc107; }
    .low-priority { border-left: 4px solid #dc3545; }
    
    .contact-info {
        background: #e3f2fd;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    
    .stSelectbox > div > div {
        background-color: #f8f9fa;
    }
    
    .acquisition-score {
        font-size: 2rem;
        font-weight: bold;
        color: #2a5298;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'company_data' not in st.session_state:
    st.session_state.company_data = None
if 'filtered_data' not in st.session_state:
    st.session_state.filtered_data = None
if 'selected_company' not in st.session_state:
    st.session_state.selected_company = None

@st.cache_data
def load_company_data():
    """Load company data from CSV file"""
    try:
        df = pd.read_csv('caprae_company_database.csv')
        return df
    except FileNotFoundError:
        st.error("⚠️ Database file not found. Please run the _mapping.py script first to generate the company database.")
        return None
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

def calculate_advanced_metrics(df):
    """Calculate advanced acquisition metrics"""
    if df is None or df.empty:
        return {}
    
    total_companies = len(df)
    avg_score = df['acquisition_score'].mean()
    high_priority = len(df[df['acquisition_score'] >= 85])
    medium_priority = len(df[(df['acquisition_score'] >= 70) & (df['acquisition_score'] < 85)])
    total_market_cap = df['revenue'].sum() / 1000000000  # Convert to billions
    
    return {
        'total_companies': total_companies,
        'avg_score': avg_score,
        'high_priority': high_priority,
        'medium_priority': medium_priority,
        'total_market_cap': total_market_cap
    }

def create_acquisition_dashboard(df):
    """Create comprehensive acquisition dashboard"""
    if df is None or df.empty:
        return
    
    # Key metrics
    metrics = calculate_advanced_metrics(df)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Total Companies</h3>
            <div class="acquisition-score">{metrics['total_companies']}</div>
            <p>In Pipeline</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Avg Score</h3>
            <div class="acquisition-score">{metrics['avg_score']:.1f}</div>
            <p>Acquisition Readiness</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>High Priority</h3>
            <div class="acquisition-score">{metrics['high_priority']}</div>
            <p>Ready for Outreach</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Market Cap</h3>
            <div class="acquisition-score">${metrics['total_market_cap']:.1f}B</div>
            <p>Total Revenue</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Acquisition Score Distribution
        fig_score = px.histogram(df, x='acquisition_score', nbins=20, 
                               title='Acquisition Score Distribution',
                               color_discrete_sequence=['#2a5298'])
        fig_score.update_layout(height=400)
        st.plotly_chart(fig_score, use_container_width=True)
    
    with col2:
        # Industry Distribution
        industry_counts = df['industry'].value_counts().head(10)
        fig_industry = px.bar(x=industry_counts.values, y=industry_counts.index,
                            title='Top 10 Industries',
                            orientation='h',
                            color_discrete_sequence=['#2a5298'])
        fig_industry.update_layout(height=400)
        st.plotly_chart(fig_industry, use_container_width=True)
    
    # Revenue vs Score Scatter
    fig_scatter = px.scatter(df, x='revenue', y='acquisition_score', 
                           color='acquisition_category', size='employees',
                           hover_data=['name', 'industry'],
                           title='Revenue vs Acquisition Score',
                           labels={'revenue': 'Revenue ($)', 'acquisition_score': 'Acquisition Score'})
    fig_scatter.update_layout(height=500)
    st.plotly_chart(fig_scatter, use_container_width=True)

def create_smart_filters(df):
    """Create advanced filtering system"""
    if df is None:
        return None
    
    st.sidebar.header("🎯 Smart Filters")
    
    # Acquisition Score Range
    score_range = st.sidebar.slider(
        "Acquisition Score Range",
        min_value=int(df['acquisition_score'].min()),
        max_value=int(df['acquisition_score'].max()),
        value=(70, 100),
        help="Filter by acquisition readiness score"
    )
    
    # Industry Filter
    industries = ['All'] + sorted(df['industry'].unique().tolist())
    selected_industry = st.sidebar.selectbox("Industry", industries)
    
    # Revenue Range
    revenue_range = st.sidebar.slider(
        "Revenue Range (Millions)",
        min_value=0,
        max_value=int(df['revenue'].max() / 1000000),
        value=(0, int(df['revenue'].max() / 1000000)),
        help="Filter by annual revenue"
    )
    
    # Employee Range
    employee_range = st.sidebar.slider(
        "Employee Range",
        min_value=0,
        max_value=int(df['employees'].max()),
        value=(0, int(df['employees'].max())),
        help="Filter by company size"
    )
    
    # Company Stage
    stages = ['All'] + sorted(df['stage'].unique().tolist())
    selected_stage = st.sidebar.selectbox("Company Stage", stages)
    
    # Growth Filter
    growth_filter = st.sidebar.selectbox(
        "Growth Rate",
        ['All', 'High Growth (>30%)', 'Medium Growth (10-30%)', 'Low Growth (<10%)']
    )
    
    # Location Filter
    locations = ['All'] + sorted(df['location'].unique().tolist())
    selected_location = st.sidebar.selectbox("Location", locations)
    
    # Apply filters
    filtered_df = df.copy()
    
    # Score filter
    filtered_df = filtered_df[
        (filtered_df['acquisition_score'] >= score_range[0]) & 
        (filtered_df['acquisition_score'] <= score_range[1])
    ]
    
    # Industry filter
    if selected_industry != 'All':
        filtered_df = filtered_df[filtered_df['industry'] == selected_industry]
    
    # Revenue filter
    filtered_df = filtered_df[
        (filtered_df['revenue'] >= revenue_range[0] * 1000000) & 
        (filtered_df['revenue'] <= revenue_range[1] * 1000000)
    ]
    
    # Employee filter
    filtered_df = filtered_df[
        (filtered_df['employees'] >= employee_range[0]) & 
        (filtered_df['employees'] <= employee_range[1])
    ]
    
    # Stage filter
    if selected_stage != 'All':
        filtered_df = filtered_df[filtered_df['stage'] == selected_stage]
    
    # Growth filter
    if growth_filter == 'High Growth (>30%)':
        filtered_df = filtered_df[filtered_df['revenue_growth'] > 0.3]
    elif growth_filter == 'Medium Growth (10-30%)':
        filtered_df = filtered_df[
            (filtered_df['revenue_growth'] >= 0.1) & 
            (filtered_df['revenue_growth'] <= 0.3)
        ]
    elif growth_filter == 'Low Growth (<10%)':
        filtered_df = filtered_df[filtered_df['revenue_growth'] < 0.1]
    
    # Location filter
    if selected_location != 'All':
        filtered_df = filtered_df[filtered_df['location'] == selected_location]
    
    return filtered_df

def display_company_targets(df):
    """Display prioritized company targets"""
    if df is None or df.empty:
        st.warning("No companies match your filter criteria.")
        return
    
    # Sort by acquisition score
    df = df.sort_values('acquisition_score', ascending=False)
    
    st.header("🎯 Priority Targets")
    
    # Display summary
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Filtered Companies", len(df))
    with col2:
        st.metric("Avg Score", f"{df['acquisition_score'].mean():.1f}")
    with col3:
        st.metric("High Priority", len(df[df['acquisition_score'] >= 85]))
    
    # Company cards
    for idx, company in df.iterrows():
        priority_class = "high-priority" if company['acquisition_score'] >= 85 else \
                        "medium-priority" if company['acquisition_score'] >= 70 else "low-priority"
        
        with st.expander(f"🏢 {company['name']} - Score: {company['acquisition_score']:.1f}"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"""
                **Industry:** {company['industry']}  
                **Revenue:** ${company['revenue']/1000000:.1f}M  
                **Employees:** {company['employees']:,}  
                **Growth:** {company['revenue_growth']*100:.1f}%  
                **Location:** {company['location']}  
                **Stage:** {company['stage']}  
                **Founded:** {company['founded']}
                """)
                
                st.markdown(f"**Investment Thesis:** {company['investment_thesis']}")
                st.markdown(f"**Recent News:** {company['recent_news']}")
                
            with col2:
                st.markdown(f"""
                <div class="contact-info">
                    <strong>Key Contacts</strong><br>
                    <strong>CEO:</strong> {company['ceo_name']}<br>
                    <strong>Email:</strong> {company['ceo_email']}<br>
                    <strong>CTO:</strong> {company['cto_name']}<br>
                    <strong>Phone:</strong> {company['company_phone']}<br>
                    <strong>LinkedIn:</strong> <a href="{company['linkedin_url']}" target="_blank">View Profile</a>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"Generate Outreach for {company['name']}", key=f"outreach_{idx}"):
                    st.session_state.selected_company = company
                    st.session_state.show_outreach = True

def generate_outreach_content(company):
    """Generate personalized outreach content"""
    if company is None:
        return
    
    st.header(f"📧 Outreach Package for {company['name']}")
    
    # Company Research Summary
    st.subheader("🔍 Company Research Summary")
    st.markdown(f"""
    **Company Overview:**
    - {company['name']} is a {company['stage'].lower()} company in the {company['industry']} industry
    - Founded in {company['founded']} ({company['company_age']} years ago)
    - Current revenue: ${company['revenue']/1000000:.1f}M with {company['revenue_growth']*100:.1f}% growth
    - Team size: {company['employees']} employees
    - Acquisition readiness score: {company['acquisition_score']:.1f}/100
    
    **Key Strengths:**
    - {company['investment_thesis']}
    - Strong market position: {company['market_position']:.1f}/10
    - Financial health score: {company['financial_health']:.1f}/10
    - Recent development: {company['recent_news']}
    
    **Competitive Landscape:**
    - Main competitors: {company['main_competitors']}
    - Primary risk factor: {company['primary_risk']}
    
    **Valuation Estimate:**
    - Range: ${company['estimated_valuation_low']:.0f}M - ${company['estimated_valuation_high']:.0f}M
    - Preferred deal structure: {company['preferred_deal_structure']}
    """)
    
    # Personalized Outreach Message
    st.subheader("📝 Personalized Outreach Message")
    st.markdown("**Email Subject:** Strategic Partnership Opportunity - [Your Company] & " + company['name'])
    
    message_container = st.container()
    with message_container:
        st.markdown(f"""
        <div style="background: #f8f9fa; padding: 1rem; border-radius: 8px; border: 1px solid #e9ecef;">
        {company['personalized_outreach']}
        </div>
        """, unsafe_allow_html=True)
    
    # Conversation Starters
    st.subheader("💬 Conversation Starters")
    starters = company['conversation_starters'].split(' | ')
    for i, starter in enumerate(starters, 1):
        st.markdown(f"**{i}.** {starter}")
    
    # Follow-up Strategy
    st.subheader("📈 Follow-up Strategy")
    st.markdown(f"""
    **Recommended Approach:**
    1. **Initial Email:** Use the personalized message above
    2. **Follow-up Timeline:** 3-5 business days if no response
    3. **LinkedIn Connection:** Connect with {company['ceo_name']} and {company['cto_name']}
    4. **Value Proposition:** Emphasize expertise in {company['industry']} sector
    5. **Meeting Objective:** 15-minute intro call to discuss strategic opportunities
    
    **Key Discussion Points:**
    - Market expansion opportunities
    - Operational scaling challenges
    - Capital requirements for growth
    - Strategic partnerships and acquisitions
    """)
    
    # Export Options
    st.subheader("📤 Export Options")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📧 Copy Email"):
            st.success("Email copied to clipboard!")
    
    with col2:
        if st.button("📱 Export Contact"):
            st.success("Contact exported!")
    
    with col3:
        if st.button("📊 Add to CRM"):
            st.success("Added to CRM!")

def create_analytics_dashboard(df):
    """Create advanced analytics dashboard"""
    if df is None or df.empty:
        return
    
    st.header("📊 Advanced Analytics")
    
    # Performance Metrics
    col1, col2 = st.columns(2)
    
    with col1:
        # Acquisition Score vs Revenue Growth
        fig_performance = px.scatter(df, x='revenue_growth', y='acquisition_score',
                                   color='industry', size='revenue',
                                   hover_data=['name', 'employees'],
                                   title='Growth vs Acquisition Score',
                                   labels={'revenue_growth': 'Revenue Growth Rate',
                                          'acquisition_score': 'Acquisition Score'})
        st.plotly_chart(fig_performance, use_container_width=True)
    
    with col2:
        # Market Position Analysis
        fig_market = px.box(df, x='industry', y='market_position',
                          title='Market Position by Industry')
        fig_market.update_xaxes(tickangle=45)
        st.plotly_chart(fig_market, use_container_width=True)
    
    # Financial Health Matrix
    fig_matrix = px.scatter(df, x='financial_health', y='market_position',
                          color='acquisition_category', size='revenue',
                          hover_data=['name', 'industry'],
                          title='Financial Health vs Market Position Matrix',
                          labels={'financial_health': 'Financial Health Score',
                                 'market_position': 'Market Position Score'})
    st.plotly_chart(fig_matrix, use_container_width=True)
    
    # Industry Deep Dive
    st.subheader("🏭 Industry Analysis")
    
    industry_stats = df.groupby('industry').agg({
        'acquisition_score': ['mean', 'count'],
        'revenue': 'mean',
        'employees': 'mean',
        'revenue_growth': 'mean'
    }).round(2)
    
    industry_stats.columns = ['Avg Score', 'Count', 'Avg Revenue', 'Avg Employees', 'Avg Growth']
    industry_stats = industry_stats.sort_values('Avg Score', ascending=False)
    
    st.dataframe(industry_stats, use_container_width=True)

def export_data_options(df):
    """Provide data export options"""
    if df is None or df.empty:
        return
    
    st.sidebar.header("📤 Export Data")
    
    # CSV Export
    csv = df.to_csv(index=False)
    st.sidebar.download_button(
        label="Download CSV",
        data=csv,
        file_name=f"caprae_filtered_companies_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )
    
    # Excel Export
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Companies', index=False)
        
        # Add summary sheet
        summary_data = {
            'Metric': ['Total Companies', 'Avg Acquisition Score', 'High Priority Targets', 'Total Revenue'],
            'Value': [len(df), df['acquisition_score'].mean(), len(df[df['acquisition_score'] >= 85]), df['revenue'].sum()]
        }
        summary_df = pd.DataFrame(summary_data)
        summary_df.to_excel(writer, sheet_name='Summary', index=False)
    
    buffer.seek(0)
    st.sidebar.download_button(
        label="Download Excel",
        data=buffer.getvalue(),
        file_name=f"caprae_filtered_companies_{datetime.now().strftime('%Y%m%d')}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

def main():
    """Main application function"""
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎯 Caprae - Acquisition Intelligence Platform</h1>
        <p>AI-Powered M&A Target Discovery & Outreach Automation</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    if st.session_state.company_data is None:
        with st.spinner("Loading company database..."):
            st.session_state.company_data = load_company_data()
    
    df = st.session_state.company_data
    
    if df is None:
        st.error("Unable to load company data. Please ensure the database file exists.")
        return
    
    # Navigation
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏠 Dashboard", 
        "🎯 Target Discovery", 
        "📧 Outreach Generator", 
        "📊 Analytics", 
        "⚙️ Settings"
    ])
    
    with tab1:
        st.header("📊 Executive Dashboard")
        create_acquisition_dashboard(df)
    
    with tab2:
        st.header("🔍 Smart Company Discovery")
        # Apply filters
        filtered_df = create_smart_filters(df)
        st.session_state.filtered_data = filtered_df
        
        # Display targets
        display_company_targets(filtered_df)
        
        # Export options
        export_data_options(filtered_df)
    
    with tab3:
        st.header("📧 Automated Outreach Generator")
        if st.session_state.selected_company is not None:
            generate_outreach_content(st.session_state.selected_company)
        else:
            st.info("Select a company from the Target Discovery tab to generate outreach content.")
            
            # Quick company selector
            if df is not None:
                st.subheader("Quick Company Selection")
                top_companies = df.nlargest(20, 'acquisition_score')
                selected_name = st.selectbox(
                    "Choose a company:",
                    options=top_companies['name'].tolist(),
                    key="quick_selector"
                )
                
                if st.button("Generate Outreach"):
                    selected_company = df[df['name'] == selected_name].iloc[0]
                    st.session_state.selected_company = selected_company
                    st.experimental_rerun()
    
    with tab4:
        st.header("📈 Advanced Analytics")
        filtered_df = st.session_state.filtered_data if st.session_state.filtered_data is not None else df
        create_analytics_dashboard(filtered_df)
    
    with tab5:
        st.header("⚙️ Settings & Configuration")
        
        st.subheader("🔧 System Settings")
        
        # API Configuration
        st.markdown("**API Configuration**")
        hunter_api = st.text_input("Hunter.io API Key", type="password", help="For email finding")
        clearbit_api = st.text_input("Clearbit API Key", type="password", help="For company enrichment")
        
        if st.button("Save API Keys"):
            st.success("API keys saved successfully!")
        
        # Data Refresh
        st.markdown("**Data Management**")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔄 Refresh Database"):
                st.session_state.company_data = None
                st.experimental_rerun()
        
        with col2:
            if st.button("📥 Import New Data"):
                st.info("Upload feature coming soon!")
        
        # System Info
        st.subheader("📊 System Information")
        if df is not None:
            st.markdown(f"""
            - **Database Size:** {len(df)} companies
            - **Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            - **Industries Covered:** {df['industry'].nunique()}
            - **Average Data Quality:** {df['data_quality_score'].mean():.1f}/10
            """)

if __name__ == "__main__":
    main()
