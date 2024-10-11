# Extracted from https://stackoverflow.com/questions/902761/saving-a-numpy-array-as-an-image
def saveAsPNG(array, filename):
    import struct
    if any([len(row) != len(array[0]) for row in array]):
        raise ValueError, "Array should have elements of equal size"

                                #First row becomes top row of image.
    flat = []; map(flat.extend, reversed(array))
                                 #Big-endian, unsigned 32-byte integer.
    buf = b''.join([struct.pack('>I', ((0xffFFff & i32)<<8)|(i32>>24) )
                    for i32 in flat])   #Rotate from ARGB to RGBA.

    data = write_png(buf, len(array[0]), len(array))
    f = open(filename, 'wb')
    f.write(data)
    f.close()

saveAsPNG([[0xffFF0000, 0xffFFFF00],
           [0xff00aa77, 0xff333333]], 'test_grid.png')

