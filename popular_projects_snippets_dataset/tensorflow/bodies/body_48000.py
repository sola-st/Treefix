# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/dense_attention.py
v_shape = tensor_shape.TensorShape(input_shape[1])
dim = v_shape[-1]
if isinstance(dim, tensor_shape.Dimension):
    dim = dim.value
if self.use_scale:
    self.scale = self.add_weight(
        name='scale',
        shape=[dim],
        initializer=init_ops.glorot_uniform_initializer(),
        dtype=self.dtype,
        trainable=True)
else:
    self.scale = None
super(AdditiveAttention, self).build(input_shape)
