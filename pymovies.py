from guessit import guessit
import os

source = './test_directory'
destination = './test_directory2'
min_size = 200000000
video_exts = ['.mkv', '.mp4']
results = {}
for directory, subdirectories, files in os.walk(source):
    for file in files:
        try:
            full_path = os.path.join(directory, file)
            file_name, file_ext = os.path.splitext(file)
            file_info = os.stat(full_path)
            if file_ext in video_exts and file_info.st_nlink == 1 and file_info.st_size > min_size:
                print('\tFound: {}'.format(ascii(full_path)))
                movie_match = guessit(file)
                new_directory = "{} ({}) [{}]".format(movie_match['title'], movie_match['year'], movie_match['screen_size'])
                print("\tMatched with {}".format(new_directory))
                results[full_path] = (destination, new_directory, file)
                confirm = input("\n\tCreate hard link? (Y\\n)\n\t\t{}\n".format(os.path.join(destination, new_directory)))
                if confirm is 'Y':
                    try:
                        os.mkdir(os.path.join(destination, new_directory))
                    except FileExistsError:
                        print('\t\tDirectory already exists.')
                    os.link(full_path, os.path.join(destination, new_directory, file))
                    print('\t\tHard link created succesfully.')
                else:
                    print('\t\tSkipping {}'.format(new_directory))

        except FileNotFoundError:
            print("File not found, skipping...")