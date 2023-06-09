
import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

img = cv.imread("2.PNG")

# code = decode(img)
# cap = cv.VideoCapture(0)

# print(code)
while True:
    # Success, frame = cap.read()

    for barcode in decode(img):
        print(barcode.data)
        myData = barcode.data.decode("utf-8")
        print(myData)

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1,1,2))
        cv.polylines(img, [pts], True, (0,255,255), 2)

        pts2 = barcode.rect

        cv.putText(img, myData, (pts2[0], pts2[1]), cv.FONT_HERSHEY_SIMPLEX,
                    0.6, (0,255,255), 2)

    cv.imshow("QR Reader", img)
    
    key = cv.waitKey(1)

    if key == ord("q"):
        # cap.release()
        cv.destroyAllWindows()
        break

# cap.release()
cv.destroyAllWindows()
