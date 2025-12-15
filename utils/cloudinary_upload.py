from cloudinary import uploader


def upload(file):
    return uploader.upload(file=file)
