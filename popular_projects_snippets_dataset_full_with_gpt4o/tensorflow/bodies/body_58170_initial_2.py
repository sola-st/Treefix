from types import SimpleNamespace # pragma: no cover
import numpy as np # pragma: no cover

UtilModifyIntegerQuantizedModelIOTypeTest = type('UtilModifyIntegerQuantizedModelIOTypeTest', (object,), {}) # pragma: no cover
cls = type('Mock', (object,), {'setUpClass': lambda: None, 'post_train_int8_model': None, 'post_train_int16_model': None}) # pragma: no cover
_generate_integer_tflite_model = lambda quantization_type=None: np.array([1, 2, 3]) # pragma: no cover
dtypes = SimpleNamespace(int16=np.int16) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util_test.py
from l3.Runtime import _l_
super(UtilModifyIntegerQuantizedModelIOTypeTest, cls).setUpClass()
_l_(21610)
cls.post_train_int8_model = _generate_integer_tflite_model()
_l_(21611)
cls.post_train_int16_model = _generate_integer_tflite_model(
    quantization_type=dtypes.int16)
_l_(21612)
