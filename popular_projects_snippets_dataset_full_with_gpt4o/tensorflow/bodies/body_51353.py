# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
first_path = self._v1_while_saved_model()
imported = load.load(first_path)
function = imported.signatures["serving_default"]
self.assertAllClose({"output": 10}, function(constant_op.constant(4)))
self.assertAllClose({"output": 15}, function(constant_op.constant(5)))
