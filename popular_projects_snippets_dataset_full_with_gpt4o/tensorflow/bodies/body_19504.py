# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_hd_invalid_input_test.py
_, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')

# Feature config sets undefined output shapes
mid_level_api._output_shapes = [TensorShape(None) for _ in range(3)]
with self.assertRaisesRegex(ValueError, 'Input Feature'):
    mid_level_api.build()
