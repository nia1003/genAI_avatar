# 📂 app.py（Streamlit）
# 網頁展示：影片 + 左右圖 + WebGL Viewer iframe
# ============================
import streamlit as st
st.set_page_config(layout="wide")

st.title("AI Avatar: manchild - Elon Musk")
st.video("out_elon_manchild/final.mp4")

st.markdown("拖曳下方視差圖模擬裸眼3D")
st.image(["left.png", "right.png"], width=400)

# WebGL Viewer
st.markdown("""
<iframe src="3dviewer/index.html" width="100%" height="600px" frameborder="0"></iframe>
""", unsafe_allow_html=True)