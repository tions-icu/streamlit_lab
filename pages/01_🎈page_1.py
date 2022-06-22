import streamlit as st
from time import sleep

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

if st.button("Press me for balloons🎈🎈🎈"):
    st.balloons()

if st.button("Press me for balloons and snowflakes"):
    st.snow()
    sleep(2)
    st.balloons()