import io
from PIL import Image, UnidentifiedImageError


# verifica se uma imagem é válida ou não
def is_image_valid(image: bytes):
    """ Check if the image at the given path is valid.
    :param image: image in bytes.
    :return: True if the image is valid, False otherwise. """
    try:
        with Image.open(io.BytesIO(image)) as img:
            img.verify()
        return True
    except (IOError, SyntaxError, UnidentifiedImageError):
        return False


def check_valid_images(images):
    images_passed = []
    images_failed = []

    for image in images:
        if is_image_valid(image["data"]):
            images_passed.append(image)
        elif not is_image_valid(image["data"]):
            images_failed.append({
                "name": image["name"],
                "message": "File is not a valid image"
            })

    return images_passed, images_failed
