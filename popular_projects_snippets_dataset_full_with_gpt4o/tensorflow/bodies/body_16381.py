# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/template.py
exit(self._variables_in_scope(
    self._eager_variable_store.non_trainable_variables()))
