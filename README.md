# CodeNTNU-Hackathon
Hackathon October 2023

Required libraries with correct versions. Will not work with newest version of numpy. 
```
 pip install -r requirements.txt 
```
<a href="https://tesseract-ocr.github.io/tessdoc/Installation.html" target="_blank">Tesseract downlaod</a>

For the full code to work '/camera/imagetext_extraction/' needs an OpenAI API key to run the code. We use the GPT4 model.

If you use mac you need to change the things listed below:
- update the tesseract_cmd file in path main.py to you tesseract installation path.
- you may have to change the relative filepaths for images in main.py and imagetext_extraction.py as Windows uses "\" in filepaths, while MAC uses "/".

Weigth_data map used for object detection training (Receipt detection with AOI (Area of Intereset)). Was not used in final due to lack of training. Options: Vertex.ai or Grayscaling and white contour as used in last update. 
