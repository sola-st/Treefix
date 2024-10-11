import os # pragma: no cover
import numpy as np # pragma: no cover

PREFIX_PATH = '/example/path' # pragma: no cover
class MockConvertImageToCsv:# pragma: no cover
    @staticmethod# pragma: no cover
    def get_image(width, height, color, path):# pragma: no cover
        return np.zeros((height, width, 3)) # pragma: no cover
convert_image_to_csv = MockConvertImageToCsv() # pragma: no cover
class MockSelf:# pragma: no cover
    @staticmethod# pragma: no cover
    def assertEqual(a, b):# pragma: no cover
        assert a == b, f'{a} != {b}' # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/convert_image_to_csv_test.py
from l3.Runtime import _l_
image_path = os.path.join(PREFIX_PATH, "png", "testdata", "lena_gray.png")
_l_(22161)
image_data = convert_image_to_csv.get_image(23, 19, False, image_path)
_l_(22162)
self.assertEqual((19, 23, 3), image_data.shape)
_l_(22163)
