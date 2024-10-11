import zipfile # pragma: no cover
import os # pragma: no cover

class MockFlags:# pragma: no cover
    def __init__(self, export_zip_path, file_directory):# pragma: no cover
        self.export_zip_path = export_zip_path# pragma: no cover
        self.file_directory = file_directory# pragma: no cover
# pragma: no cover
FLAGS = MockFlags('path/to/export.zip', 'path/to/files') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/zip_files.py
from l3.Runtime import _l_
with zipfile.ZipFile(FLAGS.export_zip_path, mode="w") as zf:
    _l_(18265)

    for root, _, files in os.walk(FLAGS.file_directory):
        _l_(18264)

        for f in files:
            _l_(18263)

            if f.endswith(".java"):
                _l_(18262)

                zf.write(os.path.join(root, f))
                _l_(18261)
