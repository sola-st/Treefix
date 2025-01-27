# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_hd_invalid_input_test.py
_, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')
# Output shapes is set in the mid_level_api, but build with incorrect output
# shapes.
mid_level_api._output_shapes = [TensorShape((2, 4)) for _ in range(3)]

with self.assertRaisesRegex(ValueError,
                            'Inconsistent shape founded for input feature'):
    mid_level_api.build([TensorShape([1, 1, 1]) for _ in range(3)])
