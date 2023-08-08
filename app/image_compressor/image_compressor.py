from PIL import Image
import os
import io

from app.image_compressor.find_output_path import find_correct_output_folder
from app.image_compressor.image_validation import check_valid_images


def compress_image(image, quality, output_folder):
    try:
        img = Image.open(io.BytesIO(image["data"]))

        # Convert RGBA to RGB if the image has an alpha channel.
        if img.mode == "RGBA":
            img = img.convert("RGB")

        # Save the image again with reduced quality.
        file_name = image["name"]
        img.save(f"{output_folder}/{file_name}", format="JPEG", optimize=True, quality=quality)

        return True

    except Exception as e:
        print(e)
        return False


def compress_all_images(images, quality):
    images_compressed = []
    images_not_compressed = []

    images_passed, images_failed = check_valid_images(images)

    if images_passed:
        output_folder = find_correct_output_folder(images_passed[0]["name"])

        for image in images_passed:
            compressed_image = compress_image(image, quality, output_folder)
            if compressed_image:
                images_compressed.append({
                    "name": image["name"],
                    "message": "Compressed successfully."
                })
            else:
                images_not_compressed.append({
                    "name": image["name"],
                    "message": "File could not be compressed"
                })

        return images_compressed, images_not_compressed, images_failed

    else:
        return [], [], images_failed


# abre a imagem e retorna seu tamanho (largura e altura) como uma tupla
def get_image_size(image_path):
    with Image.open(image_path) as img:
        return img.size


# calcula o tamanho da imagem após a compactação usando o nível de qualidade especificado. Ele salva temporariamente a
# imagem compactada, mede seu tamanho e remove o arquivo temporário
def get_compressed_image_size(image_path, quality):
    img = Image.open(image_path)
    if img.mode == "RGBA":
        img = img.convert("RGB")
    temp_output = "temp_compressed.jpg"
    img.save(temp_output, "JPEG", optimize=True, quality=quality)
    size = os.path.getsize(temp_output)
    os.remove(temp_output)
    return size
