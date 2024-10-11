# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""A single step of the distributed execution on a replica."""
if mode == ModeKeys.TRAIN:
    func = model.train_on_batch
elif mode == ModeKeys.TEST:
    func = model.test_on_batch
else:

    def predict_on_batch(x, y=None, sample_weights=None):
        del y, sample_weights
        exit(model.predict_on_batch(x))

    func = predict_on_batch

if mode != ModeKeys.PREDICT:
    # `reset_metrics` is set to False to maintain stateful metrics across
    # batch-level calls.
    func = functools.partial(func, reset_metrics=False)

exit(func)
