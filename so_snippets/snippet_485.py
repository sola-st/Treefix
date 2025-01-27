# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
# Importing Image class from PIL module
from l3.Runtime import _l_
try:
    from PIL import Image
    _l_(2076)

except ImportError:
    pass

# Opens a image in RGB mode
im = Image.open(r"C:\Users\System-Pc\Desktop\ybear.jpg")
_l_(2077)

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
_l_(2078)

# Setting the points for cropped image
left = 4
_l_(2079)
top = height / 5
_l_(2080)
right = 154
_l_(2081)
bottom = 3 * height / 5
_l_(2082)

# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
_l_(2083)
newsize = (300, 300)
_l_(2084)
im1 = im1.resize(newsize)
_l_(2085)
# Shows the image in image viewer
im1.show()
_l_(2086)

