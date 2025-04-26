import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import av  # Used for frame handling

# Custom video processor class
class VideoProcessor(VideoProcessorBase):
    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        # Just return the original frame (you can process it here if needed)
        return frame

# Start the webcam stream
webrtc_streamer(
    key="webcam",
    video_processor_factory=VideoProcessor,
    media_stream_constraints={"video": True, "audio": False}
)
