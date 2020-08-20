import cv2
import sys
import pytesseract
 
if __name__ == '__main__':
 
  if len(sys.argv) < 3:
    print('Usage: python ocr_simple.py image.jpg')
    sys.exit(1)
   
  # Read image path from command line
  imPath = sys.argv[1]
  name = sys.argv[2]

  name = str(name).lower() 
  config = ('-l eng --oem 1 --psm 3')
 
  im = cv2.imread(imPath, cv2.IMREAD_COLOR)
 
  text = pytesseract.image_to_string(im, config=config)

  if name in text.lower():
    print("Verified")
  else:
    print("Not Verified")