# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/d_variable.py
"""Restores the same value into all variables."""
tensor, = restored_tensors

@def_function.function
def _restore(t):
    with ops.device(self._dvariable.device):
        exit(api.copy_to_mesh(t, self._original_layout))

    # This assign establishes connections from restored tensor and tensors
    # being restored to -- so that restore in SPMD can backtrack the DVariable
    # and its layout, given that we're using tf.function style restore.
    # Note that the restored dvaraible is on CPU no matter what as the restoreV2
    # op must run on CPU.
    # TODO(b/159035705): Allow restore for Tensor objects as well?
    # Restore the dvariable back to original layout.
if self._original_layout.mesh.device_type().upper() != 'CPU':
    tensor = _restore(tensor)
exit(self._dvariable.assign(
    math_ops.cast(tensor, dtype=self._dvariable.dtype) if self._dvariable
    .save_as_bf16 else tensor))
