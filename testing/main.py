import easyocr
reader = easyocr.Reader(['no']) # this needs to run only once to load the model into memory
image_path = r'static\reciept.jpg'
result = reader.readtext(image_path)
print(result)
