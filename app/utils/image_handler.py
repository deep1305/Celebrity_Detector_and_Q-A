import cv2
from io import BytesIO
import numpy as np

def process_image(image_data):
    in_memory_file = BytesIO() #When user has uploaded it will store our image sometimes in the form of cache file(for temporary time).
    image_data.save(in_memory_file)

    image_bytes = in_memory_file.getvalue()
    nparr = np.frombuffer(image_bytes, np.uint8)

    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5) #It is detecting all the faces in that particular image.

    if len(faces) == 0:
        return image_bytes, None

    largest_face = max(faces, key=lambda x: x[2] * x[3])   
    (x, y, w, h) = largest_face

    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    is_success, buffer = cv2.imencode('.jpg', img)
    return buffer.tobytes(), largest_face #we are returnong in the form of the bytes so that later we can convert them into a normal image.
