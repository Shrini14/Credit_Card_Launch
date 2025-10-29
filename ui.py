import streamlit as st
import os
from datetime import datetime

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Youth Credit Card Launch",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# ADVANCED CUSTOM CSS STYLING
# ==========================================
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%);
        background-attachment: fixed;
        color: #1a1a2e;
        font-family: 'Segoe UI', 'Inter', sans-serif;
    }
    
    .main-container {
        max-width: 1400px;
        margin: 0 auto;
    }
    
    /* Headers */
    h1 {
        color: #ffffff;
        font-size: 2.8rem;
        font-weight: 900;
        text-align: center;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3);
        margin-bottom: 0.5rem;
        letter-spacing: 2px;
    }
    
    h2 {
        color: #ffffff;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 2rem 0 1rem 0;
        border-left: 6px solid #ff006e;
        padding-left: 20px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    h3 {
        color: #ff006e;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 1.5rem 0 0.8rem 0;
    }
    
    h4 {
        color: #3a86ff;
        font-weight: 700;
        font-size: 1.2rem;
    }
    
    /* Links */
    a {
        color: #ff006e !important;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    a:hover {
        color: #3a86ff !important;
        text-decoration: underline;
    }
    
    /* Divider */
    hr {
        background: linear-gradient(90deg, transparent, #ff006e, transparent);
        border: none;
        height: 3px;
        margin: 2rem 0;
    }
    
    /* Markdown Container */
    div[data-testid="stMarkdownContainer"] {
        font-size: 16px;
        line-height: 1.8;
        color: #1a1a2e;
    }
    
    /* Cards/Columns */
    div[data-testid="column"] {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 2rem;
        border: 2px solid #ff006e;
        transition: all 0.4s ease;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
    }
    
    div[data-testid="column"]:hover {
        background: rgba(255, 255, 255, 1);
        border: 2px solid #3a86ff;
        transform: translateY(-8px);
        box-shadow: 0 20px 50px rgba(58, 134, 255, 0.4);
    }
    
    /* Success Box */
    .stSuccess {
        background: linear-gradient(135deg, rgba(52, 211, 153, 0.2), rgba(16, 185, 129, 0.2)) !important;
        border-left: 6px solid #10b981 !important;
        border-radius: 12px !important;
        padding: 1.5rem !important;
        box-shadow: 0 8px 20px rgba(16, 185, 129, 0.15) !important;
    }
    
    .stSuccess > div {
        color: #1a1a2e !important;
    }
    
    /* Info Box */
    .stInfo {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.2), rgba(99, 102, 241, 0.2)) !important;
        border-left: 6px solid #3a86ff !important;
        border-radius: 12px !important;
        padding: 1.5rem !important;
        box-shadow: 0 8px 20px rgba(58, 134, 255, 0.15) !important;
    }
    
    .stInfo > div {
        color: #1a1a2e !important;
    }
    
    /* Warning Box */
    .stWarning {
        background: linear-gradient(135deg, rgba(249, 115, 22, 0.2), rgba(245, 158, 11, 0.2)) !important;
        border-left: 6px solid #f59e0b !important;
        border-radius: 12px !important;
        padding: 1.5rem !important;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(90deg, #ff006e, #f093fb);
        color: #ffffff;
        font-weight: 700;
        border: none;
        border-radius: 10px;
        padding: 0.8rem 2rem;
        transition: all 0.3s ease;
        cursor: pointer;
        box-shadow: 0 6px 20px rgba(255, 0, 110, 0.4);
        font-size: 1rem;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(255, 0, 110, 0.6);
    }
    
    /* Caption */
    .stCaption {
        color: #1a1a2e;
        font-size: 0.95rem;
        text-align: center;
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 2px solid rgba(255, 0, 110, 0.4);
    }
    
    /* Image Container */
    img {
        border-radius: 15px;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.2);
        transition: all 0.4s ease;
    }
    
    img:hover {
        box-shadow: 0 20px 50px rgba(255, 0, 110, 0.4);
        transform: scale(1.03);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.98), rgba(230, 230, 250, 0.95));
        border-right: 3px solid #ff006e;
    }
    
    [data-testid="stSidebar"] h3 {
        color: #ff006e;
    }
    
    [data-testid="stSidebar"] h2 {
        color: #ff006e;
        border-left: none;
        padding-left: 0;
    }
    
    [data-testid="stSidebar"] > div {
        color: #1a1a2e;
    }
    
    /* Metrics */
    .stMetric {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(240, 250, 255, 0.95));
        padding: 1.5rem;
        border-radius: 12px;
        border: 2px solid #3a86ff;
        box-shadow: 0 8px 20px rgba(58, 134, 255, 0.2);
        transition: all 0.3s ease;
    }
    
    .stMetric:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 30px rgba(58, 134, 255, 0.3);
    }
    
    /* Radio Button */
    .stRadio > label {
        color: #1a1a2e;
        font-weight: 600;
    }
    
    /* Tables */
    table {
        background: rgba(255, 255, 255, 0.95) !important;
        border-radius: 10px !important;
    }
    
    /* Gradient Text */
    .gradient-text {
        background: linear-gradient(135deg, #ff006e 0%, #3a86ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
with st.sidebar:
    st.markdown("### 🧭 Navigation Hub")
    page = st.radio(
        "Explore Project:",
        ["🚀 Mission", "🎯 Phase 1 Discovery", "💡 Youth Card Launch", "🧪 Phase 2 Trial", "📊 Results & Launch"],
        label_visibility="collapsed"
    )
    
    st.divider()
    st.markdown("""
    ### 📚 Project Resources
    - [GitHub Repository](https://github.com/Shrini14/Credit_Card_Launch)
    - [Phase 1 Notebook](https://github.com/Shrini14/Credit_Card_Launch/blob/main/Phase_1/Bank_project_stats_phase1.ipynb)
    - [Phase 2 Notebook](https://github.com/Shrini14/Credit_Card_Launch/blob/main/Phase_2/Bank_project_phase_2%20(1).ipynb)
    """)
    
    st.divider()
    st.markdown("""
    ### 📂 Project Details
    **Author:** R. Shrinivass  
    **Role:** Aspiring Data Scientist  
    **Year:** © 2025
    """)

# ==========================================
# HOME PAGE - MISSION
# ==========================================
if page == "🚀 Mission":
    # Header
    st.markdown('<div style="text-align: center; margin-bottom: 3rem;">', unsafe_allow_html=True)
    st.title("💳 Credit Card Launch Initiative")
    st.markdown("### 🎯 From Concept to Market Success")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.divider()
    
    # Mission Statement
    st.markdown("## 🎯 Project Mission")
    
    st.success("""
    ### Our Objective:
    **Develop, validate, and successfully launch a new Credit Card product through comprehensive market analysis,
    identifying the best target demographic and driving financial inclusion and banking engagement.**
    """)
    
    st.divider()
    
    # Project Journey
    st.markdown("## 🛤️ Project Journey")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        ### Phase 0️⃣
        **Initial Objective**
        
        Launch a new credit card product to grow market presence
        """)
    
    with col2:
        st.markdown("""
        ### Phase 1️⃣
        **Market Analysis**
        
        EDA revealed 18-25 youth segment as highest potential demographic with strong transaction activity
        """)
    
    with col3:
        st.markdown("""
        ### Phase 2️⃣
        **A/B Testing**
        
        Launched Youth Credit Card trial campaign and validated market reception through testing
        """)
    
    with col4:
        st.markdown("""
        ### 🎯 Ready to Launch!
        
        Campaign proved successful ✅ 
        Ready for full-scale market rollout
        """)
    
    st.divider()
    
    # Key Highlights
    st.markdown("## ✨ Key Project Highlights")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 📊 Phase 1: Analysis
        - Comprehensive market analysis
        - Identified 18-25 youth segment
        - Discovered highest transaction potential
        - Low risk profile confirmed
        """)
    
    with col2:
        st.markdown("""
        ### 🧪 Phase 2: Testing
        - A/B campaign validation
        - Youth Credit Card trial
        - Statistical significance proven
        - Market receptivity confirmed
        """)
    
    with col3:
        st.markdown("""
        ### ✅ Result: Success
        - Campaign exceeded targets
        - Ready for launch
        - Market validated
        - Go-ahead approved
        """)

# ==========================================
# PHASE 1 - DISCOVERY
# ==========================================
elif page == "🎯 Phase 1 Discovery":
    st.title("🎯 Phase 1: Market Discovery & Analysis")
    st.markdown("### Initial Objective vs. Discovered Opportunity")
    st.divider()
    
    st.markdown("## 📋 Initial Challenge")
    
    st.info("""
    **Original Goal:** Launch a new credit card product  
    **Target:** General market (all age groups)  
    **Challenge:** Unclear which demographic would be most receptive
    """)
    
    st.divider()
    
    # EDA Findings
    st.markdown("## 🔍 Exploratory Data Analysis Findings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 👥 Demographics
        - **Age Group:** 18-25 years
        - **Activity Level:** Highest transaction volume
        - **Status:** Early-career professionals & students
        - **Tech Savvy:** High digital adoption
        """)
    
    with col2:
        st.markdown("""
        ### 💳 Financial Profile
        - **Average Credit Score:** Healthy range ✅
        - **Risk Level:** Low & manageable
        - **Transaction Frequency:** Very high
        - **Approval Potential:** Excellent
        """)
    
    st.divider()
    
    # Spending Analysis
    st.markdown("## 💰 Spending Behavior - 18-25 Age Group")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🛍️ Top Categories
        1. **Fashion** - 35%
        2. **Electronics** - 28%
        3. **Entertainment** - 18%
        4. **Travel** - 12%
        5. **Food & Dining** - 7%
        """)
    
    with col2:
        st.markdown("""
        ### 🛒 Preferred Platforms
        1. **Amazon** - 40%
        2. **Flipkart** - 30%
        3. **Myntra** - 15%
        4. **Direct Retail** - 10%
        5. **Other** - 5%
        """)
    
    with col3:
        st.markdown("""
        ### 💻 Digital Preferences
        - Mobile first approach
        - Online shopping dominance
        - Digital wallet adoption
        - App-based services
        - Seamless checkout needed
        """)
    
    st.divider()
    
    # Visualizations
    st.markdown("## 📊 Visual Insights from Analysis")
    
    current_dir = os.path.dirname(__file__)
    img1_path = os.path.join(current_dir, "pj_1.png")
    img2_path = os.path.join(current_dir, "pj_2.png")
    
    col1, col2 = st.columns(2)
    
    if os.path.exists(img1_path):
        with col1:
            st.image(img1_path, caption="Age Distribution & Transaction Patterns", use_container_width=True)
    else:
        with col1:
            st.warning("📊 Visualization 1: Age & Transaction Analysis")
    
    if os.path.exists(img2_path):
        with col2:
            st.image(img2_path, caption="Category Preferences & Platform Usage", use_container_width=True)
    else:
        with col2:
            st.warning("📊 Visualization 2: Spending Patterns")
    
    st.divider()
    
    # Key Conclusions
    st.markdown("## 🔑 Phase 1 Conclusions")
    
    st.success("""
    ### 🎯 Critical Discovery:
    
    The 18-25 age group represents a **MASSIVE UNTAPPED OPPORTUNITY**:
    
    ✅ **Highest transaction activity** compared to all other demographics  
    ✅ **Strong spending power** in high-margin categories  
    ✅ **Low credit risk** with healthy credit scores  
    ✅ **Digital native** - perfect for mobile-first credit card  
    ✅ **Underserved segment** - lacks tailored credit products  
    
    ### 💡 Strategic Insight:
    **Instead of generic credit card, we need a YOUTH CREDIT CARD specifically designed for this demographic!**
    """)

# ==========================================
# PHASE 2 - YOUTH CARD LAUNCH
# ==========================================
elif page == "💡 Youth Card Launch":
    st.title("💡 Youth Credit Card: Product Launch")
    st.markdown("### Strategy Shift Based on Phase 1 Insights")
    st.divider()
    
    st.markdown("## 🔄 Strategic Pivot Decision")
    
    st.info("""
    **Based on Phase 1 analysis revealing 18-25 as prime demographic, we pivoted strategy:**
    
    ❌ Generic credit card for all ages  
    ✅ **Specialized YOUTH CREDIT CARD for 18-25 segment**
    """)
    
    st.divider()
    
    # Product Launch
    st.markdown("## 🚀 Youth Credit Card Product Details")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🎁 Premium Benefits
        
        **Cashback & Rewards**
        - 2% cashback on Fashion
        - 3% on Electronics
        - 1.5% on other purchases
        - Sign-up bonus: ₹5,000
        
        **Exclusive Offers**
        - Partner discounts
        - Early access sales
        - Birthday benefits
        """)
    
    with col2:
        st.markdown("""
        ### 💳 Card Features
        
        **Flexible Limits**
        - Entry: ₹25,000
        - Regular: ₹50,000
        - Premium: ₹1,00,000
        
        **Zero Fees**
        - No annual fee
        - No joining fee
        - No hidden charges
        - Lifetime validity
        """)
    
    with col3:
        st.markdown("""
        ### 📱 Digital Experience
        
        **Mobile-First**
        - Instant digital approval
        - Paperless onboarding
        - AI-powered KYC
        - 5-min card issuance
        
        **App Features**
        - Real-time notifications
        - Contactless payments
        - Reward tracking
        - Savings tools
        """)
    
    st.divider()
    
    # Target Audience
    st.markdown("## 🎯 Target Audience Profile")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Who We're Targeting
        - **Age:** 18-25 years
        - **Income:** ₹2-8 LPA
        - **Lifestyle:** Urban, digital-native
        - **Behavior:** Tech-savvy, trend-conscious
        - **Segment:** Students, fresh graduates, early-career
        """)
    
    with col2:
        st.markdown("""
        ### Why They're Perfect
        - **High transaction frequency** (proven in Phase 1)
        - **Strong spending in target categories** (Fashion, Electronics)
        - **Low credit risk** (healthy credit scores)
        - **Digital adoption** (mobile-first users)
        - **Growth potential** (lifetime value)
        """)
    
    st.divider()
    
    # Marketing Strategy
    st.markdown("## 📢 Go-to-Market Strategy")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        ### 📱 Digital Channels
        - Instagram
        - YouTube
        - TikTok
        - Snapchat
        - WhatsApp
        """)
    
    with col2:
        st.markdown("""
        ### 🌟 Influencer Mix
        - Micro-influencers
        - Finance creators
        - Lifestyle influencers
        - Student ambassadors
        - Campus programs
        """)
    
    with col3:
        st.markdown("""
        ### 🎯 Partnerships
        - Amazon/Flipkart
        - Fashion brands
        - Electronics retailers
        - Cafes & restaurants
        - Entertainment apps
        """)
    
    with col4:
        st.markdown("""
        ### 💌 Communication
        - Personalized messaging
        - Referral programs
        - Exclusive previews
        - Limited-time offers
        - Community building
        """)
    
    st.divider()
    
    st.markdown("## ✨ Next: A/B Testing & Validation")
    st.info("Now we test this Youth Credit Card with real users through A/B campaign testing...")

# ==========================================
# PHASE 3 - A/B TESTING
# ==========================================
elif page == "🧪 Phase 2 Trial":
    st.title("🧪 Phase 2: A/B Testing Campaign")
    st.markdown("### Validating Youth Credit Card Market Reception")
    st.divider()
    
    st.markdown("## 📋 Campaign Methodology")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 👥 Control Group (A)
        
        **Sample:** 100 users   
        **Treatment:** No card promotion  
        **Purpose:** Baseline engagement  
        **Measurement:** Natural behavior
        """)
    
    with col2:
        st.markdown("""
        ### 🎯 Test Group (B)
        
        **Sample:** 100 users (18-25)  
        **Treatment:** Youth Card campaign  
        **Purpose:** Measure uplift  
        **Measurement:** Campaign impact
        """)
    
    st.divider()
    
    # Test Metrics
    st.markdown("## 📊 Test Metrics & Objectives")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🎯 Primary Metrics
        - Click-through rate
        - Application rate
        - Conversion rate
        - Engagement score
        """)
    
    with col2:
        st.markdown("""
        ### 📈 Secondary Metrics
        - Brand awareness lift
        - Purchase intent
        - Net sentiment
        - Social mentions
        """)
    
    with col3:
        st.markdown("""
        ### 💰 Business Metrics
        - Cost per acquisition
        - ROI on marketing
        - Customer lifetime value
        - Payback period
        """)
    
    st.divider()
    
    # Campaign Details
    st.markdown("## 🚀 Campaign Execution")
    
    st.markdown("""
    **Campaign Period:** 60 days  
    **Channels:** Instagram, YouTube, Facebook, Email  
    **Creative Focus:** Youth-centric messaging, benefits highlight  
    **Frequency:** 3-5 touchpoints per user  
    **Messaging:** "Card built for YOUR lifestyle"
    """)
    
    st.divider()
    
    st.markdown("## ⏳ Waiting for Results...")
    st.info("""
    🔄 **Campaign Running:** 60-day trial period active  
    📊 **Data Collection:** Real-time analytics tracking  
    📈 **Statistical Analysis:** Z-Test & hypothesis testing ready  
    ⏭️ **Next:** Phase evaluation with comprehensive results
    """)

# ==========================================
# PHASE 4 - RESULTS & LAUNCH
# ==========================================
elif page == "📊 Results & Launch":
    st.title("📊 Phase 2 Results: Campaign Success! 🎉")
    st.markdown("### Youth Credit Card Trial - VALIDATED & APPROVED FOR LAUNCH")
    st.divider()
    
    # Success Banner
    st.success("""
    ### 🎯 CAMPAIGN RESULTS: SUCCESS! 
    
    The Youth Credit Card A/B testing campaign has **EXCEEDED EXPECTATIONS** and proven the market viability!
    """)
    
    st.divider()
    
    # Statistical Results
    st.markdown("## 📈 Statistical Analysis Results")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Z-Score",
            "2.748",
            "✅ Highly Significant",
        )
    
    with col2:
        st.metric(
            "p-Value",
            "0.0029",
            "✅ < 0.05 (Rejected H₀)",
        )
    
    with col3:
        st.metric(
            "Conversion Uplift",
            "+27%",
            "✅ Test vs Control",
        )
    
    with col4:
        st.metric(
            "Campaign ROI",
            "35%",
            "✅ Positive Return",
        )
    
    st.divider()
    
    
    


    # Launch Decision
    st.markdown("## 🚀 LAUNCH DECISION")
    
    st.success("""
    ### ✅ APPROVED FOR FULL-SCALE LAUNCH
    
    **Status:** GREEN LIGHT ✅  
    **Decision:** Proceed with nationwide rollout  
    **Timeline:** Immediate activation across all channels  
    **Investment:** Approved for scaling
    
    ---
    
    **Why We're Launching:**
    
    ✅ **Market Validated** - A/B testing proves demand  
    ✅ **Statistically Significant** - p-value < 0.05  
    ✅ **Financially Viable** - Positive ROI confirmed  
    ✅ **Risk Managed** - Low default rates, high engagement  
    ✅ **Strategic Fit** - Aligns with growth goals  
    ✅ **Customer Ready** - Strong demand from segment  
    """)
    
    st.divider()
    
    
    
    # Final Conclusion
    st.markdown("## 🏆 Project Success Summary")
    
    st.success("""
    ### 🎯 Mission Accomplished!
    
    **Project Journey:**
    1. ✅ **Phase 0:** Identified need for new credit card
    2. ✅ **Phase 1:** Discovered 18-25 as prime opportunity
    3. ✅ **Phase 2:** Created Youth Credit Card product & Validated with A/B testing
    4. ✅ **Phase 3:** READY FOR LAUNCH!
    
    **Key Achievements:**
    - Market opportunity identified & validated
    - Product designed based on real customer insights
    - Campaign effectiveness proven statistically
    - Financial viability confirmed
    - Ready for immediate nationwide rollout
    
    **What's Next:**
    🚀 Full-scale market launch with multi-channel strategy
    📊 Real-time performance monitoring & optimization
    💰 Capture 2.5M+ youth cardholders in Year 1
    🌟 Establish market leadership in youth segment
    """)
    
    st.divider()
    
    # Call to Action
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.button("📊 View Phase 1 Analysis")
    
    with col2:
        st.button("💡 Youth Card Details")
    
    with col3:
        st.button("🚀 Launch Now!")

# ==========================================
# FOOTER
# ==========================================
st.divider()
st.markdown("""
<div style="text-align: center; margin-top: 4rem; padding: 2rem; border-top: 3px solid rgba(255, 0, 110, 0.4);">
    <p style="color: #1a1a2e; font-size: 1rem; font-weight: 600;">
        <strong>🎓 Youth Credit Card Launch Project</strong><br>
        📊 Data Analysis | 🎯 Strategy | 🚀 Market Validation<br><br>
        <strong>Author:</strong> R. Shrinivass | <strong>Role:</strong> Aspiring Data Scientist<br>
        🔗 <a href="https://github.com/Shrini14/Credit_Card_Launch" target="_blank" style="color: #ff006e; font-weight: 700;">GitHub Repository</a> | 
        © 2025 All Rights Reserved<br><br>
        <span style="color: #3a86ff; font-weight: 700;">✅ Project Status: READY FOR LAUNCH ✅</span>
    </p>
</div>
""", unsafe_allow_html=True)