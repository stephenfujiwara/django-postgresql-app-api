import PIL
import numpy as np
from cvzone.SelfiSegmentationModule import SelfiSegmentation
from io import BytesIO
import os
from django.core.files.base import ContentFile

def remove_bg(img):
    pil_img = PIL.Image.open(img)
    np_img = np.array(pil_img)
    segmentor = SelfiSegmentation()
    nobg_img = segmentor.removeBG(np_img, (0, 255, 0), threshold=0.5)
    buffer = BytesIO()
    output_img = PIL.Image.fromarray(nobg_img)
    output_img.save(buffer, format="png")
    # data stored in buffer
    val = buffer.getvalue()
    return ContentFile(val) 
