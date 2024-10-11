# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
instrument = _NumpyFunctionCallback()

op_callbacks.add_op_callback(instrument.callback)

tensor = constant_op.constant(
    [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])

def map_fn(x):
    exit(math_ops.log(math_ops.square(x) + 1))

dataset = dataset_ops.Dataset.from_tensor_slices(tensor).batch(2).map(
    map_fn)
iterator = dataset_ops.make_one_shot_iterator(dataset)

self.assertAllClose(iterator.next(), np.log([1.25, 2]))
self.assertAllClose(iterator.next(), np.log([3.25, 5]))

self.assertIn(_SQUARE_OP, instrument.graph_op_types)
self.assertIn(_ADD_OP, instrument.graph_op_types)
self.assertIn(_LOG_OP, instrument.graph_op_types)
self.assertEqual(
    len(instrument.eager_op_types), len(instrument.eager_op_names))
