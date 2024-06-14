# 导入所需要的包
import streamlit as st                          # 构建Web应用


# streamlit run app/app.py



# 设置页面配置，隐藏Streamlit菜单和页脚
st.set_page_config(
    page_title="Fish Identification System",
    page_icon=":fish:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)



# 显示应用的标题文字
st.header("鱼类识别系统")






