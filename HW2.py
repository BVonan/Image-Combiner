from PIL import Image
import glob
# going to import glob
# goign to use my_images
# download hw2 images

# formula for median function
def my_median(color_list):
    color_list.sort()
    m = (len(color_list) - 1) // 2
    return color_list[m] 


# task3
# Using glob to output the single image needed
my_images = []
for image in glob.glob('hw2_images/*.png'):
    my_images.append(Image.open(image))

# task3

# task2
Opening the i3 given images
image1 = Image.open('img_1.jpg')
image2 = Image.open('img_2.jpg')
image3 = Image.open('img_3.jpg')

# Making a list for the images RGB's
# my_images = [image1, image2, image3]
r_list = []
g_list = []
b_list = []

# Storing the height and width of the images
w = my_images[0].width
h = my_images[0].height
# w = image1.width
# h = image1.height

# Printing the images height and width 
print(w)
print(h)

# Using the calculated RGB values to create a new pixel to place in a new image
for x in range(w):
    for y in range(h):
        for i in my_images:
            r = i.getpixel((x,y))[0]
            g = i.getpixel((x,y))[1]
            b = i.getpixel((x,y))[2]
            r_list.append(r)
            g_list.append(g)
            b_list.append(b)
        mr = my_median(r_list)
        mg = my_median(g_list)
        mb = my_median(b_list)
        i.putpixel((x,y),(mr,mg,mb))
        r_list = []
        g_list = []
        b_list = []
i.show() 
# Showing the new image


