import os


IMAGES_OUTPUT_FOLDER = "images_output"


def find_correct_output_folder(image_filename: str):
    """
    This function checks if the output folder exists and if the image folder exists.
    :param image_filename: string with the image filename.
    :return:
    """
    check_if_output_folder_exists()
    path_image_folder = check_if_image_folder_exists(image_filename)
    return path_image_folder


def check_if_output_folder_exists():
    if not os.path.exists(IMAGES_OUTPUT_FOLDER):
        os.makedirs(IMAGES_OUTPUT_FOLDER)


def check_if_image_folder_exists(image_filename: str):
    id_folder = image_filename.split("_")[0]
    year = image_filename.split("_")[2].split("-")[2]

    if not os.path.exists(f"{IMAGES_OUTPUT_FOLDER}/{year}"):
        os.makedirs(f"{IMAGES_OUTPUT_FOLDER}/{year}")

    if not os.path.exists(f"{IMAGES_OUTPUT_FOLDER}/{year}/{id_folder}"):
        os.makedirs(f"{IMAGES_OUTPUT_FOLDER}/{year}/{id_folder}")

    path_image_folder = f"{IMAGES_OUTPUT_FOLDER}/{year}/{id_folder}/"
    return path_image_folder
