import os
import cat_services
import subprocess


def main():
    # print the header
    print_header()
    # get or create output folder
    folder = get_or_create_output_folder()
    # print('Found or Created folder: ' + folder)
    # download cats
    download_cats(folder)
    # display cats
    display_cats(folder)


def print_header():
    print('------------------------------')
    print('------ Cat FACTorY ^._.^ -----')
    print('------------------------------')


def get_or_create_output_folder():
    # print(__file__)
    base_folder = os.path.abspath(os.path.dirname(__file__))
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)
    # full_path = os.path.abspath(os.path.join('.',folder))
    # print(full_path)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('Contacting Api services to download cats ... ... .. ^._.^')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat {}'.format(i)
        print('Downloading Cat -->' + name)
        # print(i, end=',')
        cat_services.get_cats(folder, name)

    print("Done !")


def display_cats(folder):
    # open folder process
    print('Displaying cat images ....... ^._.^')
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't support your os: " + platform.system())


if __name__ == '__main__':
    main()
