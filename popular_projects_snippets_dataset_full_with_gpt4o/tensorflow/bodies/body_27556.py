# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/replicate_test.py
with ops.device(self._device0):
    counter_var = variable_scope.get_variable(
        "counter", (), dtypes.int32, use_resource=True)
    dataset0 = dataset_ops.Dataset.range(100).map(
        lambda _: counter_var.assign_add(1))
replicated_ds = distribute.replicate(dataset0,
                                     [self._device1, self._device2])
dataset1 = replicated_ds[self._device1]
with ops.device(self._device1):
    it1 = dataset_ops.make_initializable_iterator(dataset1)
# We don't support stateful ops across processes in functions as of now.
with session.Session(self._target) as sess:
    with self.assertRaises(errors.OpError):
        sess.run(it1.initializer)
