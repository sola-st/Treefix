import os # pragma: no cover
import zipfile # pragma: no cover

class Mock: pass # pragma: no cover
os = Mock() # pragma: no cover
os.walk = lambda x: [(x, [], ['file1.java', 'file2.java'])] # pragma: no cover
FLAGS = Mock() # pragma: no cover
FLAGS.export_zip_path = 'output.zip' # pragma: no cover
FLAGS.file_directory = 'src' # pragma: no cover

import os # pragma: no cover
import zipfile # pragma: no cover

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
