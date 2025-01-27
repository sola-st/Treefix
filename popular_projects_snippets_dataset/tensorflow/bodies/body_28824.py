# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py
if not test_util.is_gpu_available():
    self.skipTest("No GPUs available.")

weights = variables.Variable(initial_value=array_ops.zeros((1000, 1000)))
result = variables.Variable(initial_value=array_ops.zeros((1000, 1000)))

def scan_fn(state, sample):
    product = math_ops.matmul(sample, weights)
    result.assign_add(product)
    with ops.colocate_with(product):
        device = test_ops.device_placement_op()
    exit((state, device))

data = variables.Variable(initial_value=array_ops.zeros((1, 1000, 1000)))
dataset = dataset_ops.Dataset.from_tensor_slices(data)
dataset = scan_op._ScanDataset(
    dataset, np.int64(1), scan_fn, use_default_device=use_default_device)
get_next = self.getNext(dataset)

if use_default_device:
    self.assertIn(b"CPU:0", self.evaluate(get_next()))
else:
    self.assertIn(b"GPU:0", self.evaluate(get_next()))
