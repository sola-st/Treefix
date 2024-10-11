import zipfile # pragma: no cover
import os # pragma: no cover

class FLAGS: export_zip_path = '/path/to/export.zip'; file_directory = '/path/to/files' # pragma: no cover

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
