import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd="C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
img=cv2.imread('1.jpg')
img1=img.copy()
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img ))
#for image to Boxes
imx,imy,imc=img.shape
print(imx)
boundary=pytesseract.image_to_boxes(img )
for b in boundary.splitlines():
    b=b.split(' ')
    x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,imx-y),(w,imx-h),(255,0,0),1)
    cv2.putText(img,b[0],(x,imx-y-20),cv2.FONT_HERSHEY_DUPLEX,0.34,(0,0,0),1)
    cv2.imshow('IMAGE TO LETTERS', img)

#image to Data
boundary1=pytesseract.image_to_data(img1)
for c,b1 in enumerate(boundary1.splitlines()):
    if(c!=0):
        b1=b1.split()
        if len(b1)==12:
            x1,y1,w1,h1=int(b1[6]),int(b1[7]),int(b1[8]),int(b1[9])
            cv2.rectangle(img1,(x1,y1),(w1+x1,h1+y1),(255,0,0),1)
            cv2.putText(img1,b1[11],(x1,y1),cv2.FONT_HERSHEY_DUPLEX,0.34,(0,0,0),1)
            cv2.imshow('Image TO DATA', img1)
cv2.waitKey(0)

