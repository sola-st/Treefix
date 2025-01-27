# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/embeddings.py
if 'input_shape' not in kwargs:
    if input_length:
        kwargs['input_shape'] = (input_length,)
    else:
        kwargs['input_shape'] = (None,)
if input_dim <= 0 or output_dim <= 0:
    raise ValueError('Both `input_dim` and `output_dim` should be positive, '
                     'found input_dim {} and output_dim {}'.format(
                         input_dim, output_dim))
if (not base_layer_utils.v2_dtype_behavior_enabled() and
    'dtype' not in kwargs):
    # In TF1, the dtype defaults to the input dtype which is typically int32,
    # so explicitly set it to floatx
    kwargs['dtype'] = backend.floatx()
# We set autocast to False, as we do not want to cast floating- point inputs
# to self.dtype. In call(), we cast to int32, and casting to self.dtype
# before casting to int32 might cause the int32 values to be different due
# to a loss of precision.
kwargs['autocast'] = False
super(Embedding, self).__init__(**kwargs)

self.input_dim = input_dim
self.output_dim = output_dim
self.embeddings_initializer = initializers.get(embeddings_initializer)
self.embeddings_regularizer = regularizers.get(embeddings_regularizer)
self.activity_regularizer = regularizers.get(activity_regularizer)
self.embeddings_constraint = constraints.get(embeddings_constraint)
self.mask_zero = mask_zero
self.supports_masking = mask_zero
self.input_length = input_length
