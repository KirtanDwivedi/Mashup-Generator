import sys
from moviepy.editor import VideoFileClip

def process_videos(artist_name, num_videos, duration, output_file):
    if artist_name != "Michael Jackson":
        print(f"{artist_name} is not in directory")
        return

    if not 1 <= num_videos <= 10:
        print("Please enter a number between 1 and 10")
        return
    
    videos = []
    audios = []
    
    for i in range(1, num_videos + 1):
        video_name = f"{i:02d}.mp4"
        audio_name = f"a{i}.mp3"
        
        try:
            video = VideoFileClip(video_name)
            total_duration = video.duration
            if duration > total_duration:
                print(f"Error: Requested duration ({duration}s) exceeds video length ({total_duration}s) for {video_name} or the duration is not a valid number")
                video.close()
                return

            audio = video.subclip(0, duration).audio
            audio.write_audiofile(audio_name)
            
            videos.append(video)
            audios.append(audio)
            
        except Exception as e:
            print(f"Error processing {video_name}: {str(e)}")
            return
        
    print(f"Processing complete! Merged audio saved as {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <artist_name> <num_videos> <duration> <output_file>")
        sys.exit(1)
    
    artist_name = sys.argv[1]
    num_videos = int(sys.argv[2])
    duration = float(sys.argv[3])
    output_file = sys.argv[4]
    
    process_videos(artist_name, num_videos, duration, output_file)