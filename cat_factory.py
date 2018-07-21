import os

def main():
    # print the header
    print_header()
    # get or create output folder
    get_or_create_output_folder()
    # download cats
    # display cats

def print_header():
    print('------------------------------')
    print('------ Cat FACTorY ^._.^ -----')
    print('------------------------------')


def get_or_create_output_folder():
    print(__file__)
    folder = 'cat_pictures'
    full_path = os.path.abspath(os.path.join('.',folder))
    print(full_path)


if __name__ == '__main__':
    main()
