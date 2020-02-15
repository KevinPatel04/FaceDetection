import dlib
import os
import time
import cv2

face_detector = dlib.get_frontal_face_detector()

# specify the image path [ .jpg, .png, .jpeg]
path = PATH_OF_IMAGE

# function to detect faces
def DetectFace(data_path):
    # initialize face count to 0
    face_count = 0
    
    # read the image file
    img = cv2.imread(data_path)
    faces = face_detector(img, 1)
    for face in faces:
        x = face.left()
        y = face.top()
        w = face.right() - x
        h = face.bottom() - y
        # draw box over face
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
        # count the number of face detected
        face_count = face_count+1

    if len(faces)>0:
        print("{} Face Detected".format(face_count))
    else:
        print("No Face Detected!!")
    cv2.imwrite('dlib_frontal_face_detector_result.jpg',img)
start = time.time()
DetectFace(path)
end = time.time()
print("Execution time in seconds {}".format(end-start))
