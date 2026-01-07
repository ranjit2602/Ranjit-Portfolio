import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Technical Portfolio | Ranjit B C",
    page_icon="⚙️",
    layout="wide"
)

# --- GLOBAL STYLE OPTIMIZATION ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&family=Inter:wght@400;700&display=swap');
    
    .stApp { background-color: #0e1117; }
    
    /* Unified Media Constraints */
    video, img {
        max-height: 400px;
        width: 100%;
        object-fit: contain;
        border-radius: 6px;
        border: 1px solid #30363d;
        margin-bottom: 10px;
    }

    .eng-title {
        font-family: 'Inter', sans-serif;
        color: #58a6ff;
        font-size: 2.2rem;
        font-weight: 700;
        border-bottom: 2px solid #30363d;
        padding-bottom: 10px;
        margin-bottom: 25px;
    }

    .eng-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
    }

    .tech-spec-header {
        font-family: 'Roboto Mono', monospace;
        color: #00C6FF;
        font-size: 0.9rem;
        text-transform: uppercase;
        margin-bottom: 12px;
        display: block;
        font-weight: bold;
    }

    .spec-list li {
        color: #c9d1d9 !important;
        font-size: 0.95rem;
        margin-bottom: 10px;
        line-height: 1.6;
    }

    b { color: #58a6ff; }
    hr { border-top: 1px solid #30363d; margin: 35px 0; }
    .impact-box { background: #1c2128; padding: 20px; border-radius: 8px; border-left: 4px solid #58a6ff; }

    [data-testid="stSidebar"] { background-color: #0a0d12 !important; border-right: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True
)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🔍 PROJECT LOGS")
    selection = st.radio(
        "Select Log:",
        [
            "Mid-Drive: Drivetrain Innovation", 
            "Wheelchair: Full-Cycle Development", 
            "PowerPedal™: Optical Sensing", 
            "HMI: Interface Engineering", 
            "Digital: Data Infrastructure", 
            "Skateboard: Mechatronics Capstone"
        ]
    )
    
    st.markdown("---")
    st.markdown("### 📱 NAVIGATION GUIDE")
    st.info("""
    **Desktop:** Use the radio buttons above.
    **Mobile:** Tap the **'>'** in the top left to open this project menu. 
    **Viewing:** Scroll down within each log to see technical specs and galleries.
    """)

# =========================================================================
# 00. MID-DRIVE: THE STRATEGIC PIVOT
# =========================================================================
if selection == "Mid-Drive: Drivetrain Innovation":
    st.markdown('<h1 class="eng-title">Mid-Drive Propulsion: The Strategic Pivot</h1>', unsafe_allow_html=True)
    
    st.markdown('<div class="impact-box">', unsafe_allow_html=True)
    st.write("""
    **The "Intel Inside" Strategy:** While competitors focused on frame-building and branding, we realized 
    no one in India was developing proprietary drivetrains. We pivoted to become the first in the country 
    to build a homegrown mid-drive, turning our competitors into our customers.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("")

    col1, col2 = st.columns([1.5, 1], gap="large")
    
    with col1:
        st.markdown('<span class="tech-spec-header">// SYSTEM ARCHITECTURE</span>', unsafe_allow_html=True)
        st.image("mid-drive1.jpeg")
        
        img_col1, img_col2 = st.columns(2)
        with img_col1:
            st.image("mid-drive2.jpeg")
        with img_col2:
            st.image("mid-drive2.jpeg")

    with col2:
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.markdown('<span class="tech-spec-header">My Engineering Contributions:</span>', unsafe_allow_html=True)
        st.write("""
        
        - **Requirement Math:** Calculated torque constants ($K_t$) and voltage constants ($K_v$) for Indian road gradients.
        - **Gearing Logic:** Optimized reduction ratios to maximize motor efficiency at low speeds.
        - **Custom Casing:** Designed the entire enclosure in NX for IP67 sealing and high heat dissipation.
        - **Vendor Management:** Spec'd and sourced custom motor windings from 3rd party partners.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.markdown('<span class="tech-spec-header">RECOGNITION</span>', unsafe_allow_html=True)
        st.success("Project funded and validated by the **IISc Design Clinic Scheme grant**.")
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 01. WHEELCHAIR: TOTAL PROJECT OWNERSHIP
# =========================================================================
elif selection == "Wheelchair: Full-Cycle Development":
    st.markdown('<h1 class="eng-title">Wheelchair System: Full-Cycle Engineering</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.5, 1], gap="large")
    with col1:
        st.video("Wheelchair attachment Version 1.mp4")
        st.caption("Functional validation in real-world residential environments.")
    with col2:
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.markdown('<span class="tech-spec-header">TOTAL PROJECT OWNERSHIP</span>', unsafe_allow_html=True)
        st.write("""
        I maintained **complete end-to-end responsibility** for this system. This wasn't just a design exercise; I led:
        - **Primary Field Research:** Identifying core mobility barriers.
        - **Mechatronic Architecture:** Defining drivetrain and power requirements.
        - **Sourcing & Costing:** Managing NGO-level budget constraints.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    col3, col4 = st.columns([1, 1.2], gap="large")
    with col3:
        st.image("Wheelchair.gif", use_container_width=True)
        st.caption("PoC: Validating the tool-less attachment concept.")
    with col4:
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.markdown('<span class="tech-spec-header">// STAGE 1: POC & KINEMATICS</span>', unsafe_allow_html=True)
        st.markdown('<ul class="spec-list">', unsafe_allow_html=True)
        st.write("""
        <li><b>Qualitative-to-Quantitative:</b> Translated user feedback into technical specs for a high-torque drivetrain capable of <b>15° gradients</b>.</li>
        <li><b>NX12 Modeling:</b> Developed the initial master model to test docking clearances and structural interference.</li>
        <li><b>Stress Testing:</b> Field trials identified that Version 1, while functional, required <b>mass optimization</b> for independent handling.</li>
        """, unsafe_allow_html=True)
        st.markdown('</ul>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown('<span class="tech-spec-header">// STAGE 2: ADVANCED OPTIMIZATION (VERSION 2)</span>', unsafe_allow_html=True)
    col5, col6, col7 = st.columns([1, 1, 1], gap="small")
    with col5:
        st.video("Wheelchair attachment Version 2.mp4")
        st.caption("Testing the optimized Version 2 mechanism.")
    with col6:
        st.image("Wheelchair attachment Version 2.jpeg")
        st.caption("Close-up: Refined clamping & structural assembly.")
    with col7:
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.write("""
        **V2 Improvements:**
        - **Material Transition:** Switched to **6061-T6 Aluminum**, reducing total system mass by **36%**.
        - **Docking Speed:** Engineered a self-aligning plunger system for **<10s attachment**.
        - **Production Ready:** Generated the final **BOM** and manufacturing drawings.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.image("Wheelchair flyer.png", use_container_width=True)
    st.markdown("""
    <div class="impact-box">
    <b>Final Impact:</b> This project stands as proof of my ability to manage the <b>entire engineering lifecycle</b>. By combining empathy for the user with rigorous material science and kinematic design, I delivered a system that solves a real-world problem within strict NGO economic constraints.
    </div>
    """, unsafe_allow_html=True)

# =========================================================================
# 02. POWERPEDAL™
# =========================================================================
elif selection == "PowerPedal™: Optical Sensing":
    st.markdown('<h1 class="eng-title">PowerPedal™ <span class="patent-tag">Patented</span></h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1.4], gap="large")
    with col1:
        st.video("Powerpedal Testing.mp4")
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.markdown('<span class="tech-spec-header">// SYSTEM INTENT</span>', unsafe_allow_html=True)
        st.write("""
        Delivering a **mid-drive responsiveness** using cost-effective hub-drive hardware. 
        By measurement of torque at the pedal, we eliminate the mechanical complexity and high cost of traditional mid-drive motors.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.markdown('<span class="tech-spec-header">// MECHANICAL ARCHITECTURE ROLE</span>', unsafe_allow_html=True)
        st.write("I was responsible for the **mechanical realization** of the torque-sensing architecture, ensuring precision metrology within the harsh environment of a bicycle bottom bracket.")
        st.markdown('<ul class="spec-list">', unsafe_allow_html=True)
        st.write("""
        <li><b>Torsional Sensing Element:</b> Selected and engineered <b>EN47 Spring Steel</b> for its high elastic limit and stable, repeatable angular deflection under cyclic loads.</li>
        <li><b>Optical Metrology Integration:</b> Designed the interfaces coupling the torsional element to optical encoders—measuring relative angular displacement without the fatigue issues of strain gauges.</li>
        <li><b>Constraint Management:</b> Iterated layouts to fit within standard BB axial/radial limits while isolating load paths from parasitic bending (noise).</li>
        <li><b>DFM:</b> Optimized assembly sequences and encoder placement tolerances for high-volume manufacturing.</li>
        """, unsafe_allow_html=True)
        st.markdown('</ul>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    col3, col4 = st.columns(2, gap="medium")
    with col3:
        st.image("PowerSense.png")
    with col4:
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.markdown('<span class="tech-spec-header">// PATENT ALIGNMENT</span>', unsafe_allow_html=True)
        st.write("""
        The patented architecture centers on the mechanical arrangement that enables **torque-proportional control of a hub-drive motor**. 
        My work provided the physical embodiment required to translate pedal torsion into high-fidelity digital signals.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 03. HMI
# =========================================================================
elif selection == "HMI: Interface Engineering":
    st.markdown('<h1 class="eng-title">HMI: Integrated E-Bike Control Interface</h1>', unsafe_allow_html=True)
    st.markdown('<div class="eng-card">', unsafe_allow_html=True)
    st.markdown('<span class="tech-spec-header">// CORE OBJECTIVE</span>', unsafe_allow_html=True)
    st.write("""
    Consolidated multiple disparate e-bike controls—<b>throttle, assist-level, battery indication, and horn</b>—into a 
    single ergonomic enclosure. The goal was to reduce handlebar clutter while enabling intuitive, one-handed 
    operation under real riding conditions.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        st.image("HMI _ design.jpeg")
        st.caption("CAD Design: Industrial design of the enclosure focusing on ergonomic button reach and component housing.")
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.markdown('<span class="tech-spec-header">// INDUSTRIAL & MECHANICAL DESIGN</span>', unsafe_allow_html=True)
        st.markdown('<ul class="spec-list">', unsafe_allow_html=True)
        st.write("""
        <li><b>Ergonomics:</b> Defined specific button reach zones to prevent accidental inputs while riding.</li>
        <li><b>Internal Geometry:</b> Designed complex internal routing for wiring, throttle mechanisms, and PCB mounts.</li>
        <li><b>Robustness:</b> Optimized structural integrity to withstand outdoor environmental stresses and handlebar vibrations.</li>
        """, unsafe_allow_html=True)
        st.markdown('</ul>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.image("HMI_3d printed.jpeg")
        st.caption("Functional Prototype: 3D-printed unit used to validate hand ergonomics and handlebar fitment.")
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.markdown('<span class="tech-spec-header">// RAPID PROTOTYPING</span>', unsafe_allow_html=True)
        st.markdown('<ul class="spec-list">', unsafe_allow_html=True)
        st.write("""
        <li><b>Tolerance Management:</b> Prepared 3D models with specific wall thicknesses and draft angles for additive manufacturing.</li>
        <li><b>Physical Validation:</b> Printed multiple iterations to evaluate tactile feedback and mechanical fitment of moving parts.</li>
        <li><b>Fast Iteration:</b> Used physical testing to refine the form factor before committing to final design freezes.</li>
        """, unsafe_allow_html=True)
        st.markdown('</ul>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 04. DIGITAL
# =========================================================================
elif selection == "Digital: Data Infrastructure":
    st.markdown('<h1 class="eng-title">Digital Infrastructure: Data Visualization</h1>', unsafe_allow_html=True)
    st.markdown('<div class="eng-card">', unsafe_allow_html=True)
    st.markdown('<span class="tech-spec-header">// CORE OBJECTIVE</span>', unsafe_allow_html=True)
    st.write("""
    I developed a unified digital ecosystem to serve three critical functions: **Public Communication**, 
    **Internal Engineering Analysis**, and a **Live Interactive Pitch Deck**. By replacing static slides 
    with dynamic data storytelling, I created an evidence-driven narrative for institutional investors and engineers.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 1], gap="large")
    with col1:
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.markdown('<span class="tech-spec-header">// INTERACTIVE PITCH DECK (Differentiator)</span>', unsafe_allow_html=True)
        st.write("""
        Instead of traditional presentation decks, I designed and built a live dashboard-based pitch system. 
        This allowed stakeholders to:
        - Explore performance metrics and system comparisons dynamically.
        - Verify engineering claims through real-time data transparency.
        - Engage with an evidence-driven narrative rather than marketing claims.
        """)
        st.link_button("🚀 Launch Pitch Dashboard", "https://powerpedal-pitch-dashboard.streamlit.app/")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.markdown('<span class="tech-spec-header">// WEB ARCHITECTURE & VISIBILITY</span>', unsafe_allow_html=True)
        st.write("""
        I designed and developed the high-quality product website to establish credibility and 
        communicate complex technical value to both institutional and non-technical audiences.
        """)
        st.link_button("🌐 Visit Switch Mobility", "https://www.switchmobility.in/")
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 05. SKATEBOARD (CAPSTONE)
# =========================================================================
else:
    st.markdown('<h1 class="eng-title">Capstone: Electric Propulsion & Control</h1>', unsafe_allow_html=True)
    col1, col2 = st.columns([1.4, 1], gap="large")
    with col1:
        st.video("Electric Skateboard.mp4")
    with col2:
        st.markdown('<div class="eng-card">', unsafe_allow_html=True)
        st.markdown('<span class="tech-spec-header">// MECHANICAL OWNERSHIP & PID LOGIC</span>', unsafe_allow_html=True)
        st.markdown('<ul class="spec-list">', unsafe_allow_html=True)
        st.write("""
        <li><b>Mechanical Integration:</b> Designed motor mounts, drivetrain layout, and enclosures to electrify a standard deck without compromising flexibility.</li>
        <li><b>Control Logic:</b> Applied and tuned <b>PID control parameters</b> at the controller level to mitigate jerk and achieve smooth, linear acceleration.</li>
        <li><b>Dynamics:</b> Balanced torque delivery against urban riding constraints to ensure predictable rider-friendly power delivery.</li>
        """, unsafe_allow_html=True)
        st.markdown('</ul>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="impact-box">
    <b>The Entrepreneurial Spark:</b> This project marked my transition from academic theory to product thinking. Converting a conventional system into an electrified product taught me the value of <b>iteration and usability</b>. It was here that my journey of building real-world solutions began.
    </div>
    """, unsafe_allow_html=True)