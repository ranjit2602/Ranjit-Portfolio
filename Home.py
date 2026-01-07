import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Ranjit B C | Portfolio",
    page_icon="⚙️",
    layout="wide"
)

# --- CSS: HIGH-CONTRAST VISIBILITY ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    
    .stApp { background-color: #0e1117; }

    /* The "Ranjit" Name Fix */
    .hero-name {
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 4.5rem;
        background: linear-gradient(90deg, #00C6FF, #0072FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
        line-height: 1.1;
    }

    .hero-subtitle {
        color: #005A9C !important;
        font-size: 1.5rem;
        font-weight: 700;
        margin-top: -5px;
        margin-bottom: 20px;
    }

    /* Skill Card - Forced Visibility */
    .skill-card {
        border: 2px solid #005A9C; 
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 15px;
        background-color: #161b22; 
        color: #ffffff !important; 
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }
    
    .skill-card h3 {
        color: #00C6FF !important; 
        margin-top: 0;
        font-weight: 700;
    }

    .skill-card ul { color: #ffffff !important; }

    /* Stats Table Visibility */
    .stats-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
        color: white;
    }
    .stats-table th {
        padding: 10px;
        border: 1px solid #005A9C;
        color: #00C6FF;
        background: #0a0d12;
    }
    .stats-table td {
        padding: 10px;
        border: 1px solid #005A9C;
        text-align: center;
        font-weight: bold;
        color: #ffffff;
    }

    /* Sidebar Fix */
    section[data-testid="stSidebar"] {
        background-color: #0a0d12 !important;
        border-right: 1px solid #30363d;
    }
    </style>
    """, unsafe_allow_html=True
)

# --- SIDEBAR (NAVIGATION ONLY) ---
with st.sidebar:
    st.title("Navigation")
    st.info("Select the **Projects** page in the sidebar to view technical logs")
    st.markdown("---")

# --- MAIN PROFILE SECTION ---
col_img, col_info = st.columns([1, 2.5], gap="large")

with col_img:
    st.image("ranjit_profile.jpg", use_container_width=True)
    
    # LINKS ON MAIN PAGE
    st.markdown("""
        <div style="background: #161b22; padding: 15px; border-radius: 8px; border: 1px solid #005A9C; margin-top: 10px;">
            <p style="margin-bottom: 5px;">📧 <a href="mailto:ranjitshekar@gmail.com" style="color: #00C6FF; text-decoration: none;">ranjitshekar@gmail.com</a></p>
            <p style="margin-bottom: 5px;">🔗 <a href="https://linkedin.com/in/ranjitbc" target="_blank" style="color: #00C6FF; text-decoration: none;">linkedin.com/in/ranjitbc</a></p>
            <p style="margin-bottom: 5px;">🐙 <a href="https://github.com/ranjit2602" target="_blank" style="color: #00C6FF; text-decoration: none;">github.com/ranjit2602</a></p>
            <p style="margin-bottom: 0px;">🌐 <a href="https://switchmobility.in" target="_blank" style="color: #00C6FF; text-decoration: none;">switchmobility.in</a></p>
        </div>
    """, unsafe_allow_html=True)

with col_info:
    st.markdown('<h1 class="hero-name">Ranjit B C</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Founder, Switch Mobility | Systems Integration</p>', unsafe_allow_html=True)
    
    st.markdown(f"""
        <p style="color: white; font-size: 1.1rem;">
        Driven by a passion for transforming nascent ideas into validated, <b>market-ready electromechanical products</b>. 
        I have <b>six years</b> of comprehensive experience in full-stack hardware development, spanning from 3D modeling and custom PCB design to factory execution and final product deployment.
        <br><br>
        My focus is on <b>Mechatronics and Advanced Systems</b>, with a proven ability to lead innovation, resulting in 
        <b>patented systems</b> 
        </p>
    """, unsafe_allow_html=True)
    

st.markdown("<br><hr>", unsafe_allow_html=True)

# --- SKILLS MATRIX ---
st.header("🛠️ Core Technical Expertise")

s1, s2 = st.columns(2)

with s1:
    st.markdown("""
        <div class="skill-card">
            <h3>⚙️ Mechanical Design</h3>
            <ul>
                <li><b>NX12:</b> Advanced 3D Modeling & Assemblies</li>
                <li><b>Manufacturing:</b> DFM/DFA, CNC Machining</li>
                <li><b>Process:</b> Iterative Prototyping & Testing</li>
            </ul>
        </div>
        <div class="skill-card">
            <h3>💻 Programming & Data</h3>
            <ul>
                <li><b>Languages:</b> Python, Embedded C/C++</li>
                <li><b>Control:</b> PID Algorithms, Real-Time Feedback</li>
                <li><b>Tools:</b> Pandas, Streamlit Dashboarding</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with s2:
    st.markdown("""
        <div class="skill-card">
            <h3>🔩 System Integration</h3>
            <ul>
                <li><b>End-to-End:</b> Idea to Market-Ready Product</li>
                <li><b>Electronics:</b> Custom PCB & HMI Development</li>
                <li><b>Architecture:</b> Robust Electromechanical Design</li>
            </ul>
        </div>
        <div class="skill-card">
            <h3>☁️ Deployment & DevOps</h3>
            <ul>
                <li><b>Web:</b> Custom Site Building & Cloud Hosting</li>
                <li><b>Dashboards:</b> Streamlit App Deployment</li>
                <li><b>Version Control:</b> Git/GitHub Architecture</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)