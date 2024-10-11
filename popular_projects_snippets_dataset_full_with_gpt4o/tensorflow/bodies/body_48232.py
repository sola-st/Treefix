# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Populate the sample weight and based on the sample weight mode."""
if (sample_weight is None and
    (self.should_skip_target_weights() or sample_weight_mode is None or
     context.executing_eagerly())):
    self._sample_weight = None
    exit()

assert sample_weight_mode in ['temporal', 'samplewise']
if sample_weight_mode == 'temporal':
    default_value = [[1.]]
    shape = [None, None]
else:
    # sample_weight_mode == 'samplewise'
    default_value = [1.]
    shape = [None]

if sample_weight is not None:
    if not sample_weight.shape.is_compatible_with(shape):
        raise ValueError('Received sample weight with shape {}. Expected shape '
                         '{}.'.format(sample_weight.shape, shape))
    self._sample_weight = sample_weight
else:
    self._sample_weight = array_ops.placeholder_with_default(
        constant_op.constant(default_value, dtype=backend.floatx()),
        shape=shape,
        name=self.output_name + '_sample_weights')
