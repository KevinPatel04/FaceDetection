from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from mtcnn.mtcnn import MTCNN
import cv2
import time
import os

face_count = 0

# specify the image path [ .jpg, .png, .jpeg]
path = PATH_OF_IMAGE

# function to detect faces
def DetectFace(data_path):
    # read the image file
    data = cv2.imread(data_path)

    # initialize MTCNN detector
    detector = MTCNN()
    # detect faces in the image
    result_list = detector.detect_faces(data)
    # draw box arround faces on original image file
    for i in range(len(result_list)):
        # get coordinates
        x1, y1, width, height = result_list[i]['box']
        x2, y2 = x1 + width, y1 + height
        # draw the box arround the face
        cv2.rectangle(imgframe, (x1, y1), (x2, y2), (255, 0, 0), 2)
        # count the number of face detected
        face_count = face_count+1

    if len(result_list)>0:
        print("{} Face Detected".format(face_count))
    else:
        print("No Face Detected!!")
    cv2.imwrite('mtcnn_result_img.jpg'.format(count),imgframe)
    start = time.time()
    DetectFace(path)
    end = time.time()
    print("Execution time in seconds {}".format(end-start))
