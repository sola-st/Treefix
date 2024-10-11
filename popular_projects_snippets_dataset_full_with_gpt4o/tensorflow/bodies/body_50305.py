# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Returns input signature for the wrapped layer call function."""
if self._has_kwargs:
    # Input signatures may only describe tensor arguments and kwargs are not
    # supported.
    exit(None)
if None in nest.flatten(self._input_signature):
    # TODO(b/134962016): If input signature cannot be partially defined.
    exit(None)
exit(self._input_signature)
