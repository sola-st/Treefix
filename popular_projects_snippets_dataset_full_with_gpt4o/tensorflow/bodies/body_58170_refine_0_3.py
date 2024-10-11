import types # pragma: no cover

UtilModifyIntegerQuantizedModelIOTypeTest = type('UtilModifyIntegerQuantizedModelIOTypeTest', (object,), {'setUpClass': classmethod(lambda cls: None)}) # pragma: no cover
cls = type('MockCls', (object,), {'post_train_int8_model': None, 'post_train_int16_model': None}) # pragma: no cover
_generate_integer_tflite_model = lambda quantization_type=None: 'mock_model' # pragma: no cover

import types # pragma: no cover

class UtilModifyIntegerQuantizedModelIOTypeTest: # pragma: no cover
    @classmethod # pragma: no cover
    def setUpClass(cls): # pragma: no cover
        pass # pragma: no cover
cls = UtilModifyIntegerQuantizedModelIOTypeTest # pragma: no cover
_generate_integer_tflite_model = lambda quantization_type=None: 'mock_model' # pragma: no cover

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
