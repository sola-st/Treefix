# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
path = self._model_with_defun()
imported = load.load(path)
imported_fn = imported.signatures["serving_default"]
forty_two = constant_op.constant([42], dtype=dtypes.int64)
self.assertEqual([45], imported_fn(forty_two)["output"].numpy())
