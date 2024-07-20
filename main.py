import sys
from PIL import Image
from os import listdir
from utils import getWinSize
from imageConverter import convertToAsciiPixels
from asciiConverter import convertToAsciiChars, convertToBrailleChars, AsciiChar


def getOpts(argsList):
    optDict = {}
    for arg in argsList:
        if arg.startswith("-"):
            if "=" in arg:
                data = arg.split("=")
                optDict[data[0]] = data[1]
            else:
                optDict[arg] = ""
    return optDict

def printAsciiImage(asciiImage: list[list[AsciiChar]]):
    for row in asciiImage:
        for rowVl in row:
            print(rowVl.charWithColor, end="")
        print()


def Image2AsciiCLI(*args):
    try:
        optDict = getOpts(args)
        if "-pth" in optDict: imgPath = optDict["-pth"]
        else: imgPath = args[1]

        image = Image.open(imgPath)

        imgWidth, imgHeight = image.size
        winWidth, winHeight = getWinSize()
        width, height = 0, 0

        if "-wd" in optDict: width = int(optDict["-wd"])
        elif "-ht" in optDict: height = int(optDict["-ht"])
        elif "-swd" in optDict: width = imgWidth * float(optDict["-swd"])
        elif "-sht" in optDict: height = imgHeight * float(optDict["-sht"])
        elif "-fwd" in optDict: width = winWidth * float(optDict["-fwd"])
        elif "-fht" in optDict: height = winHeight * float(optDict["-fht"])
        else: width = winWidth

        isColored = "-cl" in optDict
        isBraille = "-bri" in optDict
        isComplex = "-cx" in optDict

        asciiPixels = convertToAsciiPixels(image, int(width), int(height), full=False, isBraille=isBraille)
        if isBraille: asciiImage = convertToBrailleChars(asciiPixels, colored=isColored)
        else: asciiImage = convertToAsciiChars(asciiPixels, colored=isColored, complexMode=isComplex)

        printAsciiImage(asciiImage)
    except IndexError: print("Invalid usage")
    except FileNotFoundError or ValueError or TypeError:
        print(f"'{args[1]}' file is Invalid or File not found")


if __name__ == "__main__":
    args = sys.argv
    optDict = getOpts(args)

    if "-dir" in optDict:
        imgDir = optDict["-dir"]
        for img in listdir(imgDir):
            if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith(".png"):
                print(f"Printing {imgDir}/{img}")
                Image2AsciiCLI(f"-pth={imgDir}/{img}", *args)
                input()
    else:
        Image2AsciiCLI(*args)