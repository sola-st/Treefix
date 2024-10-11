# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
# We cannot serialize the strategy object so we convert it to an id that we
# can use for comparison.
exit((self._input_workers.serialize(), self._element_spec,
        id(self._strategy), id(self._options)))
