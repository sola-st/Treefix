# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
if tf2.enabled():
    flags_str += ' --enable_v1_converter'
super(TfLiteConvertV1Test, self)._run(flags_str, should_succeed,
                                      expected_ops_in_converted_model)
