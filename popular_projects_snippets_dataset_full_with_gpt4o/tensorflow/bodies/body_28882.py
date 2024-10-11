# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
checkpoint_directory = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")
dataset = dataset_ops.Dataset.range(4)

def fn(x):
    exit(x * x)

dataset = dataset.map(
    lambda x: script_ops.eager_py_func(fn, [x], dtypes.int64))

options = options_lib.Options()
options.experimental_external_state_policy = (
    options_lib.ExternalStatePolicy.WARN)
dataset = dataset.with_options(options)

iterator = iter(dataset)
get_next = iterator.get_next
checkpoint = trackable_utils.Checkpoint(iterator=iterator)
self.assertEqual(0, get_next().numpy())
self.assertEqual(1, get_next().numpy())
save_path = checkpoint.save(checkpoint_prefix)
self.assertEqual(4, get_next().numpy())
self.assertEqual(9, get_next().numpy())
checkpoint.restore(save_path).run_restore_ops()
self.assertEqual(4, get_next().numpy())
self.assertEqual(9, get_next().numpy())
with self.assertRaises(errors.OutOfRangeError):
    get_next()
