import logging
import azure.functions as func
from PIL import Image
import io
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Read the image from the request
    try:
        image_data = req.get_body()
        image = Image.open(io.BytesIO(image_data))
    except Exception as e:
        logging.error(f"Error reading image: {e}")
        return func.HttpResponse("Invalid image data", status_code=400)

    # Convert the image to grayscale
    grayscale_image = image.convert("L")

    # Save the grayscale image to a byte stream
    img_byte_arr = io.BytesIO()
    grayscale_image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # Return the grayscale image in the HTTP response
    return func.HttpResponse(body=img_byte_arr, mimetype="image/png")
