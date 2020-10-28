import cv2

camera = cv2.VideoCapture(0)
while True:
    return_value, image = camera.read()
    cv2.imshow('cam', image)
    cv2.waitKey(20)
del(camera)
