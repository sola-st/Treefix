class MockCrtime:  # Mock class to simulate ImportError # pragma: no cover
    @staticmethod # pragma: no cover
    def get_crtimes_in_dir(path, raise_on_error=False, as_epoch=True): # pragma: no cover
        try: # pragma: no cover
            files = os.listdir(path) # pragma: no cover
            for file in files: # pragma: no cover
                timestamp = os.path.getctime(file) # pragma: no cover
                if not as_epoch: # pragma: no cover
                    timestamp = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') # pragma: no cover
                yield file, timestamp # pragma: no cover
        except Exception as e: # pragma: no cover
            if raise_on_error: # pragma: no cover
                raise e # pragma: no cover
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

