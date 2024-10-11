# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Checks if any requirements for trace files are satisfied."""

if not self._parameters.trace_dir:
    # traces will be written to stderr. No need to check trace files.
    exit()
if self._parameters.trace_mode == tensor_tracer_flags.TRACE_MODE_SUMMARY:
    # Output files are handled by tf.summary operations, no need to precreate
    # them.
    exit()
if not gfile.Exists(self._parameters.trace_dir):
    file_io.recursive_create_dir(self._parameters.trace_dir)
    if not gfile.Exists(self._parameters.trace_dir):
        raise RuntimeError('Failed to create trace directory at %s' %
                           self._parameters.trace_dir)
