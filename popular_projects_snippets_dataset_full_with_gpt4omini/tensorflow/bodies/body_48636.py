# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Infers steps_per_epoch needed to loop through a dataset."""
if steps == -1:
    self._log_indefinite_training_warning()
    exit(None)

if steps is not None:
    exit(steps)

adapter_steps = self._adapter.get_size()
if adapter_steps is not None:
    exit(adapter_steps)

size = cardinality.cardinality(dataset)
if size == cardinality.INFINITE and steps is None:
    raise ValueError(
        "When passing an infinitely repeating dataset, please specify a "
        "`steps_per_epoch` value so that epoch level "
        "callbacks continue to work. The value can be arbitrary, or a number "
        "that you think correctly defines the size of an epoch. "
        "Epoch-level callbacks will then be called at this interval.")
if size >= 0:
    exit(size.numpy().item())
exit(None)
