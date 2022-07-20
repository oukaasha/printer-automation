import qrcode
import fitz
import io
import os
import uuid

INPUTDIR = './input'
OUTPUTDIR = './to-be-processed'

input_filenames = [f for f in os.listdir(INPUTDIR) if f.endswith('.pdf')]

for input_file in input_filenames:
    doc = fitz.open(os.path.join(INPUTDIR, input_file))

    page_num = 1

    for page in doc:
        image_byte_array = io.BytesIO()
        img = qrcode.make(str(uuid.uuid4()) + '-' + str(page_num))
        img.save(image_byte_array, format='PNG')
        page.insert_image(
            fitz.Rect(page.rect.width-100, 5, page.rect.width-50, 55),                  # where to place the image (rect-like)
            filename=None,         # image in a file
            stream=image_byte_array.getvalue(),           # image in memory (bytes)
            pixmap=None,           # image from pixmap
            mask=None,             # specify alpha channel separately
            rotate=0,              # rotate (int, multiple of 90)
            xref=0,                # re-use existing image
            oc=0,                  # control visibility via OCG / OCMD
            keep_proportion=True,  # keep aspect ratio
            overlay=True,          # put in foreground
        )
        page_num += 1

    doc.save(OUTPUTDIR + '/' + input_file)
