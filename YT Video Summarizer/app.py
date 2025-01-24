import streamlit as st
from utils import summarize_youtube_video



st.title('YouTube Summarizer')
video_url = st.text_input('Enter YouTube Video URL')

if video_url:
    summary = summarize_youtube_video(video_url)
    st.subheader("Summary:")
    st.write(summary)
