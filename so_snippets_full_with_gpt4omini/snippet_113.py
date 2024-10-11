# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/678236/how-do-i-get-the-filename-without-the-extension-from-a-path-in-python
from l3.Runtime import _l_
try:
    import os
    _l_(1282)

except ImportError:
    pass

def get_file_name(path):
    _l_(1285)

    if not os.path.isdir(path):
        _l_(1284)

        aux = os.path.splitext(os.path.basename(path))[0].split(".")[0]
        _l_(1283)
        return aux


def get_file_extension(path):
    _l_(1295)

    extensions = []
    _l_(1286)
    copy_path = path
    _l_(1287)
    while True:
        _l_(1292)

        copy_path, result = os.path.splitext(copy_path)
        _l_(1288)
        if result != '':
            _l_(1291)

            extensions.append(result)
            _l_(1289)
        else:
            break
            _l_(1290)
    extensions.reverse()
    _l_(1293)
    aux = "".join(extensions)
    _l_(1294)
    return aux

