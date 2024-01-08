import streamlit as st
st.set_page_config(page_title='Mounts')
st.header("Highest Peak Mounts")
col1,col2,col3=st.columns(3)
with col1:
  st.subheader("Everest")
  st.image("./everest.jpg",caption="Mount Everest",width=300,use_column_width=True)
  st.write("Mount Everest, standing at 29,032 feet (8,848 meters), is the world's highest peak, located in the Himalayas on the border of Nepal and Tibet.")
with col1:
  st.subheader("K2")
  st.image("k2.jpg",caption="Mount K2",width=300,use_column_width=True)
  st.write("K2, the second-highest mountain at 28,251 feet (8,611 meters), is renowned for its formidable challenges and is part of the Karakoram Range on the China-Pakistan border.")