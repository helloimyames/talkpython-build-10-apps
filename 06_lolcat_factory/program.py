import os
import cat_service
import subprocess

def main():
    # print the header
    print_header()
    # get or create output folder
    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)
    # download cats
    download_cats(folder)
    # display cats
    display_cats(folder)


def print_header():
    print('------------------------------')
    print('          CAT FACTORY')
    print('------------------------------')


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)
    
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('creating new directory at {}'.format(full_path))
        os.mkdir(full_path)
    
    return full_path


def download_cats(folder):
    # we're gonna get 8 cats
    cat_count = 8
    for i in range(1, cat_count+1):
        # cat name will be index num
        name = 'lolcat_{}'.format(i)
        cat_service.get_cat(folder, name)
        
        
def display_cats(folder):
    subprocess.call(['open', folder])


if __name__=="__main__":
    main()
