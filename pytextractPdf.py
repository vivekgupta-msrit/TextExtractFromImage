import io
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = '.\Tesseract-OCR\Tesseract.exe'
from wand.image import Image as wi

pdfImg = wi(filename = "images.png", resolution = 300 )

imgBlobs = []

for img in pdfImg.sequence:
	page = wi(image = img)
	imgBlobs.append(page.make_blob('jpeg'))

extracted_text = []

for imgBlob in imgBlobs:
	im = Image.open(io.BytesIO(imgBlob))
	text = pytesseract.image_to_string(im, lang = 'eng')
	extracted_text.append(text)

print(extracted_text[0])

file = open("Extract.txt", "a")
file.write(text) 
file.write("\n") 
file.close 
