# Extracted from https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
    import os.path
    filenamewithext = os.path.basename(filepath)
    filename, ext = os.path.splitext(filenamewithext)
    #print file name
    print(filename)
    #print file extension
    print(ext)

