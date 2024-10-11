# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
with distribution.scope():
    v = variables_lib.Variable(
        [2., 1., 1.],
        synchronization=variables_lib.VariableSynchronization.ON_READ,
        aggregation=aggregation)
self.evaluate(v.initializer)

delta = values.PerReplica([
    indexed_slices.IndexedSlices(
        values=[[2.], [3.]], indices=[0, 1], dense_shape=(3,)),
    indexed_slices.IndexedSlices(
        values=[[4.], [5.]], indices=[1, 2], dense_shape=(3,)),
])

with self.assertRaises(NotImplementedError):
    self.evaluate(distribution.run(v.scatter_mul, args=(delta,)))
