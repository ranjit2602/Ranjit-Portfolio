import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Engineering Documentation | Ranjit B C",
    page_icon="⚙️",
    layout="wide"
)

# --- UNIFIED DARK TECH CSS ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    
    .stApp { background-color: #0e1117; }

    .project-card {
        border-left: 5px solid #00C6FF; 
        border-radius: 8px;
        padding: 25px;
        margin-bottom: 25px;
        background-color: #161b22; 
        color: #ffffff !important; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    .project-card h2, .project-card h3 {
        color: #00C6FF !important;
        margin-top: 0;
        font-weight: 700;
    }

    .project-card p, .project-card li {
        color: #c9d1d9 !important;
        line-height: 1.6;
    }

    .phase-label {
        background: #00C6FF;
        color: #0e1117 !important;
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 12px;
    }

    .link-button {
        display: inline-block;
        padding: 10px 20px;
        background-color: #00C6FF;
        color: #0e1117 !important;
        text-decoration: none;
        border-radius: 6px;
        font-weight: bold;
        margin-top: 15px;
    }

    .stVideo { border: 1px solid #30363d; border-radius: 12px; }
    </style>
    """, unsafe_allow_html=True
)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("📁 PROJECT LOGS")
    selection = st.radio(
        "Select System Documentation:",
        [
            "Wheelchair: Full-Cycle Development", 
            "PowerPedal™: Optical Torque Sensing",
            "HMI: E-Bike User Interface Design",
            "Digital: Websites & Dashboards",
            "Electric Skateboard: Final Year Project"
        ]
    )
    st.markdown("---")
    st.write("**Engineering Stack**")
    st.code("NX12 CAD / FEA\nOptical Encoding\nMaterial Science\nPython / Streamlit", language="text")

# =========================================================================
# 01. WHEELCHAIR
# =========================================================================
if selection == "Wheelchair: Full-Cycle Development":
    st.markdown('<h1 style="color:#00C6FF;">Electric Wheelchair Attachment</h1>', unsafe_allow_html=True)
    
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    col_v1_t, col_v1_v = st.columns([1.5, 1])
    with col_v1_t:
        st.markdown('<span class="phase-label">Phase I: V1 Baseline</span>', unsafe_allow_html=True)
        st.write("""
        **Objective:** Validate a propulsion system for manual wheelchairs capable of 15° gradients.
        - **Drivetrain:** High-torque BLDC integration with custom reduction ratios.
        - **Chassis:** Structural mild steel frame used to establish powertrain geometry and load paths.
        """)
    with col_v1_v:
        st.video("Wheelchair attachment Version 1.mp4")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    col_v2_v, col_v2_t = st.columns([1, 1.5])
    with col_v2_v:
        st.video("Wheelchair attachment Version 2.mp4")
    with col_v2_t:
        st.markdown('<span class="phase-label">Phase II: Optimization & Kinematics</span>', unsafe_allow_html=True)
        st.write("""
        **Iteration Results:**
        - **Material:** Transitioned to **Aluminum 6061-T6**, achieving a **36% mass reduction**.
        - **Docking Mechanism:** Proprietary spring-loaded indexing plunger for self-aligning quick-release.
        - **Performance:** Attachment time optimized to **under 10 seconds**.
        """)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 02. POWERPEDAL
# =========================================================================
elif selection == "PowerPedal™: Optical Torque Sensing":
    st.markdown('<h1 style="color:#00C6FF;">PowerPedal™: Optical Torque Sensing</h1>', unsafe_allow_html=True)
    
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    col_pp1, col_pp2 = st.columns([1.5, 1])
    with col_pp1:
        st.markdown('<span class="phase-label">Sensing Innovation</span>', unsafe_allow_html=True)
        st.write("""
        **Challenge:** Measuring torque in high-vibration environments without strain-gauge fatigue.
        - **System:** Non-Contact Optical Phase-Shift architecture.
        - **Logic:** Dual encoders detect microscopic torsion in a custom-engineered spindle.
        - **Fitment:** Engineered to fit standard **68mm-73mm BB shells**.
        """)
        
    with col_pp2:
        st.image("PowerSense.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    col_pp3, col_pp4 = st.columns([1, 1.5])
    with col_pp3:
        st.video("PowerPedal_Efficiency.mp4")
    with col_pp4:
        st.markdown('<span class="phase-label">Material Science</span>', unsafe_allow_html=True)
        st.write("""
        - **Spindle Material:** **7075-T6 Aluminum** selected for high yield strength and fatigue resistance.
        - **Resolution:** System calibrated for 0.1 Nm resolution under 150Nm loads.
        - **Protection:** IP67-rated enclosure for environmental isolation.
        """)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 03. HMI FOR EBIKES
# =========================================================================
elif selection == "HMI: E-Bike User Interface Design":
    st.markdown('<h1 style="color:#00C6FF;">HMI for eBikes: Right-Side Interface</h1>', unsafe_allow_html=True)
    
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    col_h1, col_h2 = st.columns([1, 1.5])
    with col_h1:
        st.image("HMI _ design.jpeg", use_container_width=True)
    with col_h2:
        st.markdown('<span class="phase-label">Ergonomic UI Design</span>', unsafe_allow_html=True)
        st.write("""
        **Interface Layout:**
        - **Visuals:** LED bar indicators for battery SoC and diagnostic status.
        - **Input:** Integrated twist-settings for assistance levels and boost throttle.
        - **Auxiliary:** Dedicated tactile switches for lighting and horn integration.
        """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    col_h3, col_h4 = st.columns([1.5, 1])
    with col_h3:
        st.markdown('<span class="phase-label">Prototyping & Surface Modeling</span>', unsafe_allow_html=True)
        st.write("""
        - **Modeling:** Complex ergonomic surfacing developed in **NX12**.
        - **Validation:** SLA/FDM 3D printing utilized to verify tactile response and assembly clearances.
        """)
    with col_h4:
        st.image("HMI_3d printed.jpeg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 04. DIGITAL: WEBSITES & DASHBOARDS
# =========================================================================
elif selection == "Digital: Websites & Dashboards":
    st.markdown('<h1 style="color:#00C6FF;">Digital Engineering & Data Infrastructure</h1>', unsafe_allow_html=True)

    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown("### Switch Mobility Official Portal")
    st.write("Communication platform for institutional IP (IISc/IIMB) and mechatronic concept visualization.")
    st.markdown('<a class="link-button" href="https://www.switchmobility.in/" target="_blank">🔗 switchmobility.in</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown("### PowerPedal™ Live Calibration Dashboard")
    st.write("Python/Streamlit utility for real-time visualization of torque curves (Nm) and phase-shift data for PID tuning.")
    st.markdown('<a class="link-button" href="https://powerpedaltestdashboard-4tmrensx9crg9j7ezjytog.streamlit.app/" target="_blank">⚙️ Live Test Analytics</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 05. ELECTRIC SKATEBOARD
# =========================================================================
else:
    st.markdown('<h1 style="color:#00C6FF;">Electric Skateboard: Final Year Project</h1>', unsafe_allow_html=True)
    
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    col_sk8_t, col_sk8_v = st.columns([1.5, 1])
    with col_sk8_t:
        st.markdown('<span class="phase-label">Drivetrain & Energy Management</span>', unsafe_allow_html=True)
        st.write("""
        **Project Scope:** Comprehensive mechatronic integration for personal mobility.
        - **Propulsion:** Dual BLDC motors with high-torque synchronous belt drives.
        - **Power:** Custom Li-ion pack assembly with integrated BMS for cell balancing and protection.
        - **Control:** 2.4GHz RF interface for precision throttle and regenerative braking.
        """)
        
    with col_sk8_v:
        st.video("Electric Skateboard.mp4")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown("### Engineering Takeaways")
    st.write("""
    - **Mechanical:** Developed road-shock isolation mounts for electronics protection.
    - **Thermal:** Optimized ESC heat dissipation for high-current operation.
    - **Project Management:** Coordinated multi-disciplinary milestones within a 4-member team.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Switch Mobility | Engineering Portfolio")