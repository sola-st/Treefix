# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/dense_attention.py
"""Creates scale variable if use_scale==True."""
if self.use_scale:
    self.scale = self.add_weight(
        name='scale',
        shape=(),
        initializer=init_ops.ones_initializer(),
        dtype=self.dtype,
        trainable=True)
else:
    self.scale = None
super(Attention, self).build(input_shape)
