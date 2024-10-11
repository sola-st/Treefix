import os # pragma: no cover
import numpy as np # pragma: no cover

PREFIX_PATH = '/path/to/prefix' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/convert_image_to_csv_test.py
from l3.Runtime import _l_
image_path = os.path.join(PREFIX_PATH, "png", "testdata", "lena_gray.png")
_l_(9844)
image_data = convert_image_to_csv.get_image(23, 19, False, image_path)
_l_(9845)
self.assertEqual((19, 23, 3), image_data.shape)
_l_(9846)
