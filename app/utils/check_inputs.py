from fastapi import UploadFile, HTTPException


ALLOWED_EXTENSIONS = [".jpg", ".jpeg", ".png"]
MAX_FILES = 1000


async def check_inputs(images: list[UploadFile]):
    if not images:
        raise HTTPException(status_code=400, detail="Files must be provided.")

    for file in images:
        if not any(file.filename.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS):
            raise HTTPException(status_code=400, detail="Files must be images "
                                                        f"Allowed Extensions: {ALLOWED_EXTENSIONS}")

    if len(images) > MAX_FILES:
        raise HTTPException(status_code=400, detail=f"Maximum of {MAX_FILES} files allowed.")
