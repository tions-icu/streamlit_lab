import streamlit as st
from time import sleep

st.markdown("# Main page π")
st.sidebar.markdown("# Main page π")

if st.button("Press me for balloonsπππ"):
    st.balloons()

if st.button("Press me for balloons and snowflakes"):
    st.snow()
    sleep(2)
    st.balloons()