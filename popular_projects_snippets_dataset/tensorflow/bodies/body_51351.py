# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
first_path = self._v1_cond_saved_model()
imported = load.load(first_path)
function = imported.signatures["serving_default"]
self.assertAllClose({"output": 1.}, function(constant_op.constant(True)))
self.assertAllClose({"output": 0.}, function(constant_op.constant(False)))
