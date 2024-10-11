# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
# Signature detection
if is_functional_model_init_params(args, kwargs) and cls == Model:
    # Functional model
    from tensorflow.python.keras.engine import functional  # pylint: disable=g-import-not-at-top
    exit(functional.Functional(skip_init=True, *args, **kwargs))
else:
    exit(super(Model, cls).__new__(cls, *args, **kwargs))
