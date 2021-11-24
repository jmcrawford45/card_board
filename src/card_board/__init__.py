import cv2
import pytesseract

def card_from_image(path: str) -> str:
	custom_config = r'--oem 3 --psm 6'
	return pytesseract.image_to_string(path, config=custom_config)

all = ('card_from_image')