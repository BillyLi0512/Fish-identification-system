import streamlit as st

# 设置页面标题
st.title("简单的 Streamlit 应用")

# 添加文本
st.write("欢迎使用 Streamlit 应用！")

# 创建一个输入框
name = st.text_input("请输入你的名字：")

# 创建一个按钮
if st.button("提交"):
    # 当按钮被点击时，显示输入的名字
    st.write(f"你好，{name}！")

# 创建一个数字输入框
number = st.number_input("请输入一个数字：", min_value=0, max_value=100, value=50)

# 显示输入的数字
st.write(f"你输入的数字是：{number}")

# 显示一个下拉菜单
options = ["选项1", "选项2", "选项3"]
option = st.selectbox("请选择一个选项：", options)

# 显示选择的选项
st.write(f"你选择了：{option}")
