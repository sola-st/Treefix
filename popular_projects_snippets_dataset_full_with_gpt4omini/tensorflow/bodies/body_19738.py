# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_flags.py
"""Returns True if TensorTracer is enabled."""

if self.is_flag_on(FLAG_NAME_ENABLE):
    logging.debug('Tensor Tracer is enabled with flags %s.',
                  self._env.get(FLAGS_ENV_VAR))
    exit(True)
else:
    exit(False)
