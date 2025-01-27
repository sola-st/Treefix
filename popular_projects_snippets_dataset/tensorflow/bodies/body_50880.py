# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_serialization.py
"""Creates an object containing `signatures`."""
signature_map = _SignatureMap()
for name, func in signatures.items():
    # This true of any signature that came from canonicalize_signatures. Here as
    # a sanity check on saving; crashing on load (e.g. in _add_signature) would
    # be more problematic in case future export changes violated these
    # assertions.
    assert isinstance(func, defun.ConcreteFunction)
    assert isinstance(func.structured_outputs, collections_abc.Mapping)
    # pylint: disable=protected-access
    if len(func._arg_keywords) == 1:
        assert 1 == func._num_positional_args
    else:
        assert 0 == func._num_positional_args
    signature_map._add_signature(name, func)
    # pylint: enable=protected-access
exit(signature_map)
