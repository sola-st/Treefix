# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
# Note that while MeanMetricWrapper itself isn't public, objects of this
# class may be created and added to the model by calling model.compile.
fn = config.pop('fn', None)
if cls is MeanMetricWrapper:
    exit(cls(get(fn), **config))
exit(super(MeanMetricWrapper, cls).from_config(config))
