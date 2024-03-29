import streamlit as st
st.set_page_config(page_title='Mounts')
st.header("Highest Peak Mounts")
col1,col2=st.columns(2)
with col1:
  st.image("mount.gif",width=100,use_column_width=True)
with col2:
  st.write("Climb High...The mountains echo a silent call, an invitation to challenge your limits and embrace the untamed. Feel the pull of their majestic peaks, urging you to ascend and discover your inner strength. Hear the mountains whisper tales of resilience, echoing the triumph of those who dared to climb.")
with col1:
  st.subheader("Everest")
  st.image("everest.jpg",caption="Mount Everest",width=300,use_column_width=True)
  st.write("Mount Everest, standing at 29,032 feet (8,848 meters), is the world's highest peak, located in the Himalayas on the border of Nepal and Tibet.")
with col2:
  st.subheader("K2")
  st.image("k2.jpg",caption="Mount K2",width=300,use_column_width=True)
  st.write("K2, the second-highest mountain at 28,251 feet (8,611 meters), is renowned for its formidable challenges and is part of the Karakoram Range on the China-Pakistan border.")
