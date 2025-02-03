# Mashup Generator

A Python tool to create audio mashups from YouTube videos, implementing requirements from [Assignment-Mashup.pdf](./Assignment-Mashup.pdf).

## Features

- CLI interface for audio processing
- Web interface using Flask
- Video downloading from YouTube
- Audio extraction and slicing
- Multi-file merging
- Email notifications

## Project Structure

```
├── process_videos.py # Core processing logic same content as 102203600.py
├── app.py # Flask web application
├── index.html # Web interface
├── Michael_Jackson_songs # Folder containing videos of Michael Jackson songs
├── 102203600.py # Run this file as python 102203600.py "<SingerName>" <NumberOfVideos> <AudioDuration> <OutputFileName>
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/KirtanDwivedi/Mashup-Generator.git
cd Mashup-Generator
```

2. Install necessary pip packages:

```bash
pip install moviepy pytube flask python-dotemail
```

## Usage

### Command Line Interface for 102203600.py file

```bash
python 102203600.py "<SingerName>" <NumberOfVideos> <AudioDuration> <OutputFileName>

# Example
python 102203600.py "Michael Jackson" 10 25 output.mp3
```

### Web Interface

```bash
flask run
```

Visit http://localhost:5000 in your browser

## Web Interface Requirements

1. Form Validation

```xml
<input type="number" name="num_videos" min="10" max="50" required>
<input type="email" name="email" required>
```

2. Email Integration

## Error Handling

- Display error message to user if Singer Name is not found or invalid number of videos or invalid audio duration

## Submission Checklist

- CLI program (102203600.py)
- Web interface (app.py + templates)
- Core processing logic (process_videos.py)
- Proper error handling
- Parameter validation

## License

This project is licensed under the MIT License.

## Acknowledgments

- [MoviePy](https://github.com/Zulko/moviepy)
- [PyTube](https://github.com/pytube/pytube)
- [Flask](https://github.com/pallets/flask)
- [Python-dotenv](https://github.com/theskumar/python-dotenv)
- [Python-dotemail](https://github.com/kennethreitz/python-dotenv)
