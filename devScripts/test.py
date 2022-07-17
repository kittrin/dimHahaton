from faceRecognition import faceRecognition
from identifier import identifier
from processImage import processImageForDoor
import time
import cv2
import json

cap = cv2.VideoCapture('http://10.254.199.147:8080/video')
# cap = cv2.VideoCapture('video.MOV')
# out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (720,1280))

while True:
    suc, img = cap.read()
    # print(time.time())
    # if suc ==True:
    print(type(img))
    processImageForDoor(img)
    # print(type(img))
    # print(type(outi))
    # cv2.imshow('1',outi)
    # out.write(outi)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    with open('timestamps.json', 'r') as db:
        db_data = db.read()
        if(db_data):
            # print(db_data)
            data = json.loads(db_data)
            if(len(data.keys())>0):
                for i in list(data.keys()):
                    db_timestamp = data[i]
                    if(time.time() - db_timestamp >5):
                        # print(time.time() - db_timestamp >5)
                        del data[i]
                        # print(data, '2')
                        with open('timestamps.json', 'w') as db_w:
                            dataw = json.dumps(data)
                            print(f'deleted: {i}')
                            db_w.write(dataw)

            # print(data.keys())
    
    # cv2.waitKey(0)
    # cap.release()
    # out.release()
        

