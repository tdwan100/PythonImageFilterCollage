# Image Processing Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains a collection of image processing functions and filters written in Python using the `image` library. The functions provided here can be used to manipulate images in various ways and create interesting effects.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
  - [convolve](#convolve)
  - [verticalFlip](#verticalFlip)
  - [sepia](#sepia)
  - [verticalMirror](#verticalMirror)
  - [convertToGrayscale](#convertToGrayscale)
  - [makeNegative](#makeNegative)
  - [edgeImage](#edgeImage)
  - [otherFlip](#otherFlip)
  - [blurImage](#blurImage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python 3.x
- The `image` library

## Installation

To use the image processing functions, make sure you have Python 3.x installed. You can install the `image` library using pip:

```
pip install image
```

## Usage

Clone this repository to your local machine to access the image processing functions.

```
git clone https://github.com/your-username/image-processing-toolkit.git
```

## Functions

### convolve

The `convolve` function applies a given kernel to a specific pixel in the image. It computes the weighted sum of the pixel intensities in the neighborhood of the specified pixel.

### verticalFlip

The `verticalFlip` function flips the image vertically.

### sepia

The `sepia` function applies a sepia tone effect to the image.

### verticalMirror

The `verticalMirror` function creates a mirror effect by reflecting the left half of the image to the right half.

### convertToGrayscale

The `convertToGrayscale` function converts the image to grayscale by averaging the RGB values of each pixel.

### makeNegative

The `makeNegative` function creates a negative image by subtracting the RGB values from 255.

### edgeImage

The `edgeImage` function applies edge detection to the image using the Sobel operator.

### otherFlip

The `otherFlip` function flips the image differently compared to the `verticalFlip` function.

### blurImage

The `blurImage` function applies a blurring effect to the image using a kernel.

## Example

Here is an example of how to use the image processing functions:

```
# Load the original image
originalImage = FileImage("YourImageFile.jpg")
```

## Contributing

Contributions to this project are welcome. Feel free to open issues or submit pull requests.
