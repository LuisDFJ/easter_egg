import numpy as np
import cv2
import msj
import os
import Carita_detection_v1


msj.msj1()

while(True):
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        cv2.imshow('Presiona espacio para tomar una foto',frame)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            break

    cap.release()
    cv2.destroyAllWindows()

    cv2.imshow('Presiona "q" para continuar u otra tecla para tomarte otra foto', frame)
    flag = cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()
    if flag == ord('q'):
        break

src_pics = 'pics/tucarita.jpg'

if os.path.exists(src_pics):
    os.remove(src_pics)
cv2.imwrite(src_pics,frame)

msj.msj2()

clases, score = Carita_detection_v1.img_det('training/labelmap.pbtxt',src_pics,'inference_graph')
if clases[0] == 1:
    msj.msj3()
    
else:
    print(f'''ACCESO DENEGADO''')
