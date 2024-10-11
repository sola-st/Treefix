def mock_get_crtimes_in_dir(directory, raise_on_error=True, as_epoch=False): # pragma: no cover
    try: # pragma: no cover
        files = os.listdir(directory) # pragma: no cover
        for file in files: # pragma: no cover
            path = os.path.join(directory, file) # pragma: no cover
            if os.path.isfile(path): # pragma: no cover
                creation_time = os.path.getctime(path) # pragma: no cover
                yield file, creation_time if as_epoch else datetime.fromtimestamp(creation_time) # pragma: no cover
    except Exception as e: # pragma: no cover
        if raise_on_error: # pragma: no cover
            raise e # pragma: no cover
        else: # pragma: no cover
            return # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/237079/how-do-i-get-file-creation-and-modification-date-times
from l3.Runtime import _l_
try:
    from crtime import get_crtimes_in_dir
    _l_(14595)

except ImportError:
    pass

for fname, date in get_crtimes_in_dir(".", raise_on_error=True, as_epoch=False):
    _l_(14597)

    print(fname, date)
    _l_(14596)

