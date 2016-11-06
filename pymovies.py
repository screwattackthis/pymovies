from guessit import guessit
import os

root = '.'
min_size = 200000000
video_exts = ['.mkv', '.mp4']
for directory, subdirectories, files in os.walk(root):
    for file in files:
        try:
            full_path = os.path.join(directory, file)
            file_name, file_ext = os.path.splitext(file)
            file_info = os.stat(full_path)
            if file_ext in video_exts and file_info.st_nlink == 1 and file_info.st_size > min_size:
                print('\tFound: {}'.format(ascii(full_path)))
                movie_match = guessit(file)
                print("\tMatched with {}".format(movie_match['title']))
        except FileNotFoundError:
            print("File not found, skipping...")