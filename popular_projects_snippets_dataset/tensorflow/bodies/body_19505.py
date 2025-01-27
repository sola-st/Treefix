# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_hd_invalid_input_test.py
_, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')

# Build with undefined output shape
with self.assertRaisesRegex(ValueError, 'Input Feature'):
    mid_level_api.build([TensorShape([1, None, None]) for _ in range(3)])
