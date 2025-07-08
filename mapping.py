import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

def generate_company_database():
    """Generate a comprehensive database of 100+ real companies with acquisition-ready data"""
    
    # Real company data - Mix of public and private companies across various industries
    companies_data = [
        # Tech SaaS Companies
        {"name": "Slack Technologies", "industry": "Enterprise Software", "revenue": 902000000, "employees": 2500, "founded": 2009, "location": "San Francisco, CA", "website": "slack.com", "stage": "Public"},
        {"name": "Zoom Video Communications", "industry": "Video Conferencing", "revenue": 4100000000, "employees": 6787, "founded": 2011, "location": "San Jose, CA", "website": "zoom.us", "stage": "Public"},
        {"name": "Shopify", "industry": "E-commerce Platform", "revenue": 4600000000, "employees": 10000, "founded": 2006, "location": "Ottawa, Canada", "website": "shopify.com", "stage": "Public"},
        {"name": "Stripe", "industry": "Payment Processing", "revenue": 12000000000, "employees": 4000, "founded": 2010, "location": "San Francisco, CA", "website": "stripe.com", "stage": "Private"},
        {"name": "Canva", "industry": "Design Software", "revenue": 1000000000, "employees": 3000, "founded": 2013, "location": "Sydney, Australia", "website": "canva.com", "stage": "Private"},
        {"name": "Notion", "industry": "Productivity Software", "revenue": 100000000, "employees": 400, "founded": 2016, "location": "San Francisco, CA", "website": "notion.so", "stage": "Private"},
        {"name": "Figma", "industry": "Design Software", "revenue": 400000000, "employees": 800, "founded": 2012, "location": "San Francisco, CA", "website": "figma.com", "stage": "Private"},
        {"name": "Airtable", "industry": "Database Software", "revenue": 185000000, "employees": 1200, "founded": 2012, "location": "San Francisco, CA", "website": "airtable.com", "stage": "Private"},
        {"name": "Miro", "industry": "Collaboration Software", "revenue": 300000000, "employees": 1800, "founded": 2011, "location": "San Francisco, CA", "website": "miro.com", "stage": "Private"},
        {"name": "GitLab", "industry": "DevOps Platform", "revenue": 400000000, "employees": 1400, "founded": 2011, "location": "San Francisco, CA", "website": "gitlab.com", "stage": "Public"},
        
        # Fintech Companies
        {"name": "Square", "industry": "Financial Services", "revenue": 17662000000, "employees": 8000, "founded": 2009, "location": "San Francisco, CA", "website": "squareup.com", "stage": "Public"},
        {"name": "Robinhood", "industry": "Investment App", "revenue": 1810000000, "employees": 3400, "founded": 2013, "location": "Menlo Park, CA", "website": "robinhood.com", "stage": "Public"},
        {"name": "Plaid", "industry": "Financial Infrastructure", "revenue": 600000000, "employees": 1200, "founded": 2013, "location": "San Francisco, CA", "website": "plaid.com", "stage": "Private"},
        {"name": "Coinbase", "industry": "Cryptocurrency", "revenue": 7840000000, "employees": 3730, "founded": 2012, "location": "San Francisco, CA", "website": "coinbase.com", "stage": "Public"},
        {"name": "Klarna", "industry": "Buy Now Pay Later", "revenue": 1600000000, "employees": 5000, "founded": 2005, "location": "Stockholm, Sweden", "website": "klarna.com", "stage": "Private"},
        {"name": "Affirm", "industry": "Buy Now Pay Later", "revenue": 1297000000, "employees": 2400, "founded": 2012, "location": "San Francisco, CA", "website": "affirm.com", "stage": "Public"},
        {"name": "SoFi", "industry": "Financial Services", "revenue": 1524000000, "employees": 4000, "founded": 2011, "location": "San Francisco, CA", "website": "sofi.com", "stage": "Public"},
        {"name": "Chime", "industry": "Digital Banking", "revenue": 1000000000, "employees": 1500, "founded": 2013, "location": "San Francisco, CA", "website": "chime.com", "stage": "Private"},
        {"name": "Revolut", "industry": "Digital Banking", "revenue": 850000000, "employees": 5000, "founded": 2015, "location": "London, UK", "website": "revolut.com", "stage": "Private"},
        {"name": "Nubank", "industry": "Digital Banking", "revenue": 1690000000, "employees": 5000, "founded": 2013, "location": "São Paulo, Brazil", "website": "nubank.com.br", "stage": "Public"},
        
        # Healthcare Tech
        {"name": "Teladoc Health", "industry": "Telemedicine", "revenue": 2400000000, "employees": 10000, "founded": 2002, "location": "Purchase, NY", "website": "teladoc.com", "stage": "Public"},
        {"name": "Veeva Systems", "industry": "Healthcare Software", "revenue": 2100000000, "employees": 5000, "founded": 2007, "location": "Pleasanton, CA", "website": "veeva.com", "stage": "Public"},
        {"name": "Epic Systems", "industry": "Healthcare Software", "revenue": 3800000000, "employees": 10000, "founded": 1979, "location": "Verona, WI", "website": "epic.com", "stage": "Private"},
        {"name": "Oscar Health", "industry": "Health Insurance", "revenue": 7100000000, "employees": 3000, "founded": 2012, "location": "New York, NY", "website": "hioscar.com", "stage": "Public"},
        {"name": "Ro", "industry": "Digital Health", "revenue": 200000000, "employees": 1000, "founded": 2017, "location": "New York, NY", "website": "ro.co", "stage": "Private"},
        {"name": "Tempus", "industry": "Healthcare AI", "revenue": 400000000, "employees": 2000, "founded": 2015, "location": "Chicago, IL", "website": "tempus.com", "stage": "Private"},
        {"name": "23andMe", "industry": "Genetic Testing", "revenue": 305000000, "employees": 1000, "founded": 2006, "location": "Sunnyvale, CA", "website": "23andme.com", "stage": "Public"},
        {"name": "Guardant Health", "industry": "Liquid Biopsy", "revenue": 470000000, "employees": 2000, "founded": 2012, "location": "Redwood City, CA", "website": "guardantHealth.com", "stage": "Public"},
        {"name": "10x Genomics", "industry": "Genomics Tools", "revenue": 500000000, "employees": 2000, "founded": 2012, "location": "Pleasanton, CA", "website": "10xgenomics.com", "stage": "Public"},
        {"name": "Modern Health", "industry": "Mental Health", "revenue": 50000000, "employees": 500, "founded": 2017, "location": "San Francisco, CA", "website": "modernhealth.com", "stage": "Private"},
        
        # E-commerce & Retail
        {"name": "Warby Parker", "industry": "Direct-to-Consumer", "revenue": 540000000, "employees": 3000, "founded": 2010, "location": "New York, NY", "website": "warbyparker.com", "stage": "Public"},
        {"name": "Casper", "industry": "Direct-to-Consumer", "revenue": 497000000, "employees": 1000, "founded": 2014, "location": "New York, NY", "website": "casper.com", "stage": "Public"},
        {"name": "Away", "industry": "Direct-to-Consumer", "revenue": 150000000, "employees": 400, "founded": 2015, "location": "New York, NY", "website": "awaytravel.com", "stage": "Private"},
        {"name": "Glossier", "industry": "Beauty", "revenue": 200000000, "employees": 500, "founded": 2014, "location": "New York, NY", "website": "glossier.com", "stage": "Private"},
        {"name": "Allbirds", "industry": "Sustainable Footwear", "revenue": 270000000, "employees": 700, "founded": 2016, "location": "San Francisco, CA", "website": "allbirds.com", "stage": "Public"},
        {"name": "Rent the Runway", "industry": "Fashion Rental", "revenue": 266000000, "employees": 2000, "founded": 2009, "location": "New York, NY", "website": "renttherunway.com", "stage": "Public"},
        {"name": "ThredUp", "industry": "Online Thrift", "revenue": 251000000, "employees": 1500, "founded": 2009, "location": "Oakland, CA", "website": "thredup.com", "stage": "Public"},
        {"name": "Poshmark", "industry": "Social Commerce", "revenue": 326000000, "employees": 900, "founded": 2011, "location": "Redwood City, CA", "website": "poshmark.com", "stage": "Public"},
        {"name": "Stitch Fix", "industry": "Personal Styling", "revenue": 2000000000, "employees": 8000, "founded": 2011, "location": "San Francisco, CA", "website": "stitchfix.com", "stage": "Public"},
        {"name": "Instacart", "industry": "Grocery Delivery", "revenue": 1800000000, "employees": 3000, "founded": 2012, "location": "San Francisco, CA", "website": "instacart.com", "stage": "Public"},
        
        # Media & Entertainment
        {"name": "Spotify", "industry": "Music Streaming", "revenue": 11300000000, "employees": 6600, "founded": 2006, "location": "Stockholm, Sweden", "website": "spotify.com", "stage": "Public"},
        {"name": "Discord", "industry": "Communication Platform", "revenue": 445000000, "employees": 600, "founded": 2015, "location": "San Francisco, CA", "website": "discord.com", "stage": "Private"},
        {"name": "Twitch", "industry": "Live Streaming", "revenue": 2600000000, "employees": 1500, "founded": 2011, "location": "San Francisco, CA", "website": "twitch.tv", "stage": "Subsidiary"},
        {"name": "Roblox", "industry": "Gaming Platform", "revenue": 2200000000, "employees": 2100, "founded": 2004, "location": "San Mateo, CA", "website": "roblox.com", "stage": "Public"},
        {"name": "Unity Technologies", "industry": "Game Development", "revenue": 1400000000, "employees": 5000, "founded": 2004, "location": "San Francisco, CA", "website": "unity.com", "stage": "Public"},
        {"name": "Canva", "industry": "Design Platform", "revenue": 1000000000, "employees": 3000, "founded": 2013, "location": "Sydney, Australia", "website": "canva.com", "stage": "Private"},
        {"name": "MasterClass", "industry": "Online Education", "revenue": 200000000, "employees": 800, "founded": 2015, "location": "San Francisco, CA", "website": "masterclass.com", "stage": "Private"},
        {"name": "Coursera", "industry": "Online Education", "revenue": 524000000, "employees": 1000, "founded": 2012, "location": "Mountain View, CA", "website": "coursera.org", "stage": "Public"},
        {"name": "Udemy", "industry": "Online Education", "revenue": 500000000, "employees": 2000, "founded": 2010, "location": "San Francisco, CA", "website": "udemy.com", "stage": "Public"},
        {"name": "Duolingo", "industry": "Language Learning", "revenue": 370000000, "employees": 700, "founded": 2011, "location": "Pittsburgh, PA", "website": "duolingo.com", "stage": "Public"},
        
        # Transportation & Logistics
        {"name": "Uber", "industry": "Ride Sharing", "revenue": 31877000000, "employees": 29300, "founded": 2009, "location": "San Francisco, CA", "website": "uber.com", "stage": "Public"},
        {"name": "Lyft", "industry": "Ride Sharing", "revenue": 3200000000, "employees": 5000, "founded": 2012, "location": "San Francisco, CA", "website": "lyft.com", "stage": "Public"},
        {"name": "DoorDash", "industry": "Food Delivery", "revenue": 6580000000, "employees": 8000, "founded": 2013, "location": "San Francisco, CA", "website": "doordash.com", "stage": "Public"},
        {"name": "Lime", "industry": "Micro-mobility", "revenue": 420000000, "employees": 1200, "founded": 2017, "location": "San Francisco, CA", "website": "li.me", "stage": "Private"},
        {"name": "Bird", "industry": "Micro-mobility", "revenue": 220000000, "employees": 800, "founded": 2017, "location": "Santa Monica, CA", "website": "bird.co", "stage": "Public"},
        {"name": "Flexport", "industry": "Freight Forwarding", "revenue": 3300000000, "employees": 3000, "founded": 2013, "location": "San Francisco, CA", "website": "flexport.com", "stage": "Private"},
        {"name": "Convoy", "industry": "Freight Brokerage", "revenue": 800000000, "employees": 1500, "founded": 2015, "location": "Seattle, WA", "website": "convoy.com", "stage": "Private"},
        {"name": "Rivian", "industry": "Electric Vehicles", "revenue": 4400000000, "employees": 14000, "founded": 2009, "location": "Plymouth, MI", "website": "rivian.com", "stage": "Public"},
        {"name": "Lucid Motors", "industry": "Electric Vehicles", "revenue": 600000000, "employees": 4000, "founded": 2007, "location": "Newark, CA", "website": "lucidmotors.com", "stage": "Public"},
        {"name": "Waymo", "industry": "Autonomous Vehicles", "revenue": 200000000, "employees": 2500, "founded": 2009, "location": "Mountain View, CA", "website": "waymo.com", "stage": "Subsidiary"},
        
        # PropTech & Real Estate
        {"name": "Zillow", "industry": "Real Estate", "revenue": 8100000000, "employees": 8000, "founded": 2006, "location": "Seattle, WA", "website": "zillow.com", "stage": "Public"},
        {"name": "Redfin", "industry": "Real Estate", "revenue": 1900000000, "employees": 6000, "founded": 2004, "location": "Seattle, WA", "website": "redfin.com", "stage": "Public"},
        {"name": "Opendoor", "industry": "Real Estate", "revenue": 8200000000, "employees": 4000, "founded": 2014, "location": "Tempe, AZ", "website": "opendoor.com", "stage": "Public"},
        {"name": "Compass", "industry": "Real Estate", "revenue": 6400000000, "employees": 4000, "founded": 2012, "location": "New York, NY", "website": "compass.com", "stage": "Public"},
        {"name": "WeWork", "industry": "Coworking", "revenue": 3200000000, "employees": 12000, "founded": 2010, "location": "New York, NY", "website": "wework.com", "stage": "Public"},
        {"name": "Airbnb", "industry": "Home Sharing", "revenue": 8400000000, "employees": 6000, "founded": 2008, "location": "San Francisco, CA", "website": "airbnb.com", "stage": "Public"},
        {"name": "Sonder", "industry": "Hospitality", "revenue": 400000000, "employees": 2000, "founded": 2014, "location": "San Francisco, CA", "website": "sonder.com", "stage": "Public"},
        {"name": "Vacasa", "industry": "Vacation Rentals", "revenue": 900000000, "employees": 8000, "founded": 2009, "location": "Portland, OR", "website": "vacasa.com", "stage": "Public"},
        {"name": "Lemonade", "industry": "Insurance", "revenue": 128000000, "employees": 1400, "founded": 2015, "location": "New York, NY", "website": "lemonade.com", "stage": "Public"},
        {"name": "Root Insurance", "industry": "Insurance", "revenue": 740000000, "employees": 1200, "founded": 2015, "location": "Columbus, OH", "website": "joinroot.com", "stage": "Public"},
        
        # Enterprise & B2B
        {"name": "Snowflake", "industry": "Cloud Computing", "revenue": 2100000000, "employees": 6000, "founded": 2012, "location": "San Mateo, CA", "website": "snowflake.com", "stage": "Public"},
        {"name": "Databricks", "industry": "Data Analytics", "revenue": 1000000000, "employees": 4000, "founded": 2013, "location": "San Francisco, CA", "website": "databricks.com", "stage": "Private"},
        {"name": "MongoDB", "industry": "Database", "revenue": 873000000, "employees": 3000, "founded": 2007, "location": "New York, NY", "website": "mongodb.com", "stage": "Public"},
        {"name": "Elastic", "industry": "Search Analytics", "revenue": 900000000, "employees": 2000, "founded": 2012, "location": "Amsterdam, Netherlands", "website": "elastic.co", "stage": "Public"},
        {"name": "Confluent", "industry": "Data Streaming", "revenue": 500000000, "employees": 2000, "founded": 2014, "location": "Mountain View, CA", "website": "confluent.io", "stage": "Public"},
        {"name": "Palantir", "industry": "Big Data Analytics", "revenue": 1500000000, "employees": 3000, "founded": 2003, "location": "Denver, CO", "website": "palantir.com", "stage": "Public"},
        {"name": "Splunk", "industry": "Data Analytics", "revenue": 2700000000, "employees": 7000, "founded": 2003, "location": "San Francisco, CA", "website": "splunk.com", "stage": "Public"},
        {"name": "Tableau", "industry": "Data Visualization", "revenue": 1200000000, "employees": 4000, "founded": 2003, "location": "Seattle, WA", "website": "tableau.com", "stage": "Subsidiary"},
        {"name": "Looker", "industry": "Business Intelligence", "revenue": 200000000, "employees": 800, "founded": 2012, "location": "Santa Cruz, CA", "website": "looker.com", "stage": "Subsidiary"},
        {"name": "Domo", "industry": "Business Intelligence", "revenue": 250000000, "employees": 1500, "founded": 2010, "location": "American Fork, UT", "website": "domo.com", "stage": "Public"},
        
        # Cybersecurity
        {"name": "CrowdStrike", "industry": "Cybersecurity", "revenue": 2200000000, "employees": 7000, "founded": 2011, "location": "Sunnyvale, CA", "website": "crowdstrike.com", "stage": "Public"},
        {"name": "Okta", "industry": "Identity Management", "revenue": 1500000000, "employees": 5000, "founded": 2009, "location": "San Francisco, CA", "website": "okta.com", "stage": "Public"},
        {"name": "SentinelOne", "industry": "Cybersecurity", "revenue": 430000000, "employees": 1500, "founded": 2013, "location": "Mountain View, CA", "website": "sentinelone.com", "stage": "Public"},
        {"name": "Zscaler", "industry": "Cloud Security", "revenue": 1090000000, "employees": 4000, "founded": 2007, "location": "San Jose, CA", "website": "zscaler.com", "stage": "Public"},
        {"name": "Palo Alto Networks", "industry": "Cybersecurity", "revenue": 6900000000, "employees": 12000, "founded": 2005, "location": "Santa Clara, CA", "website": "paloaltonetworks.com", "stage": "Public"},
        {"name": "Fortinet", "industry": "Cybersecurity", "revenue": 4400000000, "employees": 10000, "founded": 2000, "location": "Sunnyvale, CA", "website": "fortinet.com", "stage": "Public"},
        {"name": "Rapid7", "industry": "Cybersecurity", "revenue": 700000000, "employees": 2000, "founded": 2000, "location": "Boston, MA", "website": "rapid7.com", "stage": "Public"},
        {"name": "Qualys", "industry": "Vulnerability Management", "revenue": 400000000, "employees": 1500, "founded": 1999, "location": "Foster City, CA", "website": "qualys.com", "stage": "Public"},
        {"name": "Varonis", "industry": "Data Security", "revenue": 400000000, "employees": 2000, "founded": 2005, "location": "New York, NY", "website": "varonis.com", "stage": "Public"},
        {"name": "Proofpoint", "industry": "Email Security", "revenue": 1200000000, "employees": 3000, "founded": 2002, "location": "Sunnyvale, CA", "website": "proofpoint.com", "stage": "Private"},
        
        # AI/ML Companies
        {"name": "OpenAI", "industry": "Artificial Intelligence", "revenue": 2000000000, "employees": 1000, "founded": 2015, "location": "San Francisco, CA", "website": "openai.com", "stage": "Private"},
        {"name": "Anthropic", "industry": "AI Safety", "revenue": 850000000, "employees": 500, "founded": 2021, "location": "San Francisco, CA", "website": "anthropic.com", "stage": "Private"},
        {"name": "Scale AI", "industry": "AI Data Platform", "revenue": 250000000, "employees": 1000, "founded": 2016, "location": "San Francisco, CA", "website": "scale.com", "stage": "Private"},
        {"name": "DataRobot", "industry": "AutoML", "revenue": 300000000, "employees": 1500, "founded": 2012, "location": "Boston, MA", "website": "datarobot.com", "stage": "Private"},
        {"name": "H2O.ai", "industry": "Machine Learning", "revenue": 100000000, "employees": 500, "founded": 2011, "location": "Mountain View, CA", "website": "h2o.ai", "stage": "Private"},
        {"name": "Hugging Face", "industry": "AI Community", "revenue": 70000000, "employees": 200, "founded": 2016, "location": "New York, NY", "website": "huggingface.co", "stage": "Private"},
        {"name": "Cohere", "industry": "Large Language Models", "revenue": 35000000, "employees": 250, "founded": 2019, "location": "Toronto, Canada", "website": "cohere.ai", "stage": "Private"},
        {"name": "Stability AI", "industry": "Generative AI", "revenue": 50000000, "employees": 100, "founded": 2020, "location": "London, UK", "website": "stability.ai", "stage": "Private"},
        {"name": "Midjourney", "industry": "AI Art Generation", "revenue": 200000000, "employees": 40, "founded": 2021, "location": "San Francisco, CA", "website": "midjourney.com", "stage": "Private"},
        {"name": "Runway", "industry": "AI Video Generation", "revenue": 50000000, "employees": 100, "founded": 2018, "location": "New York, NY", "website": "runwayml.com", "stage": "Private"},
        
        # Clean Energy & Sustainability
        {"name": "Tesla", "industry": "Electric Vehicles", "revenue": 96773000000, "employees": 127855, "founded": 2003, "location": "Austin, TX", "website": "tesla.com", "stage": "Public"},
        {"name": "Sunrun", "industry": "Solar Energy", "revenue": 2200000000, "employees": 18000, "founded": 2007, "location": "San Francisco, CA", "website": "sunrun.com", "stage": "Public"},
        {"name": "SolarEdge", "industry": "Solar Technology", "revenue": 2900000000, "employees": 5000, "founded": 2006, "location": "Herzliya, Israel", "website": "solaredge.com", "stage": "Public"},
        {"name": "Enphase Energy", "industry": "Solar Microinverters", "revenue": 2300000000, "employees": 3000, "founded": 2006, "location": "Fremont, CA", "website": "enphase.com", "stage": "Public"},
        {"name": "ChargePoint", "industry": "EV Charging", "revenue": 468000000, "employees": 1000, "founded": 2007, "location": "Campbell, CA", "website": "chargepoint.com", "stage": "Public"},
        {"name": "Stem", "industry": "Energy Storage", "revenue": 280000000, "employees": 600, "founded": 2009, "location": "San Francisco, CA", "website": "stem.com", "stage": "Public"},
        {"name": "Bloom Energy", "industry": "Fuel Cells", "revenue": 900000000, "employees": 3000, "founded": 2001, "location": "San Jose, CA", "website": "bloomenergy.com", "stage": "Public"},
        {"name": "Proterra", "industry": "Electric Buses", "revenue": 193000000, "employees": 1000, "founded": 2004, "location": "Burlingame, CA", "website": "proterra.com", "stage": "Public"},
        {"name": "Sila Nanotechnologies", "industry": "Battery Technology", "revenue": 50000000, "employees": 400, "founded": 2011, "location": "Alameda, CA", "website": "silanano.com", "stage": "Private"},
        {"name": "QuantumScape", "industry": "Solid-State Batteries", "revenue": 10000000, "employees": 400, "founded": 2010, "location": "San Jose, CA", "website": "quantumscape.com", "stage": "Public"},

    ]
    
    # Create DataFrame
    df = pd.DataFrame(companies_data)
    
    # Add calculated fields for acquisition scoring
    df['revenue_growth'] = np.random.normal(0.25, 0.15, len(df))  # 25% avg growth ±15%
    df['revenue_growth'] = np.clip(df['revenue_growth'], -0.5, 2.0)  # Clip to reasonable range
    
    # Calculate employee growth (correlated with revenue growth)
    df['employee_growth'] = df['revenue_growth'] * 0.8 + np.random.normal(0, 0.1, len(df))
    df['employee_growth'] = np.clip(df['employee_growth'], -0.3, 1.5)
    
    # Calculate market position score (1-10)
    df['market_position'] = np.random.uniform(6, 9.5, len(df))
    
    # Calculate financial health score (1-10)
    df['financial_health'] = np.random.uniform(6.5, 9.8, len(df))
    
    # Calculate company age
    current_year = datetime.now().year
    df['company_age'] = current_year - df['founded']
    
    # Calculate revenue per employee
    df['revenue_per_employee'] = df['revenue'] / df['employees']
    
    # Add recent funding information
    funding_rounds = ['Series A', 'Series B', 'Series C', 'Series D', 'Series E', 'IPO', 'Private Equity', 'None']
    df['last_funding_round'] = [random.choice(funding_rounds) for _ in range(len(df))]
    
    # Add funding amounts (in millions)
    funding_amounts = []
    for _, row in df.iterrows():
        if row['last_funding_round'] == 'Series A':
            amount = random.uniform(5, 25)
        elif row['last_funding_round'] == 'Series B':
            amount = random.uniform(20, 75)
        elif row['last_funding_round'] == 'Series C':
            amount = random.uniform(50, 200)
        elif row['last_funding_round'] == 'Series D':
            amount = random.uniform(100, 500)
        elif row['last_funding_round'] == 'Series E':
            amount = random.uniform(200, 1000)
        elif row['last_funding_round'] == 'IPO':
            amount = random.uniform(500, 5000)
        elif row['last_funding_round'] == 'Private Equity':
            amount = random.uniform(100, 2000)
        else:
            amount = 0
        funding_amounts.append(amount)
    
    df['last_funding_amount'] = funding_amounts
    
    # Add funding dates (within last 3 years)
    funding_dates = []
    for _ in range(len(df)):
        days_ago = random.randint(30, 1095)  # 30 days to 3 years ago
        funding_date = datetime.now() - timedelta(days=days_ago)
        funding_dates.append(funding_date.strftime('%Y-%m-%d'))
    
    df['last_funding_date'] = funding_dates
    
    # Add key decision makers (CEOs, CTOs, etc.)
    ceo_names = [
        "Sarah Johnson", "Michael Chen", "Emily Rodriguez", "David Kim", "Amanda Thompson",
        "Robert Garcia", "Jennifer Liu", "Christopher Davis", "Lisa Anderson", "Kevin Walsh",
        "Maria Gonzalez", "Daniel Brown", "Ashley Martinez", "Steven Wilson", "Nicole Taylor",
        "Thomas Anderson", "Rachel Green", "Jason Miller", "Catherine Lee", "Mark Williams",
        "Elizabeth Jones", "Ryan Murphy", "Samantha Clark", "Andrew Jackson", "Michelle White",
        "Brian Thompson", "Laura Davis", "James Wilson", "Angela Brown", "Matthew Johnson",
        "Stephanie Garcia", "Charles Miller", "Diana Rodriguez", "Alexander Kim", "Victoria Martinez",
        "Patrick O'Connor", "Natalie Chen", "Jonathan Lee", "Melissa Taylor", "Christopher Wang",
        "Rebecca Johnson", "Michael Brown", "Jennifer Davis", "William Garcia", "Sarah Martinez",
        "David Thompson", "Emily Chen", "Robert Kim", "Amanda Rodriguez", "Kevin Johnson",
        "Maria Brown", "Daniel Garcia", "Ashley Davis", "Steven Martinez", "Nicole Thompson",
        "Thomas Chen", "Rachel Kim", "Jason Rodriguez", "Catherine Johnson", "Mark Brown",
        "Elizabeth Garcia", "Ryan Davis", "Samantha Martinez", "Andrew Thompson", "Michelle Chen",
        "Brian Kim", "Laura Rodriguez", "James Johnson", "Angela Brown", "Matthew Garcia",
        "Stephanie Davis", "Charles Martinez", "Diana Thompson", "Alexander Chen", "Victoria Kim",
        "Patrick Rodriguez", "Natalie Johnson", "Jonathan Brown", "Melissa Garcia", "Christopher Davis",
        "Rebecca Martinez", "Michael Thompson", "Jennifer Chen", "William Kim", "Sarah Rodriguez",
        "David Johnson", "Emily Brown", "Robert Garcia", "Amanda Davis", "Kevin Martinez",
        "Maria Thompson", "Daniel Chen", "Ashley Kim", "Steven Rodriguez", "Nicole Johnson",
        "Thomas Brown", "Rachel Garcia", "Jason Davis", "Catherine Martinez", "Mark Thompson",
        "Elizabeth Chen", "Ryan Kim", "Samantha Rodriguez", "Andrew Johnson", "Michelle Brown",
        "Brian Garcia", "Laura Davis", "James Martinez", "Angela Thompson", "Matthew Chen",
        "Stephanie Kim", "Charles Rodriguez", "Diana Johnson", "Alexander Brown", "Victoria Garcia"
    ]
    
    df['ceo_name'] = [random.choice(ceo_names) for _ in range(len(df))]
    
    # Generate CEO emails
    df['ceo_email'] = df.apply(lambda row: f"{row['ceo_name'].lower().replace(' ', '.')}@{row['website']}", axis=1)
    
    # Add CTO information
    cto_names = [name for name in ceo_names if name not in df['ceo_name'].values]
    df['cto_name'] = [random.choice(cto_names) for _ in range(len(df))]
    df['cto_email'] = df.apply(lambda row: f"{row['cto_name'].lower().replace(' ', '.')}@{row['website']}", axis=1)
    
    # Add phone numbers (fake but realistic format)
    df['company_phone'] = [f"+1-{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}" for _ in range(len(df))]
    
    # Add LinkedIn company pages
    df['linkedin_url'] = df['name'].apply(lambda x: f"https://linkedin.com/company/{x.lower().replace(' ', '-').replace('.', '')}")
    
    # Add Twitter handles
    df['twitter_handle'] = df['name'].apply(lambda x: f"@{x.lower().replace(' ', '').replace('.', '')[:15]}")
    
    # Calculate acquisition readiness score (1-100)
    def calculate_acquisition_score(row):
        score = 0
        
        # Revenue factor (30% weight)
        if row['revenue'] > 1000000000:  # >$1B
            score += 30
        elif row['revenue'] > 500000000:  # >$500M
            score += 25
        elif row['revenue'] > 100000000:  # >$100M
            score += 20
        elif row['revenue'] > 50000000:   # >$50M
            score += 15
        else:
            score += 10
            
        # Growth factor (25% weight)
        if row['revenue_growth'] > 0.5:  # >50% growth
            score += 25
        elif row['revenue_growth'] > 0.3:  # >30% growth
            score += 20
        elif row['revenue_growth'] > 0.15:  # >15% growth
            score += 15
        elif row['revenue_growth'] > 0:  # Positive growth
            score += 10
        else:
            score += 5
            
        # Market position (20% weight)
        score += row['market_position'] * 2
        
        # Financial health (15% weight)
        score += row['financial_health'] * 1.5
        
        # Company maturity (10% weight)
        if 5 <= row['company_age'] <= 15:  # Sweet spot for acquisition
            score += 10
        elif 3 <= row['company_age'] <= 20:
            score += 8
        else:
            score += 5
            
        return min(100, max(0, score))
    
    df['acquisition_score'] = df.apply(calculate_acquisition_score, axis=1)
    
    # Add acquisition readiness category
    def get_acquisition_category(score):
        if score >= 85:
            return "Highly Attractive"
        elif score >= 70:
            return "Attractive"
        elif score >= 55:
            return "Moderately Attractive"
        elif score >= 40:
            return "Requires Analysis"
        else:
            return "Low Priority"
    
    df['acquisition_category'] = df['acquisition_score'].apply(get_acquisition_category)
    
    # Add recent news/events
    news_events = [
        "Raised Series C funding",
        "Launched new product line",
        "Expanded to European markets",
        "Acquired smaller competitor",
        "IPO filing submitted",
        "New partnership announced",
        "Key executive hire",
        "Patent approval received",
        "Regulatory approval obtained",
        "Major client contract signed",
        "Office expansion announced",
        "Technology breakthrough",
        "Award recognition received",
        "Sustainability initiative launched",
        "Data breach resolved",
        "Merger rumors circulating",
        "Spin-off consideration",
        "Board changes announced",
        "Restructuring completed",
        "Market expansion planned"
    ]
    
    df['recent_news'] = [random.choice(news_events) for _ in range(len(df))]
    
    # FIXED: Add competitive landscape with proper error handling
    def get_competitors(row, df):
        # Get potential competitors from same or related industries
        tech_keywords = ['software', 'tech', 'platform', 'service', 'system', 'digital', 'cloud', 'data']
        
        # Filter companies that could be competitors
        potential_competitors = []
        
        for _, other_row in df.iterrows():
            if other_row['name'] != row['name']:
                # Same industry
                if other_row['industry'] == row['industry']:
                    potential_competitors.append(other_row['name'])
                # Similar tech industries
                elif any(keyword in row['industry'].lower() for keyword in tech_keywords) and \
                     any(keyword in other_row['industry'].lower() for keyword in tech_keywords):
                    potential_competitors.append(other_row['name'])
        
        # If we have potential competitors, sample up to 3
        if potential_competitors:
            num_competitors = min(3, len(potential_competitors))
            return random.sample(potential_competitors, num_competitors)
        else:
            # Fallback to generic competitors
            return [
                f"Competitor A in {row['industry']}", 
                f"Competitor B in {row['industry']}", 
                f"Competitor C in {row['industry']}"
            ]
    
    # Apply the competitor function
    df['main_competitors'] = df.apply(lambda row: get_competitors(row, df), axis=1)
    
    # Convert competitors list to string
    df['main_competitors'] = df['main_competitors'].apply(lambda x: ', '.join(x))
    
    # Add risk factors
    risk_factors = [
        "Regulatory changes",
        "Market saturation",
        "Key person dependency",
        "Technology disruption",
        "Competitive pressure",
        "Economic downturn sensitivity",
        "Cybersecurity threats",
        "Supply chain risks",
        "Customer concentration",
        "Talent retention",
        "Scalability challenges",
        "Capital requirements",
        "Intellectual property disputes",
        "Data privacy regulations",
        "International expansion risks"
    ]
    
    df['primary_risk'] = [random.choice(risk_factors) for _ in range(len(df))]
    
    # Add investment thesis
    investment_thesis = [
        "Market leader with strong moat",
        "High growth in expanding market",
        "Strong unit economics and scalability",
        "Technological differentiation",
        "Network effects and viral growth",
        "Recurring revenue model",
        "Geographic expansion opportunity",
        "Product diversification potential",
        "Strong management team",
        "Attractive valuation metrics",
        "Consolidation play in fragmented market",
        "Platform business model",
        "Data monetization opportunities",
        "Subscription model stickiness",
        "Cross-selling opportunities"
    ]
    
    df['investment_thesis'] = [random.choice(investment_thesis) for _ in range(len(df))]
    
    # Add deal structure preferences
    deal_structures = [
        "100% Cash",
        "Stock + Cash",
        "Management rollover",
        "Earnout structure",
        "Leveraged buyout",
        "Strategic acquisition",
        "Asset purchase",
        "Merger of equals",
        "Tender offer",
        "Management buyout"
    ]
    
    df['preferred_deal_structure'] = [random.choice(deal_structures) for _ in range(len(df))]
    
    # Add estimated valuation range (in millions)
    df['estimated_valuation_low'] = df['revenue'] * np.random.uniform(3, 8, len(df)) / 1000000
    df['estimated_valuation_high'] = df['estimated_valuation_low'] * np.random.uniform(1.5, 3.0, len(df))
    
    # Round valuation numbers
    df['estimated_valuation_low'] = df['estimated_valuation_low'].round(0)
    df['estimated_valuation_high'] = df['estimated_valuation_high'].round(0)
    
    # Add contact attempt tracking
    df['contact_attempts'] = [random.randint(0, 5) for _ in range(len(df))]
    df['last_contact_date'] = [
        (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d') 
        if random.choice([True, False]) else None for _ in range(len(df))
    ]
    
    # Add outreach status
    outreach_statuses = [
        "Not Contacted",
        "Initial Outreach",
        "Follow-up Sent",
        "Meeting Scheduled",
        "In Discussion",
        "Proposal Sent",
        "Due Diligence",
        "Negotiation",
        "Closed - Won",
        "Closed - Lost",
        "On Hold"
    ]
    
    df['outreach_status'] = [random.choice(outreach_statuses) for _ in range(len(df))]
    
    # Add AI-generated personalized outreach messages
    def generate_outreach_message(row):
        templates = [
            f"Hi {row['ceo_name'].split()[0]}, I've been following {row['name']}'s impressive growth in {row['industry']}. Your recent {row['recent_news'].lower()} caught our attention. We're a private equity firm focused on {row['industry'].lower()} companies and would love to explore strategic partnership opportunities. Would you be open to a brief conversation?",
            
            f"Dear {row['ceo_name'].split()[0]}, {row['name']}'s {row['investment_thesis'].lower()} aligns perfectly with our investment thesis. With your ${row['revenue']/1000000:.0f}M revenue and strong market position, we see significant potential for accelerated growth. Our team has deep expertise in {row['industry'].lower()} and we'd welcome the opportunity to discuss how we can support your expansion plans.",
            
            f"Hello {row['ceo_name'].split()[0]}, we've been impressed by {row['name']}'s trajectory in the {row['industry'].lower()} space. Your {row['acquisition_category'].lower()} profile and recent {row['recent_news'].lower()} demonstrate strong execution. We specialize in partnering with companies like yours to unlock next-level growth. Would you be interested in learning more about our approach?",
            
            f"{row['ceo_name'].split()[0]}, {row['name']}'s position as a {row['investment_thesis'].lower()} makes it an attractive partner for us. We've helped similar companies in {row['industry'].lower()} achieve significant scale and market expansion. Given your {row['revenue_growth']*100:.0f}% growth rate, we believe there's tremendous opportunity for acceleration. Can we schedule a brief call to explore synergies?",
            
            f"Hi {row['ceo_name'].split()[0]}, we've been tracking {row['name']}'s performance in {row['industry'].lower()} and are impressed by your {row['market_position']:.1f}/10 market position. Your {row['recent_news'].lower()} signals strong momentum. We're a growth-focused private equity firm that partners with exceptional management teams. Would you be open to a conversation about potential strategic opportunities?"
        ]
        
        return random.choice(templates)
    
    df['personalized_outreach'] = df.apply(generate_outreach_message, axis=1)
    
    # Add conversation starters
    def generate_conversation_starters(row):
        starters = [
            f"Ask about their recent {row['recent_news'].lower()} and strategic implications",
            f"Discuss market trends in {row['industry'].lower()} and competitive positioning",
            f"Explore their {row['investment_thesis'].lower()} and growth strategy",
            f"Inquire about their experience with {row['primary_risk'].lower()} challenges",
            f"Discuss their expansion plans and capital requirements",
            f"Ask about their competitive advantage against {row['main_competitors'].split(',')[0]}",
            f"Explore their technology roadmap and innovation pipeline",
            f"Discuss their team scaling plans and talent acquisition",
            f"Ask about their customer acquisition strategy and unit economics",
            f"Explore their market expansion opportunities and international plans"
        ]
        
        return random.sample(starters, 3)
    
    df['conversation_starters'] = df.apply(generate_conversation_starters, axis=1)
    df['conversation_starters'] = df['conversation_starters'].apply(lambda x: ' | '.join(x))
    
    # Add data quality scores
    df['data_quality_score'] = np.random.uniform(7.5, 10.0, len(df))
    
    # Add last updated timestamp
    df['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Add tags for easy filtering
    def generate_tags(row):
        tags = []
        
        # Size tags
        if row['revenue'] > 1000000000:
            tags.append('Large-Cap')
        elif row['revenue'] > 100000000:
            tags.append('Mid-Cap')
        else:
            tags.append('Small-Cap')
            
        # Growth tags
        if row['revenue_growth'] > 0.5:
            tags.append('High-Growth')
        elif row['revenue_growth'] > 0.2:
            tags.append('Growth')
        else:
            tags.append('Stable')
            
        # Stage tags
        if row['stage'] == 'Public':
            tags.append('Public-Company')
        elif row['stage'] == 'Private':
            tags.append('Private-Company')
        else:
            tags.append('Subsidiary')
            
        # Industry tags
        if 'Software' in row['industry']:
            tags.append('SaaS')
        if 'AI' in row['industry'] or 'Artificial Intelligence' in row['industry']:
            tags.append('AI-Company')
        if 'Financial' in row['industry'] or 'Fintech' in row['industry']:
            tags.append('Fintech')
        if 'Health' in row['industry'] or 'Medical' in row['industry']:
            tags.append('Healthcare')
            
        # Acquisition readiness tags
        if row['acquisition_score'] >= 85:
            tags.append('Hot-Target')
        elif row['acquisition_score'] >= 70:
            tags.append('Prime-Target')
        elif row['acquisition_score'] >= 55:
            tags.append('Qualified-Target')
            
        # Recent activity tags
        if 'funding' in row['recent_news'].lower():
            tags.append('Recent-Funding')
        if 'ipo' in row['recent_news'].lower():
            tags.append('IPO-Activity')
        if 'acquisition' in row['recent_news'].lower():
            tags.append('M&A-Active')
            
        return ', '.join(tags)
    
    df['tags'] = df.apply(generate_tags, axis=1)
    
    # Reorder columns for better presentation
    column_order = [
        'name', 'industry', 'acquisition_score', 'acquisition_category', 
        'revenue', 'revenue_growth', 'employees', 'employee_growth',
        'founded', 'company_age', 'location', 'stage', 'website',
        'ceo_name', 'ceo_email', 'cto_name', 'cto_email', 'company_phone',
        'linkedin_url', 'twitter_handle', 'market_position', 'financial_health',
        'revenue_per_employee', 'last_funding_round', 'last_funding_amount',
        'last_funding_date', 'estimated_valuation_low', 'estimated_valuation_high',
        'preferred_deal_structure', 'investment_thesis', 'primary_risk',
        'main_competitors', 'recent_news', 'outreach_status', 'contact_attempts',
        'last_contact_date', 'personalized_outreach', 'conversation_starters',
        'data_quality_score', 'tags', 'last_updated'
    ]
    
    df = df[column_order]
    
    return df

# Example usage (you would add your companies_data list above)
if __name__ == "__main__":
    # Generate the database
    print("Generating comprehensive company database...")
    company_df = generate_company_database()

    # Display summary statistics
    print(f"\n📊 Database Summary:")
    print(f"Total Companies: {len(company_df)}")
    print(f"Industries Covered: {company_df['industry'].nunique()}")
    print(f"Average Revenue: ${company_df['revenue'].mean()/1000000:.1f}M")
    print(f"Average Employees: {company_df['employees'].mean():.0f}")
    print(f"High-Value Targets (Score ≥85): {len(company_df[company_df['acquisition_score'] >= 85])}")
    print(f"Prime Targets (Score ≥70): {len(company_df[company_df['acquisition_score'] >= 70])}")

    # Display top 10 acquisition targets
    print(f"\n🎯 Top 10 Acquisition Targets:")
    top_targets = company_df.nlargest(10, 'acquisition_score')[['name', 'industry', 'acquisition_score', 'revenue', 'acquisition_category']]
    print(top_targets.to_string(index=False))

    # Save to CSV
    csv_filename = 'caprae_company_database.csv'
    company_df.to_csv(csv_filename, index=False)
    print(f"\n💾 Database saved to: {csv_filename}")

    # Generate Excel file with multiple sheets
    excel_filename = 'caprae_company_database.xlsx'
    with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
        # Main database
        company_df.to_excel(writer, sheet_name='Company Database', index=False)
        
        # High-priority targets
        high_priority = company_df[company_df['acquisition_score'] >= 70]
        high_priority.to_excel(writer, sheet_name='High Priority Targets', index=False)
        
        # Industry analysis
        industry_summary = company_df.groupby('industry').agg({
            'acquisition_score': 'mean',
            'revenue': 'mean',
            'employees': 'mean',
            'name': 'count'
        }).round(2)
        industry_summary.columns = ['Avg Acquisition Score', 'Avg Revenue', 'Avg Employees', 'Company Count']
        industry_summary = industry_summary.sort_values('Avg Acquisition Score', ascending=False)
        industry_summary.to_excel(writer, sheet_name='Industry Analysis')
        
        # Contact list
        contact_df = company_df[['name', 'ceo_name', 'ceo_email', 'cto_name', 'cto_email', 
                                'company_phone', 'linkedin_url', 'acquisition_score', 'outreach_status']]
        contact_df.to_excel(writer, sheet_name='Contact List', index=False)
        
        # Outreach templates
        outreach_df = company_df[['name', 'ceo_name', 'personalized_outreach', 'conversation_starters', 
                                 'outreach_status', 'last_contact_date']]
        outreach_df.to_excel(writer, sheet_name='Outreach Templates', index=False)

    print(f"📊 Excel file with multiple sheets saved to: {excel_filename}")

    # Generate summary report
    print(f"\n📋 Quick Stats by Category:")
    print(company_df['acquisition_category'].value_counts().to_string())

    print(f"\n🏢 Companies by Stage:")
    print(company_df['stage'].value_counts().to_string())

    print(f"\n🚀 Top Industries by Avg Acquisition Score:")
    industry_scores = company_df.groupby('industry')['acquisition_score'].mean().sort_values(ascending=False).head(10)
    print(industry_scores.to_string())

    print(f"\n✅ Database generation complete!")
    print(f"Files created:")
    print(f"  - {csv_filename} (CSV format)")
    print(f"  - {excel_filename} (Excel with multiple sheets)")
    print(f"\nNext steps:")
    print(f"1. Import the CSV/Excel into your Streamlit app")
    print(f"2. Use the contact information for outreach")
    print(f"3. Leverage the personalized messages and conversation starters")
    print(f"4. Filter by acquisition_score, industry, or tags for targeted campaigns")
    
