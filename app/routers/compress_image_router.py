""".
"""
from fastapi import UploadFile, File
import asyncio
from fastapi import APIRouter, Depends

from app.image_compressor.image_compressor import compress_all_images
from app.models.image_compressor_model import ImageCompressorInput, ImageCompressorResponse, \
    ImageCompressorSuccessResponse, \
    ImageCompressorImageNotValid, ImageCompressorFailedResponse
from app.utils.check_inputs import check_inputs

router = APIRouter()


@router.post("/compress_image", tags=["Excel Writer"], summary="Solar predictions",
             response_model=ImageCompressorResponse,
             response_description="Predicted values", dependencies=[Depends(check_inputs)])
async def process_files(images: list[UploadFile] = File(...),
                        form_data: ImageCompressorInput = Depends(ImageCompressorInput)):

    images_bytes = await asyncio.gather(*(read_file(image) for image in images))

    images_compressed, images_not_compressed, images_failed = compress_all_images(images_bytes,
                                                                                  form_data.quality_value)
    response = mapping_response(images_compressed, images_not_compressed, images_failed)

    return response


async def read_file(file):
    return {
        "name": file.filename,
        "data": await file.read()
    }


def mapping_response(images_compressed, images_not_compressed, images_failed):
    response = ImageCompressorResponse(
        images_not_valid=[ImageCompressorImageNotValid(image_filename=image["name"], message=image["message"])
                          for image in images_failed],
        images_not_compressed=[ImageCompressorFailedResponse(image_filename=image["name"], message=image["message"])
                               for image in images_not_compressed],
        images_passed=[ImageCompressorSuccessResponse(image_filename=image["name"],
                                                      message=image["message"]) for image in
                       images_compressed]
    )

    return response
