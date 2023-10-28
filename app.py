from flask import Flask, render_template, request
import base64

app = Flask(__name__)
from main import main

@app.route('/save-image', methods=['POST'])
def save_image():
    try:
        data = request.get_json()
        image_data = data['image']
        # Decode the base64 image data
        image_binary = base64.b64decode(image_data.split(',')[1])

        # Define the directory to save the images
        image_directory = 'static/'
        
        # Save the image to a file in the specified directory
        with open(image_directory + 'reciept.jpg', 'wb') as f:
            f.write(image_binary)
        
        return 'Image saved successfully', 200
    
    except Exception as e:
        return 'Failed to save the image: ' + str(e), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/information')
def information():
    data = main()
    # data = ["ADS", "ADSJIDAS", "AHSDH", "AGSHD", "AOSIDPAS", "AOSPIJ"]
    return render_template('information.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
