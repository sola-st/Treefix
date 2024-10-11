# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
config = {'num_classes': self.num_classes}
base_config = super(MeanIoU, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
