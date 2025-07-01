import os
import shutil
import sys
import cv2

class FrameCapture:
    '''
    Class to capture frames from a video file using OpenCV.
    '''
    def __init__(self, file_path):
        '''
        Initialize the directory for storing captured frames.
        Deletes the directory if it already exists.
        '''
        self.directory = "captured_frames"
        self.file_path = file_path

        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        os.mkdir(self.directory)

    def capture_frames(self):
        '''
        Capture and save frames from the video file.
        '''
        cv2_object = cv2.VideoCapture(self.file_path)

        if not cv2_object.isOpened():
            print(f"Error: Cannot open video file: {self.file_path}")
            return

        frame_number = 0

        while True:
            frame_found, image = cv2_object.read()

            if not frame_found:
                break

            capture_path = os.path.join(self.directory, f'frame{frame_number}.jpg')
            cv2.imwrite(capture_path, image)
            frame_number += 1

        print(f"{frame_number} frames captured and saved to '{self.directory}' directory.")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python capture_video_frames.py <video_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    fc = FrameCapture(file_path)
    fc.capture_frames()
