import uuid
from django.db import models


def scramble_upload_filename(instance, filename):
    print("filename>>>>>>>>>>>>>>",filename)
    print(filename.split("."))
    extension = filename.split(".")(-1)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(extension)
    return "{}.{}".format(uuid.uuid4(), extension)


class UploadImage(models.Model):
    # Stores an uploaded image.
    #image = models.ImageField("Upload Image", upload_to=scramble_upload_filename)
    image = models.ImageField("Upload Image")

