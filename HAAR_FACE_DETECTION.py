import cv2
import time
import os

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# specify the image path [ .jpg, .png, .jpeg]
path = PATH_OF_IMAGE

# function to detect faces
def DetectFace(data_path):
    # initialize face count to 0
    face_count = 0
    
    # read the image file
    data = cv2.imread(data_path)
    # Convert to grayscale
    gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
       cv2.rectangle(data, (x, y), (x+w, y+h), (255, 0, 0), 2)
       # count number of faces
       face_count = face_count + 1

    if len(faces)>0:
        print("{} Face Detected".format(face_count))
    else:
        print("No Face Detected!!")
    cv2.imwrite('haar_result_img.jpg',data)
start = time.time()
DetectFace(path)
end = time.time()
print("Execution time in seconds {}".format(end-start))
