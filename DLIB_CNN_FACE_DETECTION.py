import dlib
import os
import time
import cv2

weights = 'mmod_human_face_detector.dat'
cnn_face_detector = dlib.cnn_face_detection_model_v1(weights)
face_count = 0

# specify the image path [ .jpg, .png, .jpeg]
path = PATH_OF_IMAGE

# function to detect faces
def DetectFace(data_path):
    # read the image file
    img = cv2.imread(data_path)
    # apply face detection (cnn)
    faces_cnn = cnn_face_detector(img, 1)
    imgframe = img
    # loop over detected faces
    for face in faces_cnn:
        x = face.rect.left()
        y = face.rect.top()
        w = face.rect.right() - x
        h = face.rect.bottom() - y
        # draw box over face
        cv2.rectangle(imgframe, (x,y), (x+w,y+h), (0,0,255), 2)
        # count the number of face detected
        face_count = face_count+1

    if len(result_list)>0:
        print("{} Face Detected".format(face_count))
    else:
        print("No Face Detected!!")
    cv2.imwrite('dlib_frontal_face_result_img.jpg'.format(count),imgframe)
start = time.time()
DetectFace(path)
end = time.time()
print("Execution time in seconds {}".format(end-start))
