import cv2

cascade_path = "/Users/macuser/Documents/Python/openCV/handsDetection/xml/cascade.xml"
cascade = cv2.CascadeClassifier(cascade_path)
color = (255, 255, 255)
cap = cv2.VideoCapture(0)
minsize = 100

def display(frame):
    cv2.imshow("frame",frame)

while True:
    ret,frame = cap.read()
    image_gray = cv2.cvtColor(frame, cv2.cv.CV_BGR2GRAY)
    rect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(minsize,minsize))

    if len(rect) > 0:
        for handRect in rect:
            cv2.rectangle(frame, tuple((handRect[0],handRect[1])),tuple((handRect[0]+handRect[2],handRect[1]+handRect[2])), color, thickness=2)
    
    display(frame)
            
    cv2.waitKey(1)
