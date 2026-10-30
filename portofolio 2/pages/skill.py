import streamlit as st

st.title("🚀 My skills")
st.write("Beberapa karya dan eksperimen digital.")

skills = [
    ("Personal Website", "Python · Streamlit",
     "https://images.unsplash.com/photo-1467232004584-a241de8bcf5d?w=600"),
    ("Akuntansi dan pencatatan keuangan", "Excel · Python · Pandas",
     "https://cdngnfi2.sgp1.digitaloceanspaces.com/gnfi/uploads/articles/large-tahukah-kamu-ini-8-fakta-menarik-tentang-akuntansi-1VWDVWx2sQ.jpeg?w=600"),
    ("Microsoft Office dan pengolahan data", "Word · Excel · PowerPoint",
     "https://www.mobilissimo.ro/photos/1600x900-crop/440119/danemarca-microsoft-office-collabora-cover-a97852-001.webp?upscale=1&format=webp?w=600")
]

cols = st.columns(3)
for col, (name, tech, image) in zip(cols, skills):
    with col:
        with st.container(border=True):
            st.image(image, use_container_width=True)
            st.subheader(name)
            st.caption(tech)
            st.write("Eksperimen membangun solusi digital.")

st.divider()
if st.button("✉️ Contact Me", type="primary"):
    st.switch_page("pages/contact.py")