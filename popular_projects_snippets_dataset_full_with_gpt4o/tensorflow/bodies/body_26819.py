# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/optimization_test.py
input_t = array_ops.placeholder(dtypes.int32, (None, None, None, None))
dataset = dataset_ops.Dataset.from_tensor_slices(input_t)
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
dataset = dataset.with_options(options)
iterator = dataset_ops.make_initializable_iterator(dataset)
init_op = iterator.initializer
get_next = iterator.get_next()

with self.cached_session() as sess:
    sess.run(init_op, {input_t: np.ones([1, 512, 1024, 1025], np.int32)})
    self.evaluate(get_next)
