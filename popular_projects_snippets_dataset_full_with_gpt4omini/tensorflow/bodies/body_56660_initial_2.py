import os # pragma: no cover
import numpy as np # pragma: no cover
class Mock: pass # pragma: no cover
def mock_get_image(a, b, c, d): return np.zeros((b, a, 3)) # pragma: no cover

PREFIX_PATH = '/usr/local/data' # pragma: no cover
convert_image_to_csv = type('Mock', (), {'get_image': mock_get_image})() # pragma: no cover
self = type('Mock', (), {'assertEqual': lambda self, a, b: print('Assertions match' if a == b else 'Assertions do not match')})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/convert_image_to_csv_test.py
from l3.Runtime import _l_
image_path = os.path.join(PREFIX_PATH, "png", "testdata", "lena_gray.png")
_l_(9844)
image_data = convert_image_to_csv.get_image(23, 19, False, image_path)
_l_(9845)
self.assertEqual((19, 23, 3), image_data.shape)
_l_(9846)
