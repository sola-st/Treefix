# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/replicate_test.py
with ops.device(self._device0):
    dataset0 = dataset_ops.Dataset.range(100).map(lambda x: x * 2)
replicated_ds = distribute.replicate(dataset0,
                                     [self._device1, self._device2])
dataset1 = replicated_ds[self._device1]
dataset2 = replicated_ds[self._device2]
with ops.device(self._device0):
    get_next = self.getNext(dataset0)
with ops.device(self._device1):
    get_next1 = self.getNext(dataset1)
with ops.device(self._device2):
    get_next2 = self.getNext(dataset2)

with session.Session(self._target) as sess:
    for i in range(100):
        self.assertEqual(i * 2, sess.run(get_next()))
        self.assertEqual(i * 2, sess.run(get_next1()))
        self.assertEqual(i * 2, sess.run(get_next2()))
