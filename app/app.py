from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Call a function from the database_checker script to check the credentials
    is_valid = True
    
    if is_valid:
        # Redirect to a success page
        return "Login successful"
    else:
        # Redirect to a failure page or show an error message
        return "Login failed"

if __name__ == '__main__':
    app.run(debug=True)