# Image2Ascii

Image2Ascii Converter is a Python script that converts images to ASCII art in the terminal. This project was inspired by and translated from a similar project in Go, [ascii-image-converter](https://github.com/TheZoraiz/ascii-image-converter) by TheZoraiz.

## Overview

This script allows you to convert images into ASCII art directly in your terminal. It supports various options for resizing, applying colors, and choosing between standard ASCII characters or Braille characters.

## Features

- **Image Conversion**: Convert images to ASCII art using PIL (Python Imaging Library).
- **Terminal Output**: Display ASCII art directly in the terminal.
- **Options**: Resize images, apply colors, and choose between standard ASCII or Braille characters.

## Usage

### Requirements

Make sure you have Python installed along with the following libraries:
- Numpy
- PIL (Python Imaging Library)

### Command Line Interface (CLI)

The script can be executed from the command line with various options:

```bash
python image2ascii.py [-pth=<image_path>] [-wd=<width>] [-ht=<height>] [-swd=<scale_width>] [-sht=<scale_height>] [-fwd=<fraction_width>] [-fht=<fraction_height>] [-cl] [-bri] [-cx] [-dir=<directory_path>]
```

### Options

- `-pth=<image_path>`: Specify the path to the image file. If not provided, the script will use the first positional argument as the image path.
- `-wd=<width>`: Set the width of the output image in characters.
- `-ht=<height>`: Set the height of the output image in characters.
- `-swd=<scale_width>`: Scale the output width by the given fraction.
- `-sht=<scale_height>`: Scale the output height by the given fraction.
- `-fwd=<fraction_width>`: Fit the output width to the terminal width multiplied by the given fraction.
- `-fht=<fraction_height>`: Fit the output height to the terminal height multiplied by the given fraction.
- `-cl`: Enable colored output.
- `-bri`: Enable Braille mode.
- `-cx`: Enable complex mode (uses a detailed ASCII character set).

### Example

#### Convert a single image:

```bash
python image2ascii.py -pth=path/to/image.jpg -wd=100 -ht=50 -cl
```

- Converts `path/to/image.jpg` to ASCII art with a width of 100 characters, height of 50 characters, and colored output.

#### Convert images in a directory:

```bash
python image2ascii.py -dir=path/to/images/directory
```

- Converts all `.jpg`, `.jpeg`, and `.png` images in `path/to/images/directory` to ASCII art.

### Notes

- Ensure your terminal supports ANSI escape codes for colored output.
- Use `-dir` option to convert multiple images in a directory.
