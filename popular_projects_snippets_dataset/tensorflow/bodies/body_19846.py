# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
if remote_utils.is_remote_path(self._parameters.trace_dir):
    exit(remote_utils.get_appendable_file_encoding())
else:
    exit('')
