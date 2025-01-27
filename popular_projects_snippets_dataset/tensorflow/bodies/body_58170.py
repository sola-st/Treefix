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
