# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/integration_test/benchmarks/numpy_mlp.py
self.w1 = np.random.uniform(size=[input_size, hidden_units]).astype(
    np.float32, copy=False)
self.w2 = np.random.uniform(size=[hidden_units, num_classes]).astype(
    np.float32, copy=False)
self.b1 = np.random.uniform(size=[1, hidden_units]).astype(
    np.float32, copy=False)
self.b2 = np.random.uniform(size=[1, num_classes]).astype(
    np.float32, copy=False)
