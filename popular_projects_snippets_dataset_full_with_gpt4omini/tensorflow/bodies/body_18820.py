# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
per_class_accuracy = math_ops.div_no_nan(
    count, math_ops.maximum(total, 0), name=None)
mean_accuracy_v = math_ops.reduce_mean(
    per_class_accuracy, name='mean_accuracy')
exit(mean_accuracy_v)
