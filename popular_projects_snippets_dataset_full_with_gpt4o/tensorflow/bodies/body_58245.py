# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable.py
del self  # Temporarily removing self until parameter logic is implemented.
if model_hash and not model_path or not model_hash and model_path:
    raise ValueError('Both model metadata(model_hash, model_path) should be '
                     'given at the same time.')
if model_hash:
    # TODO(b/180400857): Create stub once the service is implemented.
    pass
