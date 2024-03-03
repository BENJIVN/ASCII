import PIL.Image
import math

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize(image, new_width = 100):
    width, height = image.size
    ratio = height/width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width,new_height))
    return(resized_image)

def greyScale (image):
    greyscale_image = image.convert("L")
    return(greyscale_image)

def to_ASCII(image):
    pixels = image.getdata()
    chracters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(chracters)

def main(new_width = 100):
    path = input("Enter a valid pathname to an image: \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not a valie pathname to an image")

    new_image_data = to_ASCII(greyScale(resize(image)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range (0, pixel_count, new_width))

    print(ascii_image)

    with open("ascii_image.txt","w") as f:
        f.write(ascii_image)
main()

#charsArray = list(chars)
#charLength = len(charsArray)
#interval = charLength/256 #0-255

#def getChar(inputInteger):
    #return charsArray[math.floor(inputInteger * interval)]

#text_file = open("Output.txt", "w") #python open function creating a txt file in "w" write mode
##read image 
#image = Image.open( 'Nathan.png' )
#width, height = image.size #Image module, size in pixels 2 -tuple
#pix = image.load() #allocates storage for the image and loads pixel data
##print(width,height)

##iterate through the 2D array of pixels 
##pix[x,y] will give you the RGB value at that location
##calculate the grey value 
#for i in range(height): 
    #for j in range(width): 
        #r, g, b, _ = pix[j,i] #alpha channel bc of PNG images
        #h = int(r/3 + g/3 + b/3) 
        #pix[j,i] = (h, h, h)
        #text_file.write(getChar(h))
    #text_file.write('\n')
#text_file.close

#image.save("output.png")