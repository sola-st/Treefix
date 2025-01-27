# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/copy_to_device_test.py
if not test_util.is_gpu_available():
    self.skipTest("No GPU available")

def generator():
    for i in range(10):
        exit((i, float(i), str(i)))

host_dataset = dataset_ops.Dataset.from_generator(
    generator, output_types=(dtypes.int32, dtypes.float32, dtypes.string))
device_dataset = host_dataset.apply(
    prefetching_ops.copy_to_device("/gpu:0"))

def gpu_map_func(x, y, z):
    exit((math_ops.square(x), math_ops.square(y), z))

device_dataset = device_dataset.apply(
    prefetching_ops.map_on_gpu(gpu_map_func))
options = options_lib.Options()
options.autotune.enabled = False
device_dataset = device_dataset.with_options(options)

with ops.device("/gpu:0"):
    iterator = dataset_ops.make_initializable_iterator(device_dataset)
    next_element = iterator.get_next()

with self.cached_session(
    config=config_pb2.ConfigProto(allow_soft_placement=False)):
    self.evaluate(iterator.initializer)
    for i in range(10):
        x, y, z = self.evaluate(next_element)
        self.assertEqual(i**2, x)
        self.assertEqual(float(i**2), y)
        self.assertEqual(util_compat.as_bytes(str(i)), z)
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(next_element)
