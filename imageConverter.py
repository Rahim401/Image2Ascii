from typing import List
from PIL import Image, ImageOps
from utils import resizeImage

# Constants
MAX_VAL = 255

# Function to convert image to ASCII pixels
def convertToAsciiPixels(
        image: Image, width: int = 0, height: int = 0,
        full: bool = False, flipX: bool = False, flipY: bool = False,
        isBraille: bool = True,
) -> List[List[dict]]:
    """
    Converts the input image to ASCII pixels according to specified parameters.

    Args:
    - image: PIL Image object
    - width: integer width of the image
    - height: integer height of the image
    - flipX: boolean flag for flipping horizontally
    - flipY: boolean flag for flipping vertically
    - full: boolean flag for full terminal size

    Returns:
    - 2D list of AsciiPixel dictionaries representing each pixel's values
    """

    # Resize the image
    smallImg, _ = resizeImage(image, full, isBraille, width, height)

    # Initialize the list for storing AsciiPixel dictionaries
    imgSet = []

    # Iterate through each pixel of resized image and get an AsciiPixel instance
    for y in range(smallImg.height):
        temp = []
        for x in range(smallImg.width):

            # Get original and grayscale values
            oldPixel = smallImg.getpixel((x, y))
            grayPixel = ((oldPixel[0] + oldPixel[1] + oldPixel[2]) / 3,)

            charDepth = grayPixel[0]  # Only need the first value for charDepth in AsciiPixel

            # Get colored RGB values of original pixel
            rgbValues = oldPixel[:3]

            temp.append({
                "charDepth": charDepth,
                "grayscaleValue": grayPixel,
                "rgbValue": rgbValues
            })

        imgSet.append(temp)

    # Apply flipping if necessary
    if flipX or flipY:
        imgSet = reverse(imgSet, flipX, flipY)

    return imgSet


# Function to reverse image
def reverse(imgSet: List[List[dict]], flipX: bool, flipY: bool) -> List[List[dict]]:
    """
    Reverses the input image according to specified parameters.

    Args:
    - imgSet: 2D list of dictionaries representing image pixels
    - flipX: boolean flag for flipping horizontally
    - flipY: boolean flag for flipping vertically

    Returns:
    - reversed image: 2D list of dictionaries representing reversed image pixels
    """

    if flipX:
        for row in imgSet:
            row.reverse()

    if flipY:
        imgSet.reverse()

    return imgSet


# Example usage:
# img = Image.open("path_to_image.jpg")
# asciiPixels = convertToAsciiPixels(img, [], 0, 0, True, False, False, False, True)

# Note: Ensure you have PIL and other required libraries installed to run the code.
