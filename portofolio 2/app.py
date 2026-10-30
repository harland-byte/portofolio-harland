import streamlit as st

# =========================================
# KONFIGURASI
# =========================================
st.set_page_config(
    page_title="HARLAN | Portfolio",
    page_icon="💻",
    layout="wide"
)


# =========================================
# DATA Keahlian
# =========================================
skills = [
    {
        "name": "Personal Website",
        "category": "WEB DEVELOPMENT",
        "tech": "Python · Streamlit",
        "image": "https://images.unsplash.com/photo-1467232004584-a241de8bcf5d?w=700",
        "description": "Website personal untuk menampilkan profil dan karya digital."
    },
    {
        "name": "Akuntansi dan pencatatan keuangan",
        "category": "ACCOUNTING ",
        "tech": "Excel · Python · Pandas",
        "image": "https://cdngnfi2.sgp1.digitaloceanspaces.com/gnfi/uploads/articles/large-tahukah-kamu-ini-8-fakta-menarik-tentang-akuntansi-1VWDVWx2sQ.jpeg?w=700",
        "description": "Pencatatan transaksi, perhitungan pemasukan dan pengeluaran, serta penyusunan laporan keuangan sederhana."
    },
    {
        "name": "Microsoft Office dan pengolahan data",
        "category": "OFFICE & DATA",
        "tech": "Word · Excel · PowerPoint",
        "image": "https://www.mobilissimo.ro/photos/1600x900-crop/440119/danemarca-microsoft-office-collabora-cover-a97852-001.webp?upscale=1&format=webp?w=700",
        "description": "Penggunaan aplikasi perkantoran untuk mengolah data, membuat tabel dan laporan, serta menyusun presentasi."
    }
]


# =========================================
# HALAMAN HOME
# =========================================
def home():
    st.caption("PERSONAL PORTFOLIO / 2026")

    left, right = st.columns(
        [1.3, 1],
        gap="large",
        vertical_alignment="center"
    )

    with left:
        st.caption("HELLO, I'M harlan 👋")
        st.title("Learning. Building. Growing.")

        st.write(
            "Saya memiliki latar belakang akuntansi dan pengalaman "
            "dalam operasional toko. Saat ini, saya sedang "
            "mengembangkan kemampuan di bidang pengolahan data, "
            "pemrograman Python, dan pengembangan aplikasi web."
        )

        st.write("Accounting · Data Analysis · Web Development")

        if st.button("Explore My Work ↗", type="primary"):
            st.switch_page(skills_page)

    with right:
        st.image(
            "images/LR.jpg",
            use_container_width=True
        )

    st.divider()

    st.caption("PORTFOLIO")
    st.header("Skills & Expertise")
    st.write("Beberapa karya dan eksplorasi teknologi saya.")

    cols = st.columns(3, gap="medium")

    for col, item in zip(cols, skills):
        with col:
            with st.container(border=True):
                st.image(
                    item["image"],
                    use_container_width=True
                )
                st.caption(item["category"])
                st.subheader(item["name"])
                st.write(item["description"])
                st.caption(item["tech"])

    if st.button("Explore My Skills →"):
        st.switch_page(skills_page)

    st.divider()

    
    # =====================================
    # SKILLS & EXPERTISE
    # =====================================
    

    st.divider()

    st.caption("WHAT I DO")
    st.title("Skills & Expertise")
    st.write(
        "Kemampuan teknis yang terus saya kembangkan "
        "dalam membangun solusi digital."
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("💻 Python Programming")
        st.caption("Python · Basic Programming")
        st.progress(25)
        st.caption("25%")

        st.write("")

        st.subheader("💻 Web Development")
        st.caption("Streamlit")
        st.progress(20)
        st.caption("20%")

    with col2:
        st.subheader("🗄️ Data Processing")
        st.caption("Microsoft Excel · Data Entry")
        st.progress(30)
        st.caption("30%")

        st.write("")

        st.subheader("📊 Accounting")
        st.caption("Basic Accounting · Bookkeeping")
        st.progress(25)
        st.caption("25%")

    st.divider()
    st.caption("Always Learning — Growing through every skills.")




# =========================================
# HALAMAN ABOUT
# =========================================
def about():
    st.caption("GET TO KNOW ME")
    st.title("About Me")

    left, right = st.columns([1, 1.5], gap="large")

    with left:
        st.image(
            "pages/iam.jpeg",
            use_container_width=True
        )

    with right:
        st.subheader("Hello, I'm harlan.")
        st.write(
            "Saya merupakan lulusan SMK jurusan Akuntansi "
            "dan saat ini sedang melanjutkan pendidikan "
            "di Universitas Terbuka pada program studi Akuntansi."
        )
        st.write(
            "Saya tertarik mempelajari teknologi digital, "
            "khususnya pemrograman Python dan pengembangan "
            "aplikasi menggunakan Streamlit. Saya senang "
            "mencoba hal baru dan mengembangkan kemampuan "
            "melalui latihan serta proyek sederhana."
        )
        st.write(
            "Melalui portofolio ini, saya ingin menunjukkan "
            "proses belajar, kemampuan yang sedang saya "
            "kembangkan, dan hasil karya yang saya buat."
        )

        st.subheader("My Focus")
        st.write(
            "- Python Programming\n"
            "- Web Development with Streamlit\n"
            "- Microsoft Excel & Data Processing\n"
            "- Accounting & Financial Administration"
        )


# =========================================
# HALAMAN skillsS
# =========================================
def skills_content():
    st.caption("MY WORK")
    st.title("skills")
    st.write("Kumpulan skills, eksperimen, dan karya digital.")

    for start in range(0, len(skills), 2):
        cols = st.columns(2, gap="large")

        for col, item in zip(cols, skills[start:start + 2]):
            with col:
                with st.container(border=True):
                    st.image(
                        item["image"],
                        use_container_width=True
                    )
                    st.caption(item["category"])
                    st.subheader(item["name"])
                    st.write(item["description"])
                    st.caption(item["tech"])


# =========================================
# HALAMAN CONTACT
# =========================================

def contact():
    st.markdown("## Let's Connect")
    st.write(
        "Tertarik untuk berdiskusi atau bekerja sama? "
        "Silakan hubungi saya melalui email atau Instagram."
    )

    email = "harlandramadan"
    instagram = "rlndd_n"

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("### 📧 Email")
        st.write(email)
        st.link_button(
            "Kirim Email",
            f"mailto:{email}",
            use_container_width=True
        )

    with col2:
        st.markdown("### 📸 Instagram")
        st.write(f"@{instagram}")
        st.link_button(
            "Kunjungi Instagram",
            f"https://www.instagram.com/rlndd_n?obrf=NnU4cXY1NHdyeTc2/{instagram}/",
            use_container_width=True
        )


# =========================================
# DAFTAR HALAMAN
# =========================================
home_page = st.Page(home, title="Home", default=True)
about_page = st.Page(about, title="About")
skills_page = st.Page(skills_content, title="skills")
contact_page = st.Page(contact, title="Contact")

page = st.navigation(
    [home_page, about_page, skills_page, contact_page],
    position="hidden"
)


# =========================================
# HEADER WEBSITE / PALING DEPAN
# =========================================
logo, menu, action = st.columns(
    [1.2, 3.5, 1.2],
    vertical_alignment="center"
)

with logo:
    st.subheader("◈ HARLAN")
    st.caption("DIGITAL PORTFOLIO")

with menu:
    home_col, about_col, skills_col, contact_col = st.columns(4)

    with home_col:
        if st.button("⌂ Home", key="nav_home", use_container_width=True):
            st.switch_page(home_page)

    with about_col:
        if st.button("About", key="nav_about", use_container_width=True):
            st.switch_page(about_page)

    with skills_col:
        if st.button("▦ skills", key="nav_skills", use_container_width=True):
            st.switch_page(skills_page)

    with contact_col:
        if st.button("✉ Sosial Media", key="nav_contact", use_container_width=True):
            st.switch_page(contact_page)

with action:
    if st.button(
        "Let's Talk ↗",
        key="nav_talk",
        type="primary",
        use_container_width=True
    ):
        st.switch_page(contact_page)

st.divider()


# =========================================
# TAMPILKAN HALAMAN
# =========================================
page.run()