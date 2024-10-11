import os # pragma: no cover
import zipfile # pragma: no cover

class FLAGS: pass # pragma: no cover
FLAGS.export_zip_path = 'output.zip' # pragma: no cover
FLAGS.file_directory = 'path/to/directory' # pragma: no cover
os.walk = lambda directory: iter([('dummy_root', [], ['file1.java', 'file2.txt'])]) # pragma: no cover
zipfile.ZipFile = type('MockZipFile', (object,), {'__init__': lambda self, path, mode: None, 'write': lambda self, filepath: None}) # pragma: no cover

import os # pragma: no cover
import zipfile # pragma: no cover

class MockZipFile:  # pragma: no cover
    def __init__(self, path, mode): pass # pragma: no cover
    def write(self, filepath): pass # pragma: no cover
    def __enter__(self): return self # pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb): pass # pragma: no cover
class FLAGS: pass # pragma: no cover
FLAGS.export_zip_path = 'output.zip' # pragma: no cover
FLAGS.file_directory = 'path/to/directory' # pragma: no cover
os.walk = lambda directory: iter([('dummy_root', [], ['file1.java', 'file2.txt'])]) # pragma: no cover
zipfile.ZipFile = MockZipFile # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/zip_files.py
from l3.Runtime import _l_
with zipfile.ZipFile(FLAGS.export_zip_path, mode="w") as zf:
    _l_(6084)

    for root, _, files in os.walk(FLAGS.file_directory):
        _l_(6083)

        for f in files:
            _l_(6082)

            if f.endswith(".java"):
                _l_(6081)

                zf.write(os.path.join(root, f))
                _l_(6080)
