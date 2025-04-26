import streamlit as st
from streamlit_webrtc import webrtc_streamer

    # Example usage (you'll likely want to customize this)
def video_processor(frame):
        # Your video processing code here.  For example, you could draw a box around objects:
        # ...
    return frame

webrtc_streamer(
    key="webcam",
    video_processor_factory=video_processor
)
