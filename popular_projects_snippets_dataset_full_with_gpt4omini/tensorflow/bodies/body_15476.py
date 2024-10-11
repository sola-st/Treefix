# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_tensor_op_test.py
random.seed(5)
for config in self.CONFIGS:
    self.run_benchmark(**config)
