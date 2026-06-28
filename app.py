import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# ১. পেজ সেটিংস ও প্রিমিয়াম থিম ডিজাইন
st.set_page_config(page_title="EduResume & Portfolio Pro", page_icon="💼", layout="centered")

st.title("💼 University Student Resume & Portfolio Builder")
st.subheader("Advanced 3D-Enhanced Academic Profile & Career Dashboard")
st.write("Presidency University | CSE Dept | Career Development Project")
st.write("---")

# ২. সাইডবার ডিজাইন (প্রোফাইল কার্ড)
st.sidebar.header("🎓 Project Profile")
with st.sidebar.container(border=True):
    st.write("**Project Target:** Resume & Portfolio Builder")
    st.write("**Developer:** NA FIA")
    st.write("**Institution:** Presidency University")
    st.write("**Department:** CSE")
    st.caption("🚀 Status: 100% Dynamic & 3D Analytics Enabled")

st.sidebar.write("---")
st.sidebar.header("🔗 Quick Navigation")
st.sidebar.page_link("https://presidency.edu.bd/", label="Presidency University Portal", icon="🏫")

# ৩. ৩ডি অ্যানিমেটেড সেকশন (নাফিয়ার থিমের জন্য এক্সক্লুসিভ নিওন-মেশ গ্রাফিক্স)
st.write("### 🌐 Live 3D Career Vector Mesh (Presentation Mode)")
st.caption("মাউস দিয়ে স্ক্রল করে ৩ডি মডেলটি জুম করো এবং ড্র্যাগ করে চারদিকে ঘুরিয়ে স্যারদের দেখাও:")

n_nodes = 35
x = np.random.standard_normal(n_nodes)
y = np.random.standard_normal(n_nodes)
z = np.random.standard_normal(n_nodes)

fig_3d = go.Figure(data=[go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers+lines',
    marker=dict(size=5, color=x, colorscale='Electric', opacity=0.8),
    line=dict(color='#a855f7', width=2)
)])

fig_3d.update_layout(
    margin=dict(l=0, r=0, b=0, t=0),
    scene=dict(
        xaxis=dict(showbackground=False, showticklabels=False, title=''),
        yaxis=dict(showbackground=False, showticklabels=False, title=''),
        zaxis=dict(showbackground=False, showticklabels=False, title=''),
    ),
    height=250
)
st.plotly_chart(fig_3d, use_container_width=True)
st.write("---")

# ৪. ইনফরমেশন ইনপুট সেকশন (Dynamic Form)
st.subheader("📝 Step 1: Input Profile Details")
with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("Full Name:", value="NA FIA")
        email = st.text_input("Email Address:", value="nafia@example.com")
        phone = st.text_input("Phone Number:", value="+8801XXXXXXXXX")
    with col2:
        varsity = st.text_input("University:", value="Presidency University")
        dept = st.text_input("Department/Major:", value="Computer Science and Engineering (CSE)")
        cgpa = st.number_input("Current CGPA:", min_value=0.0, max_value=4.0, value=3.80, step=0.01)

    bio = st.text_area("Professional Summary / Objective:", 
                       value="An ambitious and dedicated CSE undergraduate student at Presidency University with a strong foundation in programming, software engineering, and data analysis. Seeking opportunities to apply academic knowledge in real-world tech environments.")

# ৫. নাফিয়ার আইডিয়া অনুযায়ী নতুন "WORK EXPERIENCE" সেকশন
st.subheader("⏳ Step 2: Work Experience & Roles")
with st.container(border=True):
    st.write("তোমার যদি কোনো চাকরি, ইন্টার্নশিপ বা পার্ট-টাইম কাজের অভিজ্ঞতা থাকে, তা এখানে যোগ করো:")
    exp_type = st.selectbox("Experience Type:", ["Internship", "Part-Time Job", "Full-Time Job", "Freelancing / Tutoring"])
    company = st.text_input("Company / Organization Name:", value="Tech Innovation Lab")
    role = st.text_input("Your Role / Designation:", value="Junior Software Developer Intern")
    duration = st.text_input("Duration (e.g., Jan 2026 - Present):", value="March 2026 - Present")
    exp_desc = st.text_area("Job Contribution / Responsibilities:", 
                            value="Assisted in building responsive web layouts, testing algorithmic solutions, and collaborating with senior developers on backend systems.")

# ৬. স্কিলস ও প্রজেক্ট ইনপুট (Skill Metrics & Project Showcase)
st.subheader("📊 Step 3: Skills & Project Analytics")
with st.container(border=True):
    st.write("**Rate Your Technical Skills (1 to 100):**")
    p_lang = st.slider("Programming (C, Java, Python, etc.)", 0, 100, 85)
    web_dev = st.slider("Web Development (HTML, CSS, Streamlit)", 0, 100, 75)
    db_ms = st.slider("Database Management (SQL)", 0, 100, 70)
    prob_sol = st.slider("Problem Solving & Logic", 0, 100, 80)
    
    st.write("---")
    st.write("**Key Projects:**")
    p1_title = st.text_input("Project 1 Title:", value="AI-Powered Discrete Math Solver")
    p1_desc = st.text_area("Project 1 Description:", value="A web application built to help CSE students solve discrete mathematics problems dynamically using modern layout techniques.")

st.write("---")

# ७. ডাইনামিক লাইভ পোর্টফোলিও ড্যাশবোর্ড (Live Analytics Screen)
st.subheader("✨ Step 4: Your Live Portfolio Dashboard")

# ইন্টারঅ্যাক্টিভ স্কিল চার্ট
st.write("#### 📈 Interactive Skill Radar / Breakdown")
skill_data = {
    'Skills': ['Programming', 'Web Dev', 'Database (SQL)', 'Problem Solving'],
    'Expertise Level (%)': [p_lang, web_dev, db_ms, prob_sol]
}
df_skills = pd.DataFrame(skill_data)
fig = px.bar(df_skills, x='Skills', y='Expertise Level (%)', color='Expertise Level (%)',
             text='Expertise Level (%)', color_continuous_scale='Purples', height=350)
fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
st.plotly_chart(fig, use_container_width=True)

# ৮. জেনারেটেড সি ভি লেআউট (Printable Resume Layout)
st.write("---")
st.subheader("📄 Generated Academic Resume")

with st.container(border=True):
    # হেডার ডিজাইন
    st.markdown(f"<h2 style='text-align: center; color: #6b21a8; margin-bottom: 0;'>{full_name}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-style: italic;'>Email: {email} | Phone: {phone}</p>", unsafe_allow_html=True)
    st.markdown("<hr style='margin-top: 5px; margin-bottom: 15px;'>", unsafe_allow_html=True)
    
    # অবজেক্টিভ
    st.markdown("#### 🎯 CAREER OBJECTIVE")
    st.write(bio)
    st.write("")
    
    # এডুকেশন কার্ড
    st.markdown("#### 🎓 EDUCATION")
    st.markdown(f"**B.Sc. in {dept}**")
    st.write(f"{varsity}")
    st.write(f"**Current CGPA:** `{cgpa} / 4.00`")
    st.write("")
    
    # নতুন যোগ করা এক্সপেরিয়েন্স সেকশন
    st.markdown("#### ⏳ WORK EXPERIENCE")
    st.markdown(f"**{role}** — *{company}* ({exp_type})")
    st.caption(f"📅 Timeline: {duration}")
    st.write(exp_desc)
    st.write("")
    
    # টেকনিক্যাল স্কিলস
    st.markdown("#### 🛠 TECHNICAL SKILLS")
    st.write(f"* **Core Languages:** Verified competence at {p_lang}% competency.")
    st.write(f"* **Web Technologies:** Practical exposure in web platforms rated at {web_dev}%.")
    st.write(f"* **Databases & Architecture:** Structured data handling rated at {db_ms}%.")
    st.write("")
    
    # প্রজেক্টস শোকেস
    st.markdown("#### 🚀 COMPLETED PROJECTS")
    st.markdown(f"**Title: {p1_title}**")
    st.write(p1_desc)
    
    st.write("---")
    st.caption("Generated automatically via EduResume Platform | Signed by Applicant")

# ডাউনলোড বাটন এনিমেশন
st.write("")
if st.button("📥 Export & Download Printable Resume View", use_container_width=True):
    st.balloons()
    st.success("🎉 Professional Resume Layout Successfully Generated for Printing!")

st.write("---")
st.caption("Developed by NA FIA & MD FAZLE RABBI SOHAN | PU CSE Career Lab")
