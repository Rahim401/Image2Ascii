from utils import getColoredCharForTerm

# ASCII tables
asciiTableSimple = " .:-=+*#%@"
asciiTableDetailed = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# Braille structure
brailleStruct = [
    [0x1, 0x8],
    [0x2, 0x10],
    [0x4, 0x20],
    [0x40, 0x80]
]

# Constants
MAX_VAL = 255
BrailleThreshold = 0


class AsciiChar:
    def __init__(self):
        self.char = ""
        self.charWithColor = ""
        self.setColor = ""
        self.rgbValue = [0, 0, 0]


def convertToAsciiChars(imgSet, negative=False, colored=True, complexMode=False, colorBg=True, customMap="", fontColor=(255, 255, 255)):
    height = len(imgSet)
    width = len(imgSet[0])

    if customMap == "":
        charSet = asciiTableDetailed if complexMode else asciiTableSimple
        chosenTable = {index: char for index, char in enumerate(charSet)}
    else:
        chosenTable = {index: char for index, char in enumerate(customMap)}

    result = []

    for i in range(height):
        tempSlice = []

        for j in range(width):
            value = float(imgSet[i][j]["charDepth"])

            tempFloat = (value / MAX_VAL) * len(chosenTable)
            if value == MAX_VAL:
                tempFloat = len(chosenTable) - 1
            tempInt = int(tempFloat)

            r, g, b = (imgSet[i][j]["rgbValue"] if colored else (imgSet[i][j]["grayscaleValue"], 0, 0))

            if negative:
                r = 255 - r
                g = 255 - g
                b = 255 - b
                tempInt = (len(chosenTable) - 1) - tempInt

            char = AsciiChar()
            char.char = chosenTable[tempInt]

            if colorBg:
                char.charWithColor = getColoredCharForTerm(r, g, b, char.char, True)
            else:
                char.charWithColor = getColoredCharForTerm(r, g, b, char.char, False)

            if fontColor != (255, 255, 255):
                fcR, fcG, fcB = fontColor
                if colorBg:
                    char.setColor = getColoredCharForTerm(fcR, fcG, fcB, char.char, True)
                else:
                    char.setColor = getColoredCharForTerm(fcR, fcG, fcB, char.char, False)

            char.rgbValue = [r, g, b]
            tempSlice.append(char)

        result.append(tempSlice)

    return result


def convertToBrailleChars(imgSet, negative=False, colored=True, colorBg=True, fontColor=(255,255,255), threshold=20):
    global BrailleThreshold
    BrailleThreshold = threshold
    height = len(imgSet)
    width = len(imgSet[0])

    result = []

    for i in range(0, height, 4):
        tempSlice = []

        for j in range(0, width, 2):
            brailleChar = getBrailleChar(i, j, negative, imgSet)
            r, g, b = (imgSet[i][j]["rgbValue"] if colored else (imgSet[i][j]["grayscaleValue"], 0, 0))

            if negative:
                r = 255 - r
                g = 255 - g
                b = 255 - b

            char = AsciiChar()
            char.char = brailleChar

            if colorBg:
                char.charWithColor = getColoredCharForTerm(r, g, b, brailleChar, True)
            else:
                char.charWithColor = getColoredCharForTerm(r, g, b, brailleChar, False)

            if fontColor != (255, 255, 255):
                fcR, fcG, fcB = fontColor
                if colorBg:
                    char.setColor = getColoredCharForTerm(fcR, fcG, fcB, brailleChar, True)
                else:
                    char.setColor = getColoredCharForTerm(fcR, fcG, fcB, brailleChar, False)

            char.rgbValue = [r, g, b]
            tempSlice.append(char)

        result.append(tempSlice)

    return result


def getBrailleChar(x, y, negative, imgSet):
    brailleChar = 0x2800

    for i in range(4):
        for j in range(2):
            if negative:
                if imgSet[x + i][y + j]["charDepth"] <= BrailleThreshold:
                    brailleChar += brailleStruct[i][j]
            else:
                if imgSet[x + i][y + j]["charDepth"] >= BrailleThreshold:
                    brailleChar += brailleStruct[i][j]

    return chr(brailleChar)
