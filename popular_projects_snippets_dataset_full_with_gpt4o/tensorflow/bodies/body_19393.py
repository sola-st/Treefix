# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_invalid_input_test.py
self.skip_if_oss()
strategy, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')
# We aren't going to actually run anything, so the batch_size here does not
# matter.
mid_level_api.build(64)

# Test pass non tensor to apply_gradients.
@def_function.function
def test_apply_1():
    mid_level_api.apply_gradients((1, 2, 3))

with self.assertRaisesRegex(ValueError, 'found non-tensor type'):
    strategy.run(test_apply_1)

# Test pass different structure to apply_gradients.
@def_function.function
def test_apply_2():
    # This should be a tuple as feature_config is a tuple of 3 configs.
    mid_level_api.apply_gradients([1, 2, 3])

with self.assertRaisesRegex(
    TypeError, 'The two structures don\'t have the same nested structure.'):
    strategy.run(test_apply_2)
