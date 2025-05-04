from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
RESUME_FOLDER = 'resume'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return 'No file part'
    file = request.files['resume']
    if file.filename == '':
        return 'No file selected'
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return 'Resume uploaded successfully!'

@app.route('/resume/<filename>')
def download_resume(filename):
    return send_from_directory(RESUME_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
