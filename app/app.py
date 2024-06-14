# 导入所需要的包
import streamlit as st                          # 构建Web应用


# streamlit run app/app.py

# 使用HTML和CSS隐藏上标和注脚
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



# 显示应用的标题文字
st.header("鱼类识别系统的系统")






