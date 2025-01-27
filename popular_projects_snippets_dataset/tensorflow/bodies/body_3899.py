# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/capture_container.py
values = nest.flatten(func())
exit([value for value in values if isinstance(value, core.Tensor)])
