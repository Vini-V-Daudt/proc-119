import cv2
import time
import math
print("Versão do OpenCV:", cv2.__version__)
video = cv2.VideoCapture("bb3.mp4")
if not video.isOpened:
    print("erro")
    exit

tracker = cv2.legacy_TrackerCSRT_create()

returned, img = video.read()

bbox = cv2.selectROI("rastreando, img, FALSE")

tracker.init(img, bbox)

def drawBox(img, bbox):
 x,y,w,h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

 cv2.rectangle(img, (x+y),(x + w, y + h), (55, 8, 259), 3, 1)
 cv2.putText(img, 'Rastreando', (75, 90), cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 255, 0), 2)

# Funcio pars realizar o rastresmento do objetivo
def goal_track(ing, bbox):
 x,y,w,h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

# Loop principal
while True:
    check,img = video.read()   
    
    sucess, bbox= tracker.update(img)

    if sucess:
       drawBox(img, bbox)
    else:
       cv2.putText(img, 'perdido', (75, 90), cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 0,255), 2)
     
    cv2.imshow("resultado",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Interrompido!")
        break


video.release()
cv2.destroyAllwindows()



