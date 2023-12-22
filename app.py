import streamlit as st



page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://th.bing.com/th/id/OIP.kigSNmXmyFgWJFarjN5ZtwHaEl?rs=1&pid=ImgDetMain");
background-size: cover;

background-color: #f0f0f0;
}


"""

st.markdown(page_bg_img, unsafe_allow_html=True)


from p_page import show_page

show_page()