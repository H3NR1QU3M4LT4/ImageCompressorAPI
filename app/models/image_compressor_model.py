""" Modelo de resposta do serviço de compressão de imagem
"""
from pydantic import BaseModel
from typing import Optional


"""def form_body(cls):
    cls.__signature__ = cls.__signature__.replace(
        parameters=[
            arg.replace(default=Form(arg.default))
            for arg in cls.__signature__.parameters.values()
        ]
    )
    return cls"""


# @form_body
class ImageCompressorInput(BaseModel):
    token: str = "default_token"
    quality_value: int = 10
    topic_id: int = 1
    survey_id: int = 1
    user_destiny: str = "default_user"
    phone_destiny: int = 1234567890
    msg_destiny: str = "default_message"


class ImageCompressorSuccessResponse(BaseModel):
    image_filename: str
    message: str


class ImageCompressorImageNotValid(BaseModel):
    image_filename: str
    message: str


class ImageCompressorFailedResponse(BaseModel):
    image_filename: str
    message: str


class ImageCompressorResponse(BaseModel):
    images_not_valid: list[ImageCompressorFailedResponse]
    images_not_compressed: list[ImageCompressorImageNotValid]
    images_passed: list[ImageCompressorSuccessResponse]