# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/dense_attention.py
config = {
    'causal': self.causal,
    'dropout': self.dropout,
}
base_config = super(BaseDenseAttention, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
