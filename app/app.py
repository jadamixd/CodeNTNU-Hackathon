from flask import Flask, render_template, request
import base64
import sys

app = Flask(__name__)

# Add the root directory to sys.path
sys.path.append('/main')

# Now you can import main
from main import main 

app = Flask(__name__)

@app.route('/save-image', methods=['POST'])
def save_image():
    try:
        data = request.get_json()
        image_data = data['image']
        # Decode the base64 image data
        image_binary = base64.b64decode(image_data.split(',')[1])

        # Define the directory to save the images
        image_directory = 'app/static/'
        
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
    list = main()
    print(list)
    return render_template('information.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
