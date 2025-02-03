from flask import Flask, render_template, request
from process_videos import process_videos  # Your existing video processing script

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    singer_name = request.form['singer_name']
    num_videos = int(request.form['num_videos'])
    duration = int(request.form['duration'])
    email = request.form['email']
    
    # Call your video processing function
    output_file = f"output_{singer_name}.mp3"
    process_videos(singer_name, num_videos, duration, output_file)
    
    return f"Processing complete! Results will be sent to {email}"

if __name__ == '__main__':
    app.run(debug=True)
