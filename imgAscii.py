import PIL.Image
import PIL

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def recizeImg(img, newWidth = 100):
    '''function resizing an image'''
    width, height = img.size
    ratio = height/ float(width * 2.5)
    newHeight = int(newWidth * ratio)
    resizedImage = img.resize((newWidth,newHeight))
    return resizedImage



def imgGray(img):
    '''function converting an image to gray scale'''
    grayscaleImage = img.convert("L")
    return grayscaleImage


def pxlToAscii(img):
    '''function converting gray pixels to Ascii symbols'''
    pixels = img.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return (characters)



def imgToAscii(imgFrame, newWidth=100):

    path = imgFrame

    frame = PIL.Image.open(path)

    newImgData = pxlToAscii(imgGray(recizeImg(frame)))

    pixelCount = len(newImgData)
    asciiImage = "\n".join(newImgData[i:(i+newWidth)] for i in range (0, pixelCount, newWidth))

    print(asciiImage)
    print()
    print()