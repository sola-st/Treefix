# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
path = self._model_with_ragged_input()
imported = load.load(path)
imported_fn = imported.signatures["serving_default"]
x = ragged_factory_ops.constant([[10., 20.], [30.]])
result = imported_fn(x_component_0=x.values, x_component_1=x.row_splits)
self.assertAllEqual(result["y"], [[20., 40.], [60.]])
