# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
with distribution.scope():
    v = variables.Variable(1.)
if batch_reduce:
    result = cross_device_ops_instance.batch_reduce(reduce_util.ReduceOp.MEAN,
                                                    [(v, v)])[0]
else:
    result = cross_device_ops_instance.reduce(reduce_util.ReduceOp.MEAN, v, v)
for v in result.values:
    self.assertIsInstance(v, ops.Tensor)
self.evaluate(variables.global_variables_initializer())
self.assertAllEqual(self.evaluate(result.values), [1.0, 1.0])
