"""
All in One AI · Story Studio
Streamlit App — Dark Holographic Theme
"""

import streamlit as st
import time

# ─── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="All in One AI · Story Studio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── CSS: Dark holographic theme ──────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@400;500;600;700&family=Syne:wght@400;600;700;800&display=swap');

/* ── Root variables ── */
:root {
    --bg:      #0E0E10;
    --bg2:     #13131A;
    --bg3:     #16161A;
    --bg4:     #1E1E24;
    --border:  rgba(255,255,255,0.07);
    --border2: rgba(255,255,255,0.13);
    --text:    #E8E6E0;
    --muted:   #888780;
    --dim:     #444441;
    --t1:      #7C6FE0;
    --t1l:     rgba(124,111,224,0.15);
    --t2:      #3DAF82;
    --t2l:     rgba(61,175,130,0.15);
    --t3:      #E09040;
    --t3l:     rgba(224,144,64,0.15);
    --t4:      #6090D0;
    --t4l:     rgba(96,144,208,0.15);
    --t5:      #D06080;
    --t5l:     rgba(208,96,128,0.15);
}

/* ── Global ── */
html, body, [class*="css"] {
    font-family: 'Noto Sans Thai', 'Syne', sans-serif !important;
    background-color: var(--bg) !important;
    color: var(--text) !important;
}

/* ── Hide Streamlit defaults ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 1.5rem 2rem !important; max-width: 100% !important; }
.stDeployButton { display: none; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: var(--bg2) !important;
    border-right: 1px solid var(--border2) !important;
    padding-top: 0 !important;
}
[data-testid="stSidebar"] > div:first-child { padding: 0; }
[data-testid="stSidebarNavItems"] { display: none; }

/* ── Sidebar radio buttons → menu items ── */
[data-testid="stSidebar"] .stRadio > label { display: none; }
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
    display: flex;
    flex-direction: column;
    gap: 2px;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
    display: flex !important;
    align-items: center;
    gap: 10px;
    padding: 9px 14px !important;
    border-radius: 8px !important;
    cursor: pointer !important;
    color: var(--muted) !important;
    font-size: 13px !important;
    border: none !important;
    background: transparent !important;
    transition: all 0.15s !important;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
    background: rgba(124,111,224,0.08) !important;
    color: var(--text) !important;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label[data-baseweb="radio"] span:first-child {
    display: none !important;
}
[data-testid="stSidebar"] input[type="radio"]:checked + div label,
[data-testid="stSidebar"] .stRadio [aria-checked="true"] {
    background: rgba(124,111,224,0.15) !important;
    color: #A89FF0 !important;
    border-left: 2px solid var(--t1) !important;
}

/* ── Inputs ── */
.stTextArea textarea {
    background: var(--bg4) !important;
    border: 1px solid var(--border2) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
    font-family: 'Noto Sans Thai', sans-serif !important;
    font-size: 13px !important;
}
.stTextArea textarea:focus {
    border-color: var(--t1) !important;
    box-shadow: 0 0 0 1px var(--t1) !important;
}
.stTextArea textarea::placeholder { color: var(--dim) !important; }

/* ── Selectbox / dropdown ── */
.stSelectbox > div > div {
    background: var(--bg4) !important;
    border: 1px solid var(--border2) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #2D2860, #1A3D2E) !important;
    border: 1px solid rgba(124,111,224,0.4) !important;
    border-radius: 10px !important;
    color: #A89FF0 !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    letter-spacing: 0.03em !important;
    padding: 0.5rem 1.5rem !important;
    transition: all 0.2s !important;
    width: 100% !important;
}
.stButton > button:hover {
    border-color: var(--t1) !important;
    color: #C4BEFF !important;
    box-shadow: 0 0 16px rgba(124,111,224,0.2) !important;
}

/* ── Progress bar ── */
.stProgress > div > div > div {
    background: linear-gradient(90deg, var(--t1), var(--t2)) !important;
    border-radius: 4px !important;
}
.stProgress > div > div {
    background: var(--bg4) !important;
    border-radius: 4px !important;
}

/* ── Metrics ── */
[data-testid="metric-container"] {
    background: var(--bg3) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    padding: 14px 16px !important;
}
[data-testid="metric-container"] label {
    color: var(--muted) !important;
    font-size: 11px !important;
}
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: var(--text) !important;
    font-size: 22px !important;
    font-weight: 700 !important;
}
[data-testid="metric-container"] [data-testid="stMetricDelta"] {
    font-size: 11px !important;
}

/* ── Divider ── */
hr { border-color: var(--border) !important; margin: 0.8rem 0 !important; }

/* ── Tab ── */
.stTabs [data-baseweb="tab-list"] {
    background: transparent !important;
    border-bottom: 1px solid var(--border2) !important;
    gap: 0 !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: var(--muted) !important;
    border: none !important;
    padding: 8px 16px !important;
    font-size: 13px !important;
}
.stTabs [aria-selected="true"] {
    color: #A89FF0 !important;
    border-bottom: 2px solid var(--t1) !important;
}

/* ── Card helper ── */
.card {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 18px 20px;
    margin-bottom: 12px;
}
.card-title {
    font-size: 12px;
    font-weight: 600;
    color: #A89FF0;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 6px;
}
.gradient-bar {
    height: 2px;
    background: linear-gradient(90deg, #7C6FE0, #3DAF82, #6090D0);
    border-radius: 1px;
    margin-bottom: 14px;
}
.badge-done {
    background: rgba(61,175,130,0.15);
    color: #3DAF82;
    padding: 2px 8px;
    border-radius: 10px;
    font-size: 10px;
}
.badge-render {
    background: rgba(224,144,64,0.15);
    color: #E09040;
    padding: 2px 8px;
    border-radius: 10px;
    font-size: 10px;
}
.badge-queue {
    background: rgba(124,111,224,0.12);
    color: #7C6FE0;
    padding: 2px 8px;
    border-radius: 10px;
    font-size: 10px;
}
.engine-done {
    background: rgba(61,175,130,0.07);
    border: 1px solid rgba(61,175,130,0.2);
    border-radius: 8px;
    padding: 8px 10px;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 5px;
    font-size: 12px;
    color: #888780;
}
.engine-active {
    background: rgba(124,111,224,0.1);
    border: 1px solid rgba(124,111,224,0.45);
    border-radius: 8px;
    padding: 8px 10px;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 5px;
    font-size: 12px;
    color: #A89FF0;
    font-weight: 500;
}
.engine-pending {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 8px;
    padding: 8px 10px;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 5px;
    font-size: 12px;
    color: #444441;
}
.shot-card {
    background: var(--bg4);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 10px 12px;
    margin-bottom: 8px;
}
.shot-done { border-color: rgba(61,175,130,0.3) !important; }
.shot-active { border-color: rgba(124,111,224,0.5) !important; }
.stat-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 5px 0;
    border-bottom: 1px solid var(--border);
    font-size: 12px;
}
.stat-row:last-child { border-bottom: none; }

/* ── Lock sidebar width + hide collapse button ── */
[data-testid="stSidebar"] {
    min-width: 210px !important;
    max-width: 210px !important;
    overflow: hidden !important;
}
[data-testid="stSidebarCollapseButton"] { display: none !important; }
section[data-testid="collapsedControl"] { display: none !important; }
button[data-testid="baseButton-header"] { display: none !important; }

/* ── Lock horizontal scroll ── */
.main .block-container { overflow-x: hidden !important; }

/* ── Standard button same height as High Quality and Ultra ── */
.stButton > button {
    min-height: 70px !important;
    height: 70px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}
</style>
""", unsafe_allow_html=True)


# ─── Session state ─────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "🏠 สร้างใหม่"
if "idea" not in st.session_state:
    st.session_state.idea = ""
if "quality" not in st.session_state:
    st.session_state.quality = "High Quality"


# ─── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    # Logo
    st.markdown("""
    <div style="padding:18px 16px 14px;border-bottom:1px solid rgba(255,255,255,0.07);margin-bottom:8px;">
        <div style="display:flex;align-items:center;gap:10px;">
            <div style="width:32px;height:32px;border-radius:8px;
                background:linear-gradient(135deg,rgba(124,111,224,0.3),rgba(61,175,130,0.3));
                border:1px solid rgba(124,111,224,0.4);
                display:flex;align-items:center;justify-content:center;font-size:15px;">✦</div>
            <div>
                <div style="font-size:13px;font-weight:700;color:#E8E6E0;">All in One AI</div>
                <div style="font-size:9px;color:#7C6FE0;letter-spacing:0.06em;">STORY STUDIO</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Navigation
    st.markdown('<div style="font-size:9px;color:#444441;letter-spacing:0.1em;text-transform:uppercase;padding:4px 14px 6px;">เมนูหลัก</div>', unsafe_allow_html=True)

    page = st.radio(
        "nav",
        ["🏠 สร้างใหม่", "⚙ Production", "▦ Storyboard", "▷ Video Player", "☰ Library"],
        label_visibility="collapsed",
        key="nav_radio"
    )
    st.session_state.page = page

    st.markdown('<div style="font-size:9px;color:#444441;letter-spacing:0.1em;text-transform:uppercase;padding:10px 14px 6px;">Mythology</div>', unsafe_allow_html=True)

    traditions = {
        "● Hindu / Thai": "#3DAF82",
        "● Norse":        "#6090D0",
        "● Greek":        "#E09040",
        "● Chinese":      "#D06080",
        "● Japanese":     "#7C6FE0",
    }
    for name, color in traditions.items():
        st.markdown(f'<div style="padding:7px 14px;font-size:12px;color:{color};cursor:pointer;">{name}</div>', unsafe_allow_html=True)

    # Self Training progress
    st.markdown("---")
    st.markdown("""
    <div style="background:#1E1E24;border-radius:10px;padding:10px 12px;border:1px solid rgba(124,111,224,0.2);margin:0 4px;">
        <div style="display:flex;justify-content:space-between;margin-bottom:6px;">
            <span style="font-size:10px;color:#7C6FE0;font-weight:500;">Self Training</span>
            <span style="font-size:10px;color:#7C6FE0;">88%</span>
        </div>
        <div style="height:3px;background:rgba(255,255,255,0.06);border-radius:2px;overflow:hidden;">
            <div style="width:88%;height:100%;background:linear-gradient(90deg,#7C6FE0,#3DAF82);border-radius:2px;"></div>
        </div>
        <div style="font-size:9px;color:#444441;margin-top:5px;">Engine 14 · อีก 12 samples</div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
#  PAGE 1 — HOME
# ══════════════════════════════════════════════════════════════

def page_home():
    # Header
    st.markdown("""
    <div style="margin-bottom:20px;">
        <div style="font-size:10px;color:#7C6FE0;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:4px;">
            All in One AI · Story Studio
        </div>
        <h1 style="font-size:22px;font-weight:700;color:#E8E6E0;margin:0 0 4px;">สร้างเรื่องราวใหม่</h1>
        <p style="font-size:12px;color:#888780;margin:0;">1 Click 1 Story — ปล่อยจินตนาการของคุณ</p>
    </div>
    """, unsafe_allow_html=True)

    col_main, col_side = st.columns([2, 1], gap="medium")

    with col_main:
        st.markdown('<div class="gradient-bar"></div>', unsafe_allow_html=True)
        st.markdown('<div class="card-title">✦ ใส่ไอเดียของคุณ</div>', unsafe_allow_html=True)

        idea = st.text_area(
            "idea_input",
            placeholder="พิมพ์ไอเดีย เช่น 'สร้างตอนกำเนิดพระพรหม' หรือ 'Thor vs Jormungandr'...",
            height=100,
            label_visibility="collapsed",
            key="idea_box"
        )

        # Example chips
        st.markdown("""
        <div style="margin:8px 0 14px;display:flex;flex-wrap:wrap;gap:6px;">
            <span style="font-size:10px;color:#888780;background:#1E1E24;border:1px solid rgba(255,255,255,0.07);padding:4px 10px;border-radius:20px;cursor:pointer;">กำเนิดพระพรหม</span>
            <span style="font-size:10px;color:#888780;background:#1E1E24;border:1px solid rgba(255,255,255,0.07);padding:4px 10px;border-radius:20px;cursor:pointer;">Thor vs Jormungandr</span>
            <span style="font-size:10px;color:#888780;background:#1E1E24;border:1px solid rgba(255,255,255,0.07);padding:4px 10px;border-radius:20px;cursor:pointer;">ซุนโงคงก่อกวนสวรรค์</span>
            <span style="font-size:10px;color:#888780;background:#1E1E24;border:1px solid rgba(255,255,255,0.07);padding:4px 10px;border-radius:20px;cursor:pointer;">พระอิศวรระบำ Tandava</span>
        </div>
        """, unsafe_allow_html=True)

        # Quality selector
        st.markdown('<div style="font-size:10px;color:#555552;letter-spacing:0.06em;text-transform:uppercase;margin-bottom:8px;">Production Quality</div>', unsafe_allow_html=True)

        q_col1, q_col2, q_col3 = st.columns(3)
        quality = st.session_state.quality

        with q_col1:
            st.markdown(f"""
            <div style="background:{'rgba(124,111,224,0.1)' if quality=='Standard' else '#1E1E24'};
                border:1px solid {'rgba(124,111,224,0.5)' if quality=='Standard' else 'rgba(255,255,255,0.07)'};
                border-radius:10px;padding:10px;text-align:center;cursor:pointer;">
                <div style="font-size:12px;font-weight:600;color:{'#A89FF0' if quality=='Standard' else '#888780'};">Standard</div>
                <div style="font-size:9px;color:{'#7C6FE0' if quality=='Standard' else '#444441'};margin-top:2px;">~5 min · 30 steps</div>
            </div>""", unsafe_allow_html=True)
            if st.button("Standard", key="q_std", use_container_width=True):
                st.session_state.quality = "Standard"
                st.rerun()

        with q_col2:
            st.markdown(f"""
            <div style="background:{'rgba(124,111,224,0.1)' if quality=='High Quality' else '#1E1E24'};
                border:1px solid {'rgba(124,111,224,0.5)' if quality=='High Quality' else 'rgba(255,255,255,0.07)'};
                border-radius:10px;padding:10px;text-align:center;cursor:pointer;">
                <div style="font-size:9px;font-weight:600;color:#7C6FE0;letter-spacing:0.08em;margin-bottom:2px;">RECOMMENDED</div>
                <div style="font-size:12px;font-weight:600;color:{'#A89FF0' if quality=='High Quality' else '#888780'};">High Quality</div>
                <div style="font-size:9px;color:{'#7C6FE0' if quality=='High Quality' else '#444441'};margin-top:2px;">~15 min · 50 steps</div>
            </div>""", unsafe_allow_html=True)
            if st.button("High Quality", key="q_hq", use_container_width=True):
                st.session_state.quality = "High Quality"
                st.rerun()

        with q_col3:
            st.markdown(f"""
            <div style="background:{'rgba(124,111,224,0.1)' if quality=='Ultra' else '#1E1E24'};
                border:1px solid {'rgba(124,111,224,0.5)' if quality=='Ultra' else 'rgba(255,255,255,0.07)'};
                border-radius:10px;padding:10px;text-align:center;cursor:pointer;">
                <div style="font-size:9px;font-weight:600;color:#E09040;letter-spacing:0.08em;margin-bottom:2px;">EPIC</div>
                <div style="font-size:12px;font-weight:600;color:{'#A89FF0' if quality=='Ultra' else '#888780'};">Ultra</div>
                <div style="font-size:9px;color:{'#E09040' if quality=='Ultra' else '#444441'};margin-top:2px;">~45 min · 80 steps</div>
            </div>""", unsafe_allow_html=True)
            if st.button("Ultra", key="q_ultra", use_container_width=True):
                st.session_state.quality = "Ultra"
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("⚡  Start AI Production", key="start_btn", use_container_width=True):
            if idea.strip():
                st.session_state.idea = idea
                st.success("✦ เริ่ม Production แล้ว! ไปที่หน้า Production เพื่อดู progress")
            else:
                st.warning("กรุณาใส่ idea ก่อนครับ")

    with col_side:
        st.markdown('<div class="gradient-bar" style="background:linear-gradient(90deg,#3DAF82,#6090D0,#7C6FE0);"></div>', unsafe_allow_html=True)
        st.markdown('<div class="card-title"><span style="color:#3DAF82;">◷</span> Episodes ล่าสุด</div>', unsafe_allow_html=True)

        episodes = [
            ("🌟", "กำเนิดพระพรหม",     "done",   "3:20", "#7C6FE0"),
            ("⚡", "Ragnarok",           "done",   "4:12", "#6090D0"),
            ("🐉", "ก่อกวนสวรรค์",       "render", "2:58", "#3DAF82"),
            ("🏛", "Birth of Athena",    "done",   "3:45", "#E09040"),
            ("🔱", "Tandava",            "done",   "3:05", "#D06080"),
        ]

        for icon, title, status, duration, color in episodes:
            badge = f'<span class="badge-done">✓ done</span>' if status == "done" else f'<span class="badge-render">⟳ render</span>'
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:8px;padding:8px 10px;
                border-radius:8px;margin-bottom:4px;background:rgba(255,255,255,0.02);
                border:1px solid rgba(255,255,255,0.04);cursor:pointer;">
                <div style="width:32px;height:22px;border-radius:5px;
                    background:linear-gradient(135deg,{color}22,{color}11);
                    border:1px solid {color}44;display:flex;align-items:center;
                    justify-content:center;font-size:13px;flex-shrink:0;">{icon}</div>
                <div style="flex:1;min-width:0;">
                    <div style="font-size:11px;color:#C4C0D8;overflow:hidden;
                        text-overflow:ellipsis;white-space:nowrap;">{title}</div>
                    <div style="display:flex;align-items:center;gap:6px;margin-top:2px;">
                        {badge}
                        <span style="font-size:9px;color:#444441;">{duration}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div style="text-align:center;margin-top:6px;"><span style="font-size:11px;color:#7C6FE0;cursor:pointer;">ดูทั้งหมด →</span></div>', unsafe_allow_html=True)

    # Stats row
    st.markdown("<br>", unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.metric("วิดีโอทั้งหมด", "47", delta="+3 สัปดาห์นี้")
    with s2:
        st.metric("รอ Render", "3", delta=None)
    with s3:
        st.metric("ประหยัดเวลา", "128h", delta="+12h")
    with s4:
        st.metric("อัตราสำเร็จ", "98%", delta="+1%")


# ══════════════════════════════════════════════════════════════
#  PAGE 2 — PRODUCTION PROGRESS
# ══════════════════════════════════════════════════════════════

def page_production():
    st.markdown("""
    <div style="margin-bottom:20px;">
        <div style="font-size:10px;color:#7C6FE0;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:4px;">Production Pipeline</div>
        <h1 style="font-size:22px;font-weight:700;color:#E8E6E0;margin:0 0 4px;">Production Progress</h1>
        <p style="font-size:12px;color:#888780;margin:0;">ติดตามสถานะการทำงานของ 14 AI Engines</p>
    </div>
    """, unsafe_allow_html=True)

    # Episode info + overall progress
    ep_col, prog_col = st.columns([3, 1])
    with ep_col:
        st.markdown("""
        <div style="background:#16161A;border:1px solid rgba(255,255,255,0.08);border-radius:14px;padding:16px 20px;">
            <div class="gradient-bar"></div>
            <div style="font-size:10px;color:#444441;margin-bottom:4px;">Episode #a3f9b2</div>
            <div style="font-size:16px;font-weight:700;color:#E8E6E0;margin-bottom:2px;">กำเนิดพระพรหมจาก Cosmic Lotus</div>
            <div style="font-size:11px;color:#888780;">Hindu Mythology · origin · epic · cosmic</div>
        </div>
        """, unsafe_allow_html=True)

    with prog_col:
        st.markdown("""
        <div style="background:#16161A;border:1px solid rgba(124,111,224,0.25);border-radius:14px;
            padding:16px;text-align:center;">
            <div style="font-size:32px;font-weight:700;color:#A89FF0;">63%</div>
            <div style="font-size:10px;color:#888780;">ความคืบหน้า</div>
            <div style="font-size:10px;color:#7C6FE0;margin-top:4px;">~8 นาที</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div style="font-size:11px;color:#7C6FE0;font-weight:500;margin-bottom:4px;">Engine 11: Production Engine กำลังทำงาน</div>', unsafe_allow_html=True)
    st.progress(0.63)
    st.markdown('<div style="font-size:11px;color:#888780;margin-top:4px;">⟳ Stable Diffusion กำลัง render Shot 7 — Wide shot: พระพรหมปรากฏกาย...</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Stats
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Shots Rendered", "7 / 11")
    with c2:
        st.metric("QC Passed", "6")
    with c3:
        st.metric("เวลาที่เหลือ", "~8 min")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div style="font-size:10px;color:#444441;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:10px;">14 Engine Pipeline</div>', unsafe_allow_html=True)

    engines = [
        (1,  "Idea Engine",           "done"),
        (2,  "Expert Role Engine",    "done"),
        (3,  "AI Director Engine",    "done"),
        (4,  "Mythology Engine",      "done"),
        (5,  "Tool Decision Engine",  "done"),
        (6,  "Adaptive Strategy",     "done"),
        (7,  "Prompt Intelligence",   "done"),
        (8,  "Cinematic Physics",     "done"),
        (9,  "Divine Sound Engine",   "done"),
        (10, "Style DNA Engine",      "done"),
        (11, "Production Engine",     "active"),
        (12, "Quality Control",       "pending"),
        (13, "Story Universe",        "pending"),
        (14, "Self Training",         "pending"),
    ]

    col_a, col_b = st.columns(2)
    for i, (num, name, status) in enumerate(engines):
        col = col_a if i % 2 == 0 else col_b
        with col:
            if status == "done":
                icon = "✓"
                css_class = "engine-done"
                color = "#3DAF82"
            elif status == "active":
                icon = "◉"
                css_class = "engine-active"
                color = "#A89FF0"
            else:
                icon = "○"
                css_class = "engine-pending"
                color = "#444441"

            st.markdown(f"""
            <div class="{css_class}">
                <span style="color:{color};font-size:11px;width:14px;">{icon}</span>
                <span style="font-size:10px;color:{color};min-width:18px;opacity:0.6;">{num}</span>
                <span>{name}</span>
            </div>
            """, unsafe_allow_html=True)

    # Log
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div style="font-size:10px;color:#444441;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:8px;">Production Log</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#13131A;border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:12px 14px;font-family:monospace;">
        <div style="font-size:11px;color:#444441;">[09:42:01] ✓ Engine 1-10 completed</div>
        <div style="font-size:11px;color:#444441;">[09:43:12] ✓ Shot 1-6 rendered · QC passed</div>
        <div style="font-size:11px;color:#A89FF0;">[09:51:34] ◉ Shot 7 rendering · SD 50 steps...</div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
#  PAGE 3 — STORYBOARD
# ══════════════════════════════════════════════════════════════

def page_storyboard():
    st.markdown("""
    <div style="margin-bottom:20px;">
        <div style="font-size:10px;color:#7C6FE0;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:4px;">Episode #a3f9b2</div>
        <h1 style="font-size:22px;font-weight:700;color:#E8E6E0;margin:0 0 4px;">Storyboard</h1>
        <p style="font-size:12px;color:#888780;margin:0;">กำเนิดพระพรหมจาก Cosmic Lotus · 11 shots · 3:20</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Passed ✓", "6")
    with c2: st.metric("Rendering ⟳", "1")
    with c3: st.metric("Queued ○", "4")
    with c4: st.metric("Avg QC", "0.89")

    st.markdown("<br>", unsafe_allow_html=True)

    shots = [
        (1,  "จักรวาลก่อนกำเนิด",      "done",   "wide · static · 12s",       "divine_glow",       0.92),
        (2,  "มหาสมุทรแห่งจักรวาล",    "done",   "aerial · crane · 18s",      "ethereal",          0.88),
        (3,  "ดอกบัวทองผุด",           "done",   "medium · dolly · 14s",      "divine_glow",       0.91),
        (4,  "สี่พักตร์เผยออก",         "done",   "close-up · tilt · 10s",     "dramatic",          0.85),
        (5,  "พระพรหมบนบัลลังก์บัว",   "done",   "wide · pan · 20s",          "epic",              0.90),
        (6,  "ดวงตาศักดิ์สิทธิ์",       "done",   "extreme-close · static · 8s","mystical",         0.87),
        (7,  "พระพรหมสร้างสรรพสิ่ง",   "active", "wide · crane · 22s",        "epic",              None),
        (8,  "แสงสร้างสรรค์",           "pending","medium · dolly · 16s",      "divine_glow",       None),
        (9,  "จักรวาลกำเนิด",           "pending","aerial · pan · 18s",        "epic",              None),
        (10, "พระพรหมท่ามกลางดาว",      "pending","wide · static · 14s",       "mystical",          None),
        (11, "บทสรุป cosmic",           "pending","aerial · crane · 20s",      "serene",            None),
    ]

    # แสดง 2 columns
    for i in range(0, len(shots), 2):
        col_l, col_r = st.columns(2)
        for j, col in [(i, col_l), (i+1, col_r)]:
            if j >= len(shots):
                break
            num, title, status, meta, lighting, score = shots[j]
            with col:
                if status == "done":
                    border = "rgba(61,175,130,0.3)"
                    status_html = f'<span class="badge-done">✓ QC {score}</span>'
                    bg = "linear-gradient(135deg,#0a0500,#1a0a00)"
                elif status == "active":
                    border = "rgba(124,111,224,0.5)"
                    status_html = '<span class="badge-render">◉ Rendering...</span>'
                    bg = "rgba(0,0,0,0.5)"
                else:
                    border = "rgba(255,255,255,0.05)"
                    status_html = f'<span class="badge-queue">○ รอคิว</span>'
                    bg = "rgba(0,0,0,0.25)"

                st.markdown(f"""
                <div style="background:#16161A;border:1px solid {border};border-radius:10px;
                    overflow:hidden;margin-bottom:10px;">
                    <div style="height:56px;background:{bg};display:flex;align-items:center;
                        justify-content:center;position:relative;border-bottom:1px solid {border};">
                        <span style="font-size:9px;color:#888780;position:absolute;top:6px;left:8px;">Shot {num}</span>
                        <span style="position:absolute;top:6px;right:8px;">{status_html}</span>
                        <span style="font-size:9px;color:#444441;position:absolute;bottom:6px;left:8px;">{meta}</span>
                        <span style="font-size:18px;color:rgba(124,111,224,0.3);">▶</span>
                    </div>
                    <div style="padding:10px 12px;">
                        <div style="font-size:12px;font-weight:500;color:#E8E6E0;margin-bottom:3px;">{title}</div>
                        <div style="display:flex;gap:6px;">
                            <span style="font-size:9px;background:#1E1E24;border:1px solid rgba(255,255,255,0.06);
                                color:#888780;padding:2px 7px;border-radius:10px;">{lighting}</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
#  PAGE 4 — VIDEO PLAYER
# ══════════════════════════════════════════════════════════════

def page_player():
    st.markdown("""
    <div style="margin-bottom:20px;">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;">
            <div>
                <div style="font-size:10px;color:#3DAF82;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:4px;">Production Complete ✓</div>
                <h1 style="font-size:20px;font-weight:700;color:#E8E6E0;margin:0 0 2px;">กำเนิดพระพรหมจาก Cosmic Lotus</h1>
                <p style="font-size:12px;color:#888780;margin:0;">The Birth of Brahma from the Cosmic Lotus · Episode #a3f9b2</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Success banner
    st.success("✦ Production เสร็จสมบูรณ์ — 11 shots · QC avg 0.89 · ใช้เวลา 14m 32s")

    player_col, info_col = st.columns([2, 1], gap="medium")

    with player_col:
        # Video player mockup
        st.markdown("""
        <div style="background:#000;border-radius:12px;overflow:hidden;aspect-ratio:2.39/1;position:relative;
            display:flex;align-items:center;justify-content:center;
            background:linear-gradient(135deg,#0a0500 0%,#1a0800 40%,#100500 70%,#050200 100%);">
            <div style="text-align:center;">
                <div style="width:56px;height:56px;border-radius:50%;
                    background:rgba(124,111,224,0.15);border:1px solid rgba(124,111,224,0.4);
                    display:flex;align-items:center;justify-content:center;margin:0 auto 10px;cursor:pointer;">
                    <span style="font-size:22px;color:#A89FF0;margin-left:3px;">▶</span>
                </div>
                <div style="font-size:11px;color:rgba(124,111,224,0.6);">กำเนิดพระพรหม · 3:20 · 4K Cinematic</div>
            </div>
            <div style="position:absolute;top:10px;right:12px;font-size:9px;
                background:rgba(0,0,0,0.6);border:1px solid rgba(124,111,224,0.2);
                color:#7C6FE0;padding:3px 8px;border-radius:4px;">4K · 2.39:1</div>
            <div style="position:absolute;bottom:0;left:0;right:0;height:32px;
                background:rgba(0,0,0,0.7);display:flex;align-items:center;padding:0 12px;gap:10px;">
                <span style="font-size:11px;color:rgba(240,230,208,0.7);">▶</span>
                <div style="flex:1;height:3px;background:rgba(255,255,255,0.15);border-radius:2px;">
                    <div style="width:0%;height:100%;background:#7C6FE0;border-radius:2px;"></div>
                </div>
                <span style="font-size:10px;color:rgba(240,230,208,0.5);white-space:nowrap;">0:00 / 3:20</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div style="font-size:12px;color:#888780;margin-bottom:8px;">ให้คะแนน Episode นี้ (feedback → Engine 14)</div>', unsafe_allow_html=True)

        rating = st.slider("rating", 1, 5, 4, label_visibility="collapsed", key="rating_slider")
        stars = "★" * rating + "☆" * (5 - rating)
        st.markdown(f'<div style="font-size:22px;color:#E09040;letter-spacing:4px;">{stars}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="font-size:11px;color:#888780;margin-top:4px;">คุณให้ {rating}/5 ดาว · AI จะเรียนรู้จาก feedback นี้</div>', unsafe_allow_html=True)

    with info_col:
        # Stats
        st.markdown("""
        <div class="gradient-bar" style="background:linear-gradient(90deg,#3DAF82,#6090D0,#7C6FE0);"></div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="card-title">📊 Video Info</div>', unsafe_allow_html=True)

        info_rows = [
            ("Duration",     "3:20"),
            ("Resolution",   "3840×1608"),
            ("Shots",        "11"),
            ("QC Score",     "0.89"),
            ("Quality",      "High Quality"),
            ("Color Grade",  "divine_gold_lut"),
            ("Tradition",    "Hindu"),
            ("Universe",     "✓ Registered"),
        ]
        for label, value in info_rows:
            color = "#3DAF82" if value.startswith("✓") else "#E8E6E0"
            st.markdown(f"""
            <div class="stat-row">
                <span style="color:#888780;">{label}</span>
                <span style="color:{color};font-weight:500;">{value}</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="card-title">⬇ Download</div>', unsafe_allow_html=True)

        for label in ["Download MP4 (4K)", "Download MP4 (1080p)", "Download Audio", "Download Subtitle (.srt)"]:
            st.button(label, key=f"dl_{label}", use_container_width=True)


# ══════════════════════════════════════════════════════════════
#  PAGE 5 — LIBRARY
# ══════════════════════════════════════════════════════════════

def page_library():
    st.markdown("""
    <div style="margin-bottom:20px;">
        <div style="font-size:10px;color:#7C6FE0;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:4px;">All Episodes</div>
        <h1 style="font-size:22px;font-weight:700;color:#E8E6E0;margin:0 0 4px;">Episode Library</h1>
        <p style="font-size:12px;color:#888780;margin:0;">8 episodes · 5 traditions · Universe Canon active</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Episodes", "8")
    with c2: st.metric("Total Runtime", "26m")
    with c3: st.metric("Avg QC Score", "0.88")
    with c4: st.metric("Traditions", "5")

    st.markdown("<br>", unsafe_allow_html=True)

    # Search
    search = st.text_input("🔍 ค้นหา Episodes...", placeholder="พิมพ์ชื่อ episode...", key="lib_search", label_visibility="collapsed")

    st.markdown("<br>", unsafe_allow_html=True)

    episodes = [
        ("🌟", "กำเนิดพระพรหม",          "Hindu",   "origin",         "3:20", "0.89", "★★★★☆", "#7C6FE0"),
        ("⚡", "Ragnarok: Battle of Gods", "Norse",   "battle",         "4:12", "0.91", "★★★★★", "#6090D0"),
        ("🐉", "ก่อกวนสวรรค์วังหยก",      "Chinese", "journey",        "2:58", "0.86", "★★★★☆", "#3DAF82"),
        ("🏛", "Birth of Athena",          "Greek",   "origin",         "3:45", "0.90", "★★★★☆", "#E09040"),
        ("🔱", "Tandava — จังหวะทำลาย",   "Hindu",   "transformation", "3:05", "0.87", "★★★★☆", "#D06080"),
        ("⚔", "สงครามเทวดาและอสูร",       "Thai",    "war",            "2:42", "0.84", "★★★☆☆", "#7C6FE0"),
    ]

    filtered = [ep for ep in episodes if not search or search.lower() in ep[1].lower() or search.lower() in ep[2].lower()]

    for i in range(0, len(filtered), 2):
        col_l, col_r = st.columns(2)
        for j, col in [(i, col_l), (i+1, col_r)]:
            if j >= len(filtered):
                break
            icon, title, tradition, ep_type, duration, qc, stars, color = filtered[j]
            with col:
                st.markdown(f"""
                <div style="background:#16161A;border:1px solid rgba(255,255,255,0.07);border-radius:12px;
                    overflow:hidden;margin-bottom:10px;cursor:pointer;
                    transition:border-color 0.2s;">
                    <div style="height:70px;background:linear-gradient(135deg,{color}22,{color}11,#0d0d12);
                        display:flex;align-items:center;justify-content:center;position:relative;">
                        <span style="position:absolute;top:7px;left:8px;font-size:9px;
                            background:{color}22;border:1px solid {color}44;color:{color};
                            padding:2px 7px;border-radius:10px;">{tradition}</span>
                        <span style="position:absolute;top:7px;right:8px;font-size:9px;
                            background:rgba(61,175,130,0.15);color:#3DAF82;
                            padding:2px 7px;border-radius:10px;">QC {qc}</span>
                        <span style="font-size:28px;color:rgba(255,255,255,0.25);">{icon}</span>
                        <span style="position:absolute;bottom:7px;right:8px;font-size:9px;color:#444441;">{duration}</span>
                    </div>
                    <div style="padding:10px 12px;">
                        <div style="font-size:10px;color:{color};margin-bottom:2px;">{ep_type}</div>
                        <div style="font-size:12px;font-weight:500;color:#E8E6E0;margin-bottom:4px;">{title}</div>
                        <div style="font-size:14px;color:#E09040;letter-spacing:2px;">{stars}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    # Universe timeline
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div style="font-size:10px;color:#444441;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:10px;">Universe Canon Timeline</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#16161A;border:1px solid rgba(255,255,255,0.07);border-radius:12px;padding:14px 16px;">
        <div style="display:flex;flex-direction:column;gap:8px;padding-left:16px;border-left:1px solid rgba(124,111,224,0.25);">
            <div style="font-size:11px;color:#888780;"><span style="color:#7C6FE0;margin-right:8px;">●</span><span style="color:#444441;margin-right:10px;">Primordial</span>กำเนิดพระพรหม</div>
            <div style="font-size:11px;color:#888780;"><span style="color:#7C6FE0;margin-right:8px;">●</span><span style="color:#444441;margin-right:10px;">Ancient</span>สงครามเทวดา, Tandava</div>
            <div style="font-size:11px;color:#888780;"><span style="color:#7C6FE0;margin-right:8px;">●</span><span style="color:#444441;margin-right:10px;">Mythic Age</span>Birth of Athena, ก่อกวนสวรรค์</div>
            <div style="font-size:11px;color:#888780;"><span style="color:#7C6FE0;margin-right:8px;">●</span><span style="color:#444441;margin-right:10px;">Cosmic</span>Ragnarok: Battle of Gods</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
#  ROUTER
# ══════════════════════════════════════════════════════════════

page_map = {
    "🏠 สร้างใหม่": page_home,
    "⚙ Production":  page_production,
    "▦ Storyboard":  page_storyboard,
    "▷ Video Player": page_player,
    "☰ Library":     page_library,
}

current = st.session_state.get("nav_radio", "🏠 สร้างใหม่")
page_map.get(current, page_home)()
