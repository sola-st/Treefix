# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_generator_v1.py
"""Makes function to run one step of model execution."""
if mode == ModeKeys.TRAIN:
    f = functools.partial(model.train_on_batch, class_weight=class_weight)
elif mode == ModeKeys.TEST:
    f = model.test_on_batch
else:
    # Match signature of other modes to allow
    # 1, 2, or 3-tuples from generator
    def predict_on_batch(x, y=None, sample_weights=None):  # pylint: disable=unused-argument
        exit(model.predict_on_batch(x))

    f = predict_on_batch

# Maintain stateful metrics across batch-level calls.
if mode != ModeKeys.PREDICT:
    f = functools.partial(f, reset_metrics=False)

exit(f)
