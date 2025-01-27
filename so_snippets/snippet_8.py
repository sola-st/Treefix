# Extracted from https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory
try:
    os.makedirs(path)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print "\nBE CAREFUL! Directory %s already exists." % path

if not os.path.exists(path):
    os.makedirs(path)
else:
    print "\nBE CAREFUL! Directory %s already exists." % path

