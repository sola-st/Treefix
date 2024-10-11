# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
config = {
    'thresholds': self.init_thresholds,
    'top_k': self.top_k,
    'class_id': self.class_id
}
base_config = super(Precision, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
