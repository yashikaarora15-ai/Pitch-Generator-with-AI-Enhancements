import streamlit as st
from utils.generator import generate_pitch
from utils.ai_enhancer import enhance_pitch_with_ai
from utils.sanitizer import clean_input, sanitize_pitch
from utils.review import save_review

#To store pitch temporarily
if "generated_pitch" not in st.session_state:
    st.session_state.generated_pitch = None

# ---------------------------------
# Page Config
# ---------------------------------
st.set_page_config(
    page_title="PitchPerfect",
    layout="wide"
)

# ---------------------------------
# Custom CSS (Dark Premium UI)
# ---------------------------------
st.markdown("""
<style>
.main { background-color: #0f172a; }
h1, h2, h3, h4 { color: #f8fafc; }
.stTextInput > div > div > input,
.stSelectbox > div > div,
.stNumberInput > div > div > input { background-color: #1e293b; color: white; }
.stButton>button { background-color: #6366f1; color: white; border-radius: 10px; height: 3em; width: 100%; font-size: 16px; }
.stButton>button:hover { background-color: #4f46e5; color: white; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------
# Title
# ---------------------------------
st.markdown("""
<h1 style='text-align:center;
background: linear-gradient(90deg, #6366f1, #22d3ee);
-webkit-background-clip: text;
color: transparent;'>
Pitch Generator
</h1>
""", unsafe_allow_html=True)

# ---------------------------------
# Category Selection
# ---------------------------------
category_display = st.selectbox(
    "Select Pitch Type",
    [
        "Internship",
        "Job",
        "Project Showcase",
        "Freelancing",
        "Business / Startups",
        "Networking / Bio",
        "Presentation"
    ]
)

category_map = {
    "Internship": "internship",
    "Job": "job",
    "Project Showcase": "project",
    "Freelancing": "freelancer",
    "Business / Startups": "business",
    "Networking / Bio": "networking",
    "Presentation": "presentation"
}

category = category_map[category_display]

# ---------------------------------
# Category-Based Inputs
# ---------------------------------
if category in ["internship", "job", "project"]:
    st.subheader("Personal Details")
    name = st.text_input("Your Name")
    domain = st.text_input("Domain / Field")
    skills = st.text_input("Skills (comma separated)")
    project_name = st.text_input("Project / Work Title(e.g.:Pitch generator)")
    problem = st.text_input("Problem that your project/work solved (optional)(e.g.:generating pitches manually)")
    beneficiary = st.text_input("Who benefited(e.g.:students) (optional)")

    # Extra fields per type
    if category == "internship":
        current_status = st.text_input("Current Status (e.g.: 3rd year, B.Tech Student...)")
        internship_type = st.text_input("Type of Internship(e.g.:Ai Internships...)")
    else:
        current_status = ""
        internship_type = ""

    if category == "job":
        years = st.number_input("Years of Experience", 0, 50, 0, 1)
        job_role = st.text_input("Job Role Applying For(e.g.:ML Engineer)")
    else:
        years = 0
        job_role = ""

elif category == "freelancer":
    st.subheader("Freelance Details")
    name = st.text_input("Your Name")
    domain = st.text_input("Service Domain(e.g.:Graphic Designer...)")
    services = st.text_input("Services You Offer(e.g.:Logo design, branding kits...)")
    project_name = st.text_input("Recent Project Name")
    problem = st.text_input("Problem Solved(e.g.:Inconsistent branding...) (optional)")
    beneficiary = st.text_input("Client / Beneficiary(e.g.:Tech startups) (optional)")

elif category == "networking":
    st.subheader("Personal Details")
    name = st.text_input("Your Name")
    domain = st.text_input("Your Main Domain(e.g.:AI/ML,UI/UX design...)")
    interests = st.text_input("Areas of Interest(e.g.:coding projects,branding...) (comma separated)")
    current_focus = st.text_input("Current Focus(e.g.:building AI projects...) (optional)")
    achievement = st.text_input("Any Achievement (e.g.:elevator pitch tool used by 50+ peers...)(optional)")

elif category == "presentation":
    name = st.text_input("Your Name")
    project_title = st.text_input("Project Title")
    current_status = st.text_input("Your Current Status(e.g.:developer...)")
    problem_statement = st.text_area("Problem Statement(detailed, e.g.:Freelancers struggle to create...)")
    solution = st.text_area("Your Solution(Detailed, e.g.:Web app that generates...)")
    impact = st.text_area("Impact / Results(e.g.:Used by 50+ peers...)")
    audience = st.text_input("Target Audience(e.g.:CS students, freelance developers...) (Optional)")

else:
    # Business
    st.subheader("Business Details")
    business_name = st.text_input("Business / Startup Name(e.g.:PixelCraft Studio...)")
    domain = st.text_input("Industry / Domain(e.g.:Graphic Design...)")
    target_audience = st.text_input("Target Audience(e.g.:tech startups...)")
    problem = st.text_input("Market Problem(e.g.:inconsistent branding across platforms...)")
    product_name = st.text_input("Product / Platform Name(e.g.:BrandSync Kit...)")
    solution = st.text_input("Your Solution(e.g.:complete visual identity packages with style guides...)")

# ---------------------------------
# AI Enhancement Section
# ---------------------------------
st.divider()
st.subheader("✨ AI Enhancement")
enhance = st.checkbox("Enhance pitch with AI for better impact")
st.divider()

# ---------------------------------
# Generate Button
# ---------------------------------
generate = st.button("Generate Pitch")

if generate:
    # Basic required check
    if category in ["internship", "job", "project", "freelancer","networking"]:
        if not name or not domain:
            st.warning("Please fill at least Name and Domain.")
            st.stop()

    elif category in ["presentation"]:
        if not project_title :
            st.warning("Please fill at least Project Name.")
            st.stop()
    
    else:  # Business
        if not business_name or not domain or not product_name or not solution:
            st.warning("Please fill all required business fields.")
            st.stop()

    # -----------------------------
    # Build Data Dictionary
    # -----------------------------
    if category in ["internship", "job", "project"]:
        data = {
            "name": clean_input(name),
            "domain": clean_input(domain),
            "skills": clean_input(skills),
            "project_name": clean_input(project_name),
            "beneficiary": clean_input(beneficiary),
            "problem": clean_input(problem),
            "years": clean_input(years),
            "job_role": clean_input(job_role),
            "current_status": clean_input(current_status),
            "internship_type": clean_input(internship_type)
        }
    elif category == "freelancer":
        data = {
            "name": clean_input(name),
            "domain": clean_input(domain),
            "services": clean_input(services),
            "project_name": clean_input(project_name),
            "beneficiary": clean_input(beneficiary),
            "problem": clean_input(problem)
        }

    elif category == "networking":
        data = {
            "name": clean_input(name),
            "domain": clean_input(domain),
            "interests": clean_input(interests),
            "current_focus": clean_input(current_focus),
            "achievement": clean_input(achievement)
        }

    elif category == "presentation":
        data = {
            "name": clean_input(name),
            "project_title": clean_input(project_title),
            "current_status": clean_input(current_status),
            "problem_statement": clean_input(problem_statement),
            "solution": clean_input(solution),
            "impact": clean_input(impact),
            "audience": clean_input(audience)
        }

    else:  # Business
        data = {
            "business_name": clean_input(business_name),
            "domain": clean_input(domain),
            "target_audience": clean_input(target_audience),
            "problem": clean_input(problem),
            "product_name": clean_input(product_name),
            "solution": clean_input(solution)
        }

    # -----------------------------
    # Generate Pitch
    # -----------------------------
    with st.spinner("Generating your pitch... Please wait"):
        pitch = generate_pitch(category, data)
        pitch = sanitize_pitch(pitch)

    # -----------------------------
    # AI Enhancement
    # -----------------------------
        if enhance:
            try:
                pitch = enhance_pitch_with_ai(pitch)
            except Exception:
                st.error("AI enhancement failed. Please check API configuration.")
        
        st.session_state.generated_pitch = pitch


# -----------------------------
# Output Card
# -----------------------------
if st.session_state.generated_pitch:
    st.markdown("### Your Generated Pitch")
    st.markdown(f"""
    <div style="
    background-color:#1e293b;
    padding:20px;
    border-radius:15px;
    color:white;
    font-size:16px;
    ">
    {st.session_state.generated_pitch}
    </div>
    """, unsafe_allow_html=True)


    # -----------------------------
    # Download as txt
    # -----------------------------
    st.download_button(
        label="📥 Download Pitch as TXT",
        data=st.session_state.generated_pitch,
        file_name="my_pitch.txt",
        mime="text/plain"
    )


    # -----------------------------
    # Review
    # -----------------------------
    st.markdown("### Rate This Pitch")
    rating = st.radio(
        "Select Rating:",
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: "⭐" * x,
        horizontal=True
    )


    if st.button("Submit Review"):
        save_review(
            st.session_state.generated_pitch,
            rating,
            enhance
        )
        st.success("Thank you for your feedback!")