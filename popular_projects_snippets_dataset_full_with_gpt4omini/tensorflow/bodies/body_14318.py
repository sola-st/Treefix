# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/integration_test/benchmarks/tf_numpy_mlp.py
self.w1 = np.random.uniform(size=[input_size, hidden_units]).astype(
    np.float32)
self.w2 = np.random.uniform(size=[hidden_units, num_classes]).astype(
    np.float32)
self.b1 = np.random.uniform(size=[1, hidden_units]).astype(
    np.float32)
self.b2 = np.random.uniform(size=[1, num_classes]).astype(
    np.float32)
