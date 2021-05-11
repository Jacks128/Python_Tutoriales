from flask import Flask, render_template,  request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(filename))
        return 'file uploaded successfully'

app.run(debug=True)