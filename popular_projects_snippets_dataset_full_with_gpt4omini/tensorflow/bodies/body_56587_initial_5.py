import zipfile # pragma: no cover
import os # pragma: no cover

FLAGS = type('MockFlags', (), {'export_zip_path': 'output.zip', 'file_directory': 'source_directory'})() # pragma: no cover
zipfile = type('MockZipFile', (object,), {'ZipFile': zipfile.ZipFile}) # pragma: no cover
os = type('MockOS', (object,), {'walk': os.walk, 'path': type('MockPath', (object,), {})()}) # pragma: no cover

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
