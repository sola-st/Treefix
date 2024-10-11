# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt = ragged_factory_ops.constant([[1, 2, 3], [4, 5], [], [6, 7, 8, 9]])
ds = dataset_ops.Dataset.from_tensor_slices(rt)
if context.executing_eagerly():
    for i, value in enumerate(ds):
        self.assertAllEqual(rt[i], value)
else:
    it = dataset_ops.make_one_shot_iterator(ds)
    out = it.get_next()
    with self.cached_session() as sess:
        for i in range(3):
            self.assertAllEqual(sess.run(rt[i]), out)
