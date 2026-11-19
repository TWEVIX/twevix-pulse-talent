import base64
import pandas as pd
import streamlit as st

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="TWEVIX PULSE™ | Verified Analyst & Intern Directory",
    page_icon="favicon.png",
    layout="wide",
)
with open("logo.png", "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode()



st.markdown(
    """
    <style>
    .stApp { background-color: #020617; color: #f8fafc; }
    .hero-banner {
        background: linear-gradient(135deg, rgba(251,191,36,0.16) 0%, #0f172a 70%);
        border: 1px solid rgba(251,191,36,0.4);
        border-radius: 16px;
        padding: 28px 32px;
        margin-bottom: 24px;
    }
    .talent-card {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-left: 4px solid #fbbf24;
        border-radius: 16px;
        padding: 22px 24px;
        margin-bottom: 12px;
    }
    .passport-img {
        width: 92px;
        height: 92px;
        border-radius: 14px;
        object-fit: cover;
        border: 2px solid #fbbf24;
    }
    .skill-pill {
        display: inline-block;
        background: rgba(251,191,36,0.12);
        color: #fcd34d;
        border: 1px solid rgba(251,191,36,0.35);
        padding: 4px 11px;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 600;
        margin: 3px 5px 3px 0;
    }
    .tenure-badge {
        display: inline-block;
        background: rgba(16,185,129,0.15);
        color: #6ee7b7;
        border: 1px solid rgba(52,211,153,0.35);
        padding: 4px 12px;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 700;
    }
    .stButton > button, .stLinkButton > a {
        background: #fbbf24 !important;
        color: #020617 !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        border: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def get_tenure_tier(cycle_count: int):
    months = cycle_count * 3
    if cycle_count == 1:
        return f"{months} Months Verified (1 Cycle)", "Associate Decision Analyst"
    elif cycle_count == 2:
        return f"{months} Months Verified (2 Cycles)", "Applied Decision-Intelligence Specialist"
    else:
        return f"{months} Months Verified ({cycle_count} Cycles)", "Lead Operational Data Architect"

DEFAULT_RECORDS = [
    {
        "analyst_id": "TVX-001",
        "name": "Jean-Paul Mugisha",
        "photo_url": "https://ui-avatars.com",
        "institution": "University of Rwanda (BSc Data Science)",
        "location": "Kigali, Rwanda (Remote / Hybrid)",
        "availability": "Open to Full-Time & Remote Contract",
        "skills_with_years": "Python (2.5 Yrs) | SQL & Pandas (2 Yrs) | Margin & Waste Analytics (6 Mos) | RFM Segmentation (1 Yr)",
        "linkedin": "https://linkedin.com",
        "cycle_number": "Cycle 01 (3 Months)",
        "credential_id": "TVX-8F4A2C91E0B7",
        "deployment_title": "Perishable Waste & RFM Retention Engine for Kigali Artisan Bakery",
        "impact_metric": "+14% Monthly Net Margin • -22% Perishable Waste",
    },
    {
        "analyst_id": "TVX-001",
        "name": "Jean-Paul Mugisha",
        "photo_url": "https://ui-avatars.com",
        "institution": "University of Rwanda (BSc Data Science)",
        "location": "Kigali, Rwanda (Remote / Hybrid)",
        "availability": "Open to Full-Time & Remote Contract",
        "skills_with_years": "Python (2.5 Yrs) | SQL & Pandas (2 Yrs) | Margin & Waste Analytics (6 Mos) | RFM Segmentation (1 Yr)",
        "linkedin": "https://linkedin.com",
        "cycle_number": "Cycle 02 (3 Months)",
        "credential_id": "TVX-4B9E10D7C3A2",
        "deployment_title": "East African Agricultural Supply-Chain Price Volatility Forecaster",
        "impact_metric": "12,000+ Market Records Modeled • -18% Forecast Error",
    },
    {
        "analyst_id": "TVX-002",
        "name": "Aline Uwase",
        "photo_url": "https://ui-avatars.com",
        "institution": "African Leadership University (ALU)",
        "location": "Kigali, Rwanda (Remote / On-Site)",
        "availability": "Open to Paid Internship & Junior Analyst Roles",
        "skills_with_years": "Operational Analytics (1.5 Yrs) | Time-Series Forecasting (1 Yr) | Anomaly Detection (6 Mos) | PowerBI & Excel (2 Yrs)",
        "linkedin": "https://linkedin.com",
        "cycle_number": "Cycle 01 (3 Months)",
        "credential_id": "TVX-3D91B7E4A205",
        "deployment_title": "Cold-Chain Drift Audit & 14-Day Roster Modeling for Outpatient Clinic",
        "impact_metric": "2 Early Compressor Failures Prevented • -19% Overtime Cost",
    },
]

@st.cache_data(ttl=300)
def load_talent():
    url = st.secrets.get("PULSE_SHEET_CSV_URL", "")
    if url:
        try:
            return pd.read_csv(url).fillna("").to_dict(orient="records")
        except Exception:
            pass
    return DEFAULT_RECORDS

records = load_talent()

grouped = {}
for row in records:
    aid = str(row.get("analyst_id", ""))
    if aid not in grouped:
        grouped[aid] = {
            "name": row.get("name", ""),
            "photo_url": row.get("photo_url") or f"https://ui-avatars.com{str(row.get('name', 'Analyst')).replace(' ', '+')}&background=fbbf24&color=020617&size=200",
            "institution": row.get("institution", ""),
            "location": row.get("location", "Remote / Hybrid"),
            "availability": row.get("availability", "Open to Opportunities"),
            "skills_with_years": row.get("skills_with_years", "Python (1 Yr) | Data Analytics (1 Yr)"),
            "linkedin": row.get("linkedin", "https://linkedin.com"),
            "cycles": [],
        }
    grouped[aid]["cycles"].append(row)
st.markdown(
    f"""
        <div style="display:flex;align-items:center;gap:16px;padding:0 0 12px 0;margin-bottom:28px;">

        <img src="data:image/png;base64,{logo_b64}" style="width:62px;height:62px;border-radius:50%;border:2px solid #fbbf24;object-fit:cover;" />
        <div>
            <div style="font-size:26px;font-weight:900;letter-spacing:-0.02em;line-height:1.1;color:#f8fafc;">
                TWEVIX <span style="color:#fbbf24;">PULSE™</span>
            </div>
            <div style="font-size:12px;font-weight:700;letter-spacing:0.16em;color:#94a3b8;text-transform:uppercase;margin-top:4px;">
                VERIFIED TALENT • HR-TECH DIRECTORY
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-banner">
        <div style="color:#fbbf24;font-size:0.78rem;font-weight:800;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:6px;">
            TWEVIX PULSE™ • HR-TECH TALENT MARKETPLACE
        </div>
        <h1 style="margin:0 0 8px 0;font-size:2rem;">Verified Analyst &amp; Intern Directory</h1>
        <p style="color:#94a3b8;margin:0;max-width:760px;">
            Recruit pre-vetted data scientists and analysts backed by stackable 3-to-12+ month field deployments, verified skills, and SHA-256 credentials.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

f1, f2 = st.columns(2)
with f1:
    min_tenure = st.selectbox(
        "Minimum Verified Experience",
        ["All Verified Talent", "3+ Months (1+ Cycles)", "6+ Months (2+ Cycles)", "9+ Months (3+ Cycles)"],
    )
with f2:
    avail_filter = st.selectbox(
        "Hiring Availability",
        ["All Availability", "Full-Time", "Internship", "Contract"],
    )

min_map = {"All Verified Talent": 1, "3+ Months (1+ Cycles)": 1, "6+ Months (2+ Cycles)": 2, "9+ Months (3+ Cycles)": 3}
req_cycles = min_map[min_tenure]

for aid, person in grouped.items():
    cycles = person["cycles"]
    if len(cycles) < req_cycles:
        continue
    if avail_filter != "All Availability" and avail_filter.lower() not in person["availability"].lower():
        continue

    tenure_label, tier_title = get_tenure_tier(len(cycles))
    skills_html = "".join(
        [f'<span class="skill-pill">{s.strip()}</span>' for s in str(person["skills_with_years"]).split("|") if s.strip()]
    )

    st.markdown(
        f"""
        <div class="talent-card">
            <div style="display:flex;gap:20px;align-items:flex-start;flex-wrap:wrap;">
                <img src="{person['photo_url']}" alt="{person['name']}" class="passport-img" />
                <div style="flex:1;min-width:240px;">
                    <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;">
                        <h3 style="margin:0;color:#f8fafc;">{person['name']}</h3>
                        <span class="tenure-badge">{tenure_label} • {tier_title}</span>
                    </div>
                    <p style="color:#94a3b8;margin:6px 0 10px 0;font-size:0.9rem;">
                        <strong>Education:</strong> {person['institution']} &nbsp;|&nbsp;
                        <strong>Location:</strong> {person['location']} &nbsp;|&nbsp;
                        <strong>Status:</strong> {person['availability']}
                    </p>
                    <div style="font-size:0.76rem;font-weight:700;color:#cbd5e1;margin-bottom:4px;">VERIFIED SKILLS &amp; YEARS:</div>
                    <div>{skills_html}</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    b1, b2, b3 = st.columns([2, 1, 1])
    with b1:
        with st.expander(f"Inspect {len(cycles)} Audited Deployment(s)"):
            for c in cycles:
                st.markdown(
                    f"- **{c.get('cycle_number', '')}** (`{c.get('credential_id', '')}`): "
                    f"*{c.get('deployment_title', '')}* → **{c.get('impact_metric', '')}**"
                )
    with b2:
        st.link_button("LinkedIn Profile →", person["linkedin"], use_container_width=True)
    with b3:
        st.link_button(
            "Book Interview →",
            f"mailto:info.pulse@://gmail.com{person['name'].replace(' ', '%20')}",
            use_container_width=True,
        )

st.divider()
st.link_button("← Back to TWEVIX PULSE™ Home", " https://pulse.twevix.com/")
