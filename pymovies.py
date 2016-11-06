from guessit import guessit
import os

root = '.'
for directory, subdirectories, files in os.walk(root):
    for file in files:
        try:
            full_path = os.path.join(directory, file)
            file_info = os.stat(full_path)
            if file_info.st_nlink == 1:
                print('\tFound: {}'.format(ascii(full_path)))
                movie_match = guessit(full_path)
                print("\tMatched with {}".format(movie_match['title']))
        except FileNotFoundError:
            print("File not found, skipping...")