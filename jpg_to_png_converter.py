import sys
from pathlib import Path
from PIL import Image
import constants

def convert_all_jpeg_images_to_png_format(source_folder, destination_folder):

    if not folder_exists(folder_name=source_folder):
        print(f'Source folder: {source_folder} doesn\'t exist')
        return
    
    if not folder_exists(destination_folder):
        create_destination_folder(destination_folder)
    
    jpg_files_sorted = sorted(Path(source_folder).glob('*.jpg'))

    jpg_file_names = []

    for jpg in jpg_files_sorted:
        jpg_file_names.append(jpg.name)

    convert_jpg_to_png(jpg_file_names, destination_folder)      

    return

def folder_exists(folder_name=''):
    return Path(folder_name).exists()

def create_destination_folder(destination_folder_name):
    try:
        dest_dir = Path(destination_folder_name).mkdir()
        print(f'Destination directory created: {dest_dir}')
    except ValueError as error:
        print(error)

def display_empty_args_error_message(folder_type_name):
    print(f'Give a {folder_type_name} folder path!')

def convert_jpg_to_png(jpg_file_names, destination_folder):

    for jpg_name in jpg_file_names:
        image_name = jpg_name.split(".", 1)[0]
        img = Image.open(source_folder + jpg_name,'r')
        img.save(f'{destination_folder}{image_name}.png')
    
    print("All images are converted from jpg to png!👍")


if __name__ == '__main__':
    '''
    Main entry of a program
    '''

    source_folder = str(sys.argv[1])
    destination_folder = str(sys.argv[2])

    if  "/" not in source_folder :
        source_folder=source_folder+'/'


    if(len(source_folder.strip())==0):
        display_empty_args_error_message(constants.CONST_ERROR_MSG_SOURCE)

    elif(len(destination_folder.strip())==0):
        display_empty_args_error_message(constants.CONST_ERROR_MSG_DESTINATION)

    else:  
        convert_all_jpeg_images_to_png_format(source_folder=constants.CONST_SOURCE_FOLDER, destination_folder=constants.CONST_DESTINATION_FOLDER)