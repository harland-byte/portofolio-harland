import streamlit as st

st.title("👋 About Me")
kiri, kanan = st.columns([1, 2])

with kiri:
    st.image("pages/iam.jpeg", use_container_width=True)

with kanan:
    st.header("Hi, I'm harlan!")
    st.write("Saya tertarik pada web development, data, dan AI.")
    st.subheader("My Skills")
    for skill, value in [
        ("Python", 85), ("Web Development", 75), ("AI", 60)
    ]:
        st.write(skill)
        st.progress(value)

st.info("Learn • Build • Improve")
