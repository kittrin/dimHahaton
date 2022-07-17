from faceRecognition import faceRecognitionFromPhoto
from identifier import identifier
from faceRecognition import faceRecognitionFromPhoto

import numpy as np
import qrtools

import time

import requests

import cv2
import base64
import json

with open('../data/face_enc.json', 'r') as jsonFile:
    data = json.load(jsonFile)


# with open('face_enc.json', 'r') as jsonFile:
#     data = json.load(jsonFile)
def processImage(frame:str):
    frame = base64.b64decode(frame)
    np_data = np.fromstring(frame, np.uint8)
    frame = cv2.imdecode(np_data, cv2.IMREAD_UNCHANGED)
    qrcode = frame
    detector = cv2.QRCodeDetector()
    qrData, bbox, straight_qrcode = detector.detectAndDecode(qrcode)
    if(qrData):
        x = requests.get(
            'https://hakatonkrasnodar.pythonanywhere.com/verify_qr?qr='+qrData)
        print(x.text)


    face = faceRecognitionFromPhoto(frame)
    if(len(face[1])>0):
        photo = identifier(face[1], data, face[2])
        print(type(photo))
        if type(photo) is np.ndarray:
            photo = cv2.imencode('.jpeg', photo)[1].tostring()
            encoded_string = base64.b64encode(photo)
            return(encoded_string)
        else:
            photo = cv2.imencode('.jpeg', face[0])[1].tostring()
            print(2)
            encoded_string = base64.b64encode(photo)
        return(encoded_string)

    else:
        photo = cv2.imencode('.jpeg', face[0])[1].tostring()
        print(2)
        encoded_string = base64.b64encode(photo)
        return(encoded_string)

def processImageFromPhoto(frame):
    # print(frame)
    qrcode = frame
    detector = cv2.QRCodeDetector()
    qrData, bbox, straight_qrcode = detector.detectAndDecode(qrcode)
    if(qrData):
        x = requests.get(
            'https://hakatonkrasnodar.pythonanywhere.com/verify_qr?qr='+qrData)
        print(x.text)


    face = faceRecognitionFromPhoto(frame)
    if(len(face[1])>0):
        photo = identifier(face[1], data, face[2])
        out = photo
        # print(type(photo))
        if type(photo) is np.ndarray:
            # photo = cv2.imencode('.jpeg', photo)[1].tostring()
            # encoded_string = base64.b64encode(photo)
            return out
            return(encoded_string)
        else:
            # photo = cv2.imencode('.jpeg', face[0])[1].tostring()
            # print(2)
            out = face[0]
            # encoded_string = base64.b64encode(photo)
        return out
        return(encoded_string)

    else:
        # photo = cv2.imencode('.jpeg', face[0])[1].tostring()
        # print(2)
        out = face[0]
        # encoded_string = base64.b64encode(photo)
        return out
        return(encoded_string)

def processImageForDoor(frame):
    # print(frame)
    qrcode = frame
    detector = cv2.QRCodeDetector()
    qrData, bbox, straight_qrcode = detector.detectAndDecode(qrcode)
    if(qrData):
        print(qrData)
        x = requests.get(
            'http://10.254.199.132:8080//verify_qr?qr='+qrData)
        text_resp = json.loads(x.text)
        print(text_resp['status'])
        if(text_resp['status'] == 'OK'):
            dict_data = {}
            with open ('timestamps.json', 'r') as dataj:
                # print(data.read())
                dr = dataj.read()
                if(dr):
                    dict_data = json.loads(dr)
            with open('timestamps.json', 'w') as data_w:
                dict_data['Вход по QR коду'] = time.time()
                dataw = json.dumps(dict_data)
                data_w.write(dataw)
    
    face = faceRecognitionFromPhoto(frame)
    if(len(face[1])>0):
        photo = identifier(face[1], data, face[2])
        out = photo
        # print(type(photo))
        if type(photo) is np.ndarray:
            # photo = cv2.imencode('.jpeg', photo)[1].tostring()
            # encoded_string = base64.b64encode(photo)
            return out
            return(encoded_string)
        else:
            # photo = cv2.imencode('.jpeg', face[0])[1].tostring()
            # print(2)
            out = face[0]
            # encoded_string = base64.b64encode(photo)
        return out
        return(encoded_string)

    else:
        # photo = cv2.imencode('.jpeg', face[0])[1].tostring()
        # print(2)
        out = face[0]
        # encoded_string = base64.b64encode(photo)
        return out
        return(encoded_string)



