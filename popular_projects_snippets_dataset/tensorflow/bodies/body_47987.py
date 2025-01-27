# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/dense_attention.py
super(BaseDenseAttention, self).__init__(**kwargs)
self.causal = causal
self.dropout = dropout
self.supports_masking = True
