# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/convert_test.py
resp = convert.optional_param_to_tensor("foo", 3)
self.assertEqual(3, self.evaluate(resp))
