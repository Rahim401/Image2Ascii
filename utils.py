import numpy as np
from PIL import Image
from platform import system
from typing import Tuple, List
from os import get_terminal_size

# Constants
MAX_VAL = 255

def getWinSize():
    return get_terminal_size()


# Function to resize image
def resizeImage(image: Image, full: bool, isBraille: bool, width: int, height: int) -> Tuple[Image, None]:
    """
    Resizes the input image according to specified parameters.

    Args:
    - image: PIL Image object
    - full: boolean flag for full terminal size
    - isBraille: boolean flag for braille mode
    - dimensions: list of dimensions [width, height]
    - width: integer width of the image
    - height: integer height of the image

    Returns:
    - resized image: PIL Image object
    - error: None or exception message
    """

    # Get image dimensions
    imgWidth, imgHeight = image.size
    aspectRatio = imgWidth / imgHeight

    # Calculate ASCII dimensions
    if full:
        terminalWidth, terminalHeight = getWinSize()
        asciiWidth = terminalWidth - 1
        asciiHeight = int(asciiWidth / aspectRatio * 0.5)
    elif width != 0 and height == 0:
        asciiWidth = width
        asciiHeight = int(asciiWidth / aspectRatio * 0.5)
    elif height != 0 and width == 0:
        asciiHeight = height
        asciiWidth = int(asciiHeight * aspectRatio * 2)
    else:
        asciiWidth = width
        asciiHeight = height
        # raise ValueError("Both width and height can't be set. Use dimensions instead.")

    # Adjust for braille mode
    if isBraille:
        asciiWidth *= 2
        asciiHeight *= 4

    # Resize the image
    resizedImage = image.resize((asciiWidth, asciiHeight), Image.LANCZOS)

    return resizedImage, None


# Function to reverse image
def reverse(imgSet: List[List[Tuple[int, int, int]]], flipX: bool, flipY: bool) -> List[List[Tuple[int, int, int]]]:
    """
    Reverses the input image according to specified parameters.

    Args:
    - imgSet: list of list of tuples representing image pixels
    - flipX: boolean flag for flipping horizontally
    - flipY: boolean flag for flipping vertically

    Returns:
    - reversed image: list of list of tuples representing reversed image pixels
    """

    imgSet = np.array(imgSet)

    if flipX:
        imgSet = np.flip(imgSet, axis=1)

    if flipY:
        imgSet = np.flip(imgSet, axis=0)

    return imgSet.tolist()


# Function to get colored character for terminal
def getColoredCharForTerm(r: int, g: int, b: int, char: str, background: bool) -> str:
    """
    Returns the colored character for the terminal.

    Args:
    - r: integer red color component
    - g: integer green color component
    - b: integer blue color component
    - char: string character to be colored
    - background: boolean flag for background color

    Returns:
    - colored character: string
    """

    if system() == "Windows": return char
    # Use your preferred method to render colored characters in terminal
    # This example uses ANSI escape codes
    return f"\033[48;2;{r};{g};{b}m{char}\033[0m"

# Example usage:
# img = Image.open("path_to_image.jpg")
# dithered_img = ditherImage(img)
# resized_img, _ = resizeImage(img, True, False, [], 0, 0)
# reversed_img = reverse(imgSet, True, False)
# colored_char = getColoredCharForTerm(255, 0, 0, "*", True)

# Note: Replace the rendering method in `getColoredCharForTerm` as per your terminal's capability.
