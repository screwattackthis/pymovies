from guessit import guessit
import os

root = '.'
for directory, subdirectories, files in os.walk(root):
    print('Directory: {}'.format(ascii(directory)))
    for file in files:
        file_info = os.stat(file)
        if file_info.st_nlink == 1:
            print('Found file {} and matching...'.format(ascii(file), 'ignore'))
            movie_match = guessit(file)
            print("Matched with {}".format(movie_match['title']))