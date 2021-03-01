import argparse
from webcam_utils import get_current_emotion,run_realtime_emotions
from prediction_utils import prediction_path
import sys

# for running emotion detection
def read_emotion(path):
    get_current_emotion(path)

# to run emotion detection on image saved on disk
def run_detection_path(path_img,path_res):
    prediction_path(path_img,path_res)

if __name__ == '__main__':

    # try:
    #     os.listdir()
    #     os.listdir("volume")
    run_detection_path(sys.argv[1],sys.argv[2])
    # except:
    #     print("python app.py [src] [dest]\n[src]: le path vers l'image\n[dest]: le path vers le fihcier texte du résultat")

    # run_detection_path("C:/xampp/htdocs/FDS/S6/HLIN601/TER_S6/_data/face.jpg","C:/xampp/htdocs/FDS/S6/HLIN601/TER_S6/_data/emotion.txt")
