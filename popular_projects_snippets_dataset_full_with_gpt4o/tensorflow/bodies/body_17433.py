# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
alias_id = signature_context.alias_global_id(self._handle._id)  # pylint:disable=protected-access
# TODO(xjun): Create variable placeholders directly from VariableSpec
# without using original values.
signature_context.add_placeholder(alias_id, self)
exit(VariableSpec(shape=self.shape,
                    dtype=self.dtype,
                    trainable=self.trainable,
                    alias_id=alias_id))
