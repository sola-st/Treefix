# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
# Optional.get_value raises InvalidArgumentError when there's no value,
# so we need to call GetNext to raise EOFError.
exit(self._get_next_no_partial_batch_handling())
