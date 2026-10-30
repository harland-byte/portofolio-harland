
import streamlit as st

st.title("📬 Let's Connect")

st.write(
    "Punya ide atau ingin berkolaborasi? "
    "Hubungi saya melalui email atau Instagram."
)

st.divider()

# Ganti dengan informasi milikmu
email = "emailkamu@gmail.com"
instagram = "usernamekamu"

col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("📧 Email")
    st.write(email)

    st.link_button(
        "Kirim Email ↗",
        f"mailto:{email}",
        use_container_width=True
    )

with col2:
    st.subheader("📸 Instagram")
    st.write(f"@{instagram}")

    st.link_button(
        "Kunjungi Instagram ↗",
        f"https://www.instagram.com/{instagram}/",
        use_container_width=True
    )

st.divider()

st.caption("Terima kasih sudah mengunjungi portofolio saya.")
