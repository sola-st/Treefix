# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/replicate_test.py
with ops.device(self._device0):
    dataset0 = dataset_ops.Dataset.range(100).map(
        lambda _: random_ops.random_uniform(  # pylint:disable=g-long-lambda
            [],
            minval=1,
            maxval=10,
            dtype=dtypes.float32))
    opt = options_lib.Options()
    opt.experimental_external_state_policy = (
        options_lib.ExternalStatePolicy.FAIL)
    dataset0 = dataset0.with_options(opt)
with self.assertRaises(errors.FailedPreconditionError):
    replicated_ds = distribute.replicate(dataset0,
                                         [self._device1, self._device2])
    dataset1 = replicated_ds[self._device1]
    dataset2 = replicated_ds[self._device2]

    with ops.device(self._device0):
        get_next0 = self.getNext(dataset0)
    with ops.device(self._device1):
        get_next1 = self.getNext(dataset1)
    with ops.device(self._device2):
        get_next2 = self.getNext(dataset2)

    for _ in range(100):
        self.evaluate(get_next0())
        self.evaluate(get_next1())
        self.evaluate(get_next2())
