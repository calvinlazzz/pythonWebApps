from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/', methods=['POST'])
def home_post():
    length = request.form['length']
    width = request.form['width']
    height = request.form['height']
    volume = float(length) * float(width) * float(height)
    print(volume)
    
    print('get Post Request')
    return render_template('index.html', output = volume, length1 = length, width1 = width, height1 = height)

app.run(port=5000)