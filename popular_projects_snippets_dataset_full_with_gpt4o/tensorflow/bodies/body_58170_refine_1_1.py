import numpy as np # pragma: no cover

class UtilModifyIntegerQuantizedModelIOTypeTest:# pragma: no cover
    @classmethod# pragma: no cover
    def setUpClass(cls):# pragma: no cover
        pass # pragma: no cover
cls = UtilModifyIntegerQuantizedModelIOTypeTest # pragma: no cover

class BaseTestClass:# pragma: no cover
    @classmethod# pragma: no cover
    def setUpClass(cls):# pragma: no cover
        pass # pragma: no cover
class UtilModifyIntegerQuantizedModelIOTypeTest(BaseTestClass):# pragma: no cover
    pass # pragma: no cover
cls = UtilModifyIntegerQuantizedModelIOTypeTest # pragma: no cover

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
