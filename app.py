from flask import Flask, render_template, request
from PIL import Image
import base64

app = Flask(__name__)
from main import main
import persistence.access as access 

@app.route('/save-image', methods=['POST'])
def save_image():
    try:
        data = request.get_json()
        image_data = data['image']
        # Decode the base64 image data
        image_binary = base64.b64decode(image_data.split(',')[1])

        # Define the directory to save the images
        image_directory = 'static/'
        image_path = r'static/reciept.jpg'
        
        # Save the image to a file in the specified directory
        with open(image_directory + 'reciept.jpg', 'wb') as f:
            f.write(image_binary)
        
        image = Image.open(image_path).transpose(Image.ROTATE_270).save(image_path)
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

@app.route('/db-save-and-redirect', methods=['POST'])
def save_and_redirect():
    # Add your Python code to run the script here
    items = request.form['data']
    conn = access.connect_to_database("persistence/data.db")
    access.add_receipt(conn, "Example shop", 1)
    
    for item in items:
        access.add_item(conn, item, None, 1, 0)
    
    # You can perform any necessary operations
    # For example, print some data or perform some processing

    # After running the script, redirect to the index page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
