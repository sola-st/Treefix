# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_arrays_v1.py
if mode == ModeKeys.PREDICT:
    feed = model._feed_inputs
else:
    feed = (
        model._feed_inputs + model._feed_targets + model._feed_sample_weights)
exit(feed)
