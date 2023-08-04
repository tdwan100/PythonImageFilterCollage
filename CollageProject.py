import math
#from PIL import Image
#import PIL
import image
originalImage = image.FileImage("YourImage.jpg")

def convolve(originalImage, pixelRow, pixelCol, kernel):
    kernelColBase = pixelCol - 1
    kernelRowBase = pixelRow - 1
    total = 0
    for row in range(kernelRowBase, kernelRowBase+3):
        for col in range(kernelColBase, kernelColBase+3):
            kColIndex = col - kernelColBase
            kRowIndex = row - kernelRowBase
            pixel = originalImage.getPixel(col, row)
            intensity = pixel.getRed()
            total = total + intensity * kernel[kRowIndex][kColIndex]
    return total

# flip image

def verticalFlip(originalImage):
    height = originalImage.getHeight()
    width = originalImage.getWidth()
    last = width - 1
    
    verticalFlip = image.EmptyImage(width, height)
    for x in range(width):
        for y in range(height):
            pixel = originalImage.getPixel(last - x, y)
            verticalFlip.setPixel(x, y, pixel)
            
    return verticalFlip

# sepia image

def sepia(originalImage):
    
    width = originalImage.getWidth()
    height = originalImage.getHeight()
    sepia = image.EmptyImage(width, height)
    for y in range(height):
        for x in range(width):
            r, g, b = originalImage.getPixel(x, y)
            red = int(r * 0.293 + g * 0.469 + b * 0.089)
            green = int(r * 0.149 + g * 0.486 + b * 0.068)
            blue = int(r * 0.072 + g * 0.334 + b * 0.031)
            if red > 255:
                red = 255
            if green > 255:
                green = 255
            if blue > 255:
                blue = 255
            pixel = image.Pixel(red, green, blue)
            sepia.setPixel(x, y, pixel)
            
    return sepia

# mirror image

def verticalMirror(originalImage):
    oldW = originalImage.getWidth()
    oldH = originalImage.getHeight()
    verticalMirror = image.EmptyImage(oldW, oldH)
    if oldW % 2 == 0:
        halfway = oldW // 2
    else:
        halfway = oldW // 2 + 1
    maxP = oldW - 1
    for row in range(oldH):
        for col in range(halfway):
            oldPixel = originalImage.getPixel(maxP - col, row)
            verticalMirror.setPixel(maxP - col, row, oldPixel)
            verticalMirror.setPixel(col, row, oldPixel)
    return verticalMirror

# grayscale image

def convertToGrayscale(originalImage):
    
    width = originalImage.getWidth()
    height = originalImage.getHeight()
    convertToGrayscale = image.EmptyImage(width, height)
    for row in range(height):
        for col in range(width):
            pixel = originalImage.getPixel(col, row)
            pixelIntensity = pixel.getRed() + pixel.getGreen() + pixel.getBlue()
            avgRGB = pixelIntensity // 3
            pixel = image.Pixel(avgRGB, avgRGB, avgRGB)            
            convertToGrayscale.setPixel(col, row, pixel)
    return convertToGrayscale

# negative image

def negativePixel(pixel):
    newRed = 255 - pixel.getRed()
    newGreen = 255 - pixel.getGreen()
    newBlue = 255 - pixel.getBlue()
    newPixel = image.Pixel(newRed, newGreen, newBlue)
    return newPixel

def makeNegative(originalImage):
    width = originalImage.getWidth()
    height = originalImage.getHeight()
    makeNegative = image.EmptyImage(width, height)
    for row in range(height):
        for col in range(width):
            oldPixel = originalImage.getPixel(col, row)
            newPixel = negativePixel(oldPixel)
            makeNegative.setPixel(col, row, newPixel)
    return makeNegative

# edge detect image

def edgeImage(originalImage):
    
    grayscale = convertToGrayscale(originalImage)

    edgeImage = image.EmptyImage(originalImage.getWidth(), originalImage.getHeight())
    black = image.Pixel(0, 0, 0)
    white = image.Pixel(255, 255, 255)
    xMask = [ [-1, -2, -1], [0, 0, 0], [1,2,1] ]
    yMask = [ [1, 0, -1], [2, 0, -2], [1,0,-1] ]
    
    for row in range(1, originalImage.getHeight()-1):
        for col in range(1, originalImage.getWidth()-1):
            gX = convolve(grayscale, row, col, xMask)
            gY = convolve(grayscale, row, col, yMask)
            g = math.sqrt(gX**2 + gY**2)
            if g > 175:
                edgeImage.setPixel(col, row, black)
            else:
                edgeImage.setPixel(col, row, white) 
    return edgeImage

# custom filter image

def otherFlip(originalImage):
    height = originalImage.getHeight()
    width = originalImage.getWidth()
    last = width - 1
    
    otherFlip = image.EmptyImage(width, height)
    for x in range(width):
        for y in range(height):
            pixel = originalImage.getPixel(last - y, x)
            otherFlip.setPixel(x, y, pixel)
            
    return otherFlip

# blur image

def blurImage(originalImage):

    grayscale = convertToGrayscale(originalImage)

    blurImage = image.EmptyImage(originalImage.getWidth(), originalImage.getHeight())
    width = originalImage.getHeight()
    height = originalImage.getHeight()
    kmask = [ [1, 2, 1], [2, 1, 2], [1,2,1] ]
    for mask_x in range(1, originalImage.getHeight()-1):
        for mask_y in range(1, originalImage.getWidth()-1):
            gX = convolve(grayscale, width, height, mask_x)
            gY = convolve(grayscale, width, height, mask_y)
            g = math.sqrt(gX**2 + gY**2 / 13)
            R += kmask[mask_x][mask_y] * Pixel.getRed()
            G += kmask[mask_x][mask_y] * Pixel.getRed()
            B += kmask[mask_x][mask_y] * Pixel.getRed()
    return blurImage

#create collage

originalImage = image.FileImage("project6/liam.jpg")
height = originalImage.getHeight()
width  = originalImage.getWidth()

image1 = verticalFlip(originalImage)
image2 = sepia(originalImage)
image3 = verticalMirror(originalImage)
image4 = convertToGrayscale(originalImage)
image5 = makeNegative(originalImage)
image6 = edgeImage(originalImage)
image7 = otherFlip(originalImage)
#image8 = blurImage(originalImage)

window = image.ImageWin(3*width,  3*height, "Image Collage")
image1.setPosition(0, 0)
image2.setPosition(1*width, 0)
image3.setPosition(2*width, 0)
image4.setPosition(0, 1*height)
originalImage.setPosition(1*width, 1*height)
image5.setPosition(2*width, 1*height)
image6.setPosition(0, 2*height)
image7.setPosition(1*width, 2*height)
#image8.setPosition(2*width, 2*height)

image1.draw(window)
image2.draw(window)
image3.draw(window)
image4.draw(window)
originalImage.draw(window)
image5.draw(window)
image6.draw(window)
image7.draw(window)
#image8.draw(window)

window.exitonclick()



