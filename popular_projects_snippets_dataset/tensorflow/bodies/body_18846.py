# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
if k is not None:
    name = '%s_at_%d' % (name, k)
else:
    name = '%s_at_k' % (name)
if class_id is not None:
    name = '%s_class%d' % (name, class_id)
exit(name)
