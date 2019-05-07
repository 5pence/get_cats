import os
import cat_service


def print_the_header():
    print('=======================================')
    print('              CAT FACTORY')
    print('=======================================')
    print()


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cats'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory')
        os.mkdir(full_path)

    return full_path


def download_cats(full_path):
    cat_count = 101
    for i in range(1, cat_count):
        name = f'lolcat_{i}'
        cat_service.get_cat(full_path, name)



def main():
    print_the_header()
    full_path = get_or_create_output_folder()
    print(f'Found or created folder: {full_path}')
    print('Getting cats......')
    download_cats(full_path)


if __name__ == '__main__':
    main()
