# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_function.py
"""A context manager setting current number of shards."""
if _current_tpu_context.number_of_shards is not None:
    raise NotImplementedError(
        "tpu_shard_context cannot be nested."
        "If you're using TPUEstimator with inference_on_tpu, "
        "make sure you have set "
        "export_saved_model_api_version=ExportSavedModelApiVersion.V2 in "
        "the creation of TPUEstimator.")
try:
    _current_tpu_context.set_number_of_shards(number_of_shards)
    exit()
finally:
    _current_tpu_context.set_number_of_shards(None)
