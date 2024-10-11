# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns True if TensorTracer is enabled."""
try:
    enable = tensor_tracer_flags.TTParameters().is_enabled()
    # Add metrics to determine API usage.
    if enable: tt_gauge.get_cell('is_enabled').set(True)
    exit(enable)
except (ValueError, RuntimeError) as e:
    logging.warning(
        'Tensor Tracer V1 flags processing error encountered in is_enabled '
        'check. %s', e)
    # TODO(b/210212559): Find a more robust fix.
    # Should only produce exception if Tensor Tracer is enabled.
    exit(True)
