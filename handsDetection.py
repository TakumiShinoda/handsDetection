import cv2

cascade_path = "/Users/macuser/Documents/Python/openCV/handsDetection/xml/cascade.xml"
cascade = cv2.CascadeClassifier(cascade_path)
color = (255, 255, 255)
cap = cv2.VideoCapture(0)
minsize = 120

def display(frame):
    cv2.imshow("frame",frame)

while True:
    lastRect = []
    ret,frame = cap.read()
    image_gray = cv2.cvtColor(frame, cv2.cv.CV_BGR2GRAY)
    rect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=3, minSize=(minsize,minsize))

    for colorRect in rect:
        cx = colorRect[0] + (colorRect[2] / 2)
        cy = colorRect[1] + (colorRect[2] / 2)
        frameSmooth = cv2.medianBlur(frame,7);
        frameHSV = cv2.cvtColor(frameSmooth,cv2.cv.CV_BGR2HSV)
        ch = frameHSV[cy][cx][0]
        cs = frameHSV[cy][cx][1]
        cv = frameHSV[cy][cx][2]

        if ch >= 15 and cs >= 50 and cs <= 255 and cv >= 50 and cv <= 255:
            lastRect.append([colorRect[0],colorRect[1],colorRect[2],colorRect[3]])

    if len(lastRect) > 0:
        for handRect in lastRect:
            cv2.rectangle(frame, tuple((handRect[0],handRect[1])),tuple((handRect[0]+handRect[2],handRect[1]+handRect[2])), color, thickness=2)
    
    display(frame)
            
    cv2.waitKey(1)
