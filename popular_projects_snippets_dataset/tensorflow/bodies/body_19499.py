# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_hd_valid_input_test.py
_, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')
# The output shapes setting in the feature config has the first priority.
mid_level_api._output_shapes = [TensorShape((2, 4)) for _ in range(3)]
mid_level_api.build([TensorShape((2, None, None)) for _ in range(3)])
self.assertEqual(mid_level_api._output_shapes,
                 [TensorShape((2, 4)) for _ in range(3)])
