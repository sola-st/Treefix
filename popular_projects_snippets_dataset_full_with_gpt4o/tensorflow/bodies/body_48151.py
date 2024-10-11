# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
# Validate that arguments passed by the user to `compile` are supported by
# tf.distribute.Strategy.
if self._distribution_strategy:
    if sample_weight_mode:
        raise NotImplementedError('sample_weight_mode is not supported with '
                                  'tf.distribute.Strategy.')
    if weighted_metrics:
        raise NotImplementedError('weighted_metrics is not supported with '
                                  'tf.distribute.Strategy.')
    if target_tensors:
        raise ValueError('target_tensors is not supported with '
                         'tf.distribute.Strategy.')

    if run_eagerly:
        raise ValueError(
            'We currently do not support enabling `run_eagerly` with '
            'distribution strategy.')

    if (distributed_training_utils_v1.is_distributing_by_cloning(self) and
        (not self.built or not self.inputs or not self.outputs)):
        raise ValueError(
            'We currently do not support distribution strategy with a '
            '`Sequential` model that is created without `input_shape`/'
            '`input_dim` set in its first layer or a subclassed model.')
