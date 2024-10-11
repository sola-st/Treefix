# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
# Importing Image class from PIL module
from l3.Runtime import _l_
try:
    from PIL import Image
    _l_(12853)

except ImportError:
    pass

# Opens a image in RGB mode
im = Image.open(r"C:\Users\System-Pc\Desktop\ybear.jpg")
_l_(12854)

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
_l_(12855)

# Setting the points for cropped image
left = 4
_l_(12856)
top = height / 5
_l_(12857)
right = 154
_l_(12858)
bottom = 3 * height / 5
_l_(12859)

# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
_l_(12860)
newsize = (300, 300)
_l_(12861)
im1 = im1.resize(newsize)
_l_(12862)
# Shows the image in image viewer
im1.show()
_l_(12863)

