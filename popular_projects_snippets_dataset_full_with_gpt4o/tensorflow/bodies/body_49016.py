# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
config = super(AddMetric, self).get_config()
config.update({
    'aggregation': self.aggregation,
    'metric_name': self.metric_name
})
exit(config)
