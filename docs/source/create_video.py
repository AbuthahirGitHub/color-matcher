import cv2
import os

def create_video(cframe_input_folder, coutput_video_path, fps=30):
    frames = [f for f in os.listdir(cframe_input_folder) if f.endswith('-c.png')]
    frames.sort(key=lambda x: int(x.split('-')[0]))

    if not frames:
        raise ValueError("No frames found for creating video.")

    first_frame_path = os.path.join(cframe_input_folder, frames[0])
    frame = cv2.imread(first_frame_path)
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(coutput_video_path, fourcc, fps, (width, height))

    for frame_name in frames:
        frame_path = os.path.join(cframe_input_folder, frame_name)
        frame = cv2.imread(frame_path)
        video.write(frame)

    video.release()

if __name__ == "__main__":
    cframe_input_folder = "/content/color-matcher/MyFolder/ColorMatchFrame"
    coutput_video_path = "/content/color-matcher/MyFolder"

    create_video(cframe_input_folder, coutput_video_path)
