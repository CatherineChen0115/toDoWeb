import streamlit as st

colWidth = 200

st.set_page_config(layout="wide") #setting the page display as wide as screen

st.write("<b>THis is about all drawing thing.</b>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["水彩", "電繪", "others"])

with tab2: 
    st.write("電繪-貼圖")
    col1, col2= st.columns(2)
    with col1:
        st.image("images/LINECreatorsMarket.png", width=colWidth)
    with col2:
        st.image("images/LINECreatorsMarket2.png", width=colWidth)
with tab1: 
    st.write("水彩")
    for i in range(1,3):
        col1, col2, col3 = st.columns(3) 
        try:
            for index in range(1,6,3):
                with col1:
                    st.image(f"images/img{i}{index}.jpg", width=colWidth)
                with col2:
                    st.image(f"images/img{i}{index+1}.jpg", width=colWidth)
                with col3:
                    st.image(f"images/img{i}{index+2}.jpg", width=colWidth)
        except:
            print("檔案不存在!")
