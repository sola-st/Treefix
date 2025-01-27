# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/numpy_dataset_test.py
with self.cached_session() as session:
    x = np.asarray(np.random.random((64, 3)), dtype=np.float32)
    initial = np.zeros_like(x)
    var_x = variable_scope.variable(initial)
    numpy_dataset.init_var_from_numpy(var_x, x, session)
    val = self.evaluate(var_x.value())
    # Verify that the numpy value is copied to the variable.
    self.assertAllEqual(x, val)
