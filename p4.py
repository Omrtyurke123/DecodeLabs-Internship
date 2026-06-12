import cv2
import pytesseract

image = cv2.imread("/content/i2.png")

gray = cv2.cvtColor(image,
                    cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray,(5,5),0)

thresh = cv2.threshold(
    blur,
    0,
    255,
    cv2.THRESH_BINARY +
    cv2.THRESH_OTSU
)[1]

text = pytesseract.image_to_string(
    thresh
)

print(text)