# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/678236/how-do-i-get-the-filename-without-the-extension-from-a-path-in-python
from l3.Runtime import _l_
try:
    import os
    _l_(12814)

except ImportError:
    pass

def get_file_name(path):
    _l_(12817)

    if not os.path.isdir(path):
        _l_(12816)

        aux = os.path.splitext(os.path.basename(path))[0].split(".")[0]
        _l_(12815)
        return aux


def get_file_extension(path):
    _l_(12827)

    extensions = []
    _l_(12818)
    copy_path = path
    _l_(12819)
    while True:
        _l_(12824)

        copy_path, result = os.path.splitext(copy_path)
        _l_(12820)
        if result != '':
            _l_(12823)

            extensions.append(result)
            _l_(12821)
        else:
            break
            _l_(12822)
    extensions.reverse()
    _l_(12825)
    aux = "".join(extensions)
    _l_(12826)
    return aux

