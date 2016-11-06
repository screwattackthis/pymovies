from guessit import guessit
import os

root = '.'
for directory, subdirectories, files in os.walk(root):
    print('Directory: {}'.format(ascii(directory)))
    for file in files:
        file_info = os.stat(file)
        if file_info.st_nlink == 1:
            full_path = os.path.join(directory, file)
            print('\tFound: {}'.format(ascii(full_path)))
            movie_match = guessit(full_path)
            print("\tMatched with {}".format(movie_match['title']))