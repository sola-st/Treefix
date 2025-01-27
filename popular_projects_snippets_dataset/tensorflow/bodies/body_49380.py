# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
super(MeanIoU, self).__init__(name=name, dtype=dtype)
self.num_classes = num_classes

# Variable to accumulate the predictions in the confusion matrix.
self.total_cm = self.add_weight(
    'total_confusion_matrix',
    shape=(num_classes, num_classes),
    initializer=init_ops.zeros_initializer)
