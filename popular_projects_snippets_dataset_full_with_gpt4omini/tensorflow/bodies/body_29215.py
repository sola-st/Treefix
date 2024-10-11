# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/convert_test.py
resp = convert.optional_param_to_tensor("bar", "value", "default",
                                        dtypes.string)
self.assertEqual(compat.as_bytes("value"), self.evaluate(resp))
