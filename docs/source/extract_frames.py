import cv2
import os

def extract_frames(source_video_path, frame_output_folder, video_id):
    cap = cv2.VideoCapture(source_video_path)
    frame_count = 1

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_name = f"{video_id}-{frame_count}.png"
        frame_path = os.path.join(frame_output_folder, frame_name)
        cv2.imwrite(frame_path, frame)
        frame_count += 1

    cap.release()

if __name__ == "__main__":
    video_folder = "/content/color-matcher/MyFolder/VideosWOCon"
    frame_output_folder = "/content/color-matcher/MyFolder/Frames"

    os.makedirs(frame_output_folder, exist_ok=True)

    videos = [f for f in os.listdir(video_folder) if f.endswith('.mp4')]

    for i, video in enumerate(videos, start=1):
        source_video_path = os.path.join(video_folder, video)
        extract_frames(source_video_path, frame_output_folder, i)
