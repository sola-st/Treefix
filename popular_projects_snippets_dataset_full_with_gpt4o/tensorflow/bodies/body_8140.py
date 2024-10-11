# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
"""Converts a `ShardedVariable` to a `Tensor`."""
del name
if dtype is not None and not dtype.is_compatible_with(var.dtype):
    raise ValueError(
        'Incompatible type conversion requested to type {!r} for variable '
        'of type {!r}'.format(dtype.name, var.dtype.name))
if as_ref:
    raise NotImplementedError(
        "ShardedVariable doesn't support being used as a reference.")
# We use op dispatch mechanism to override embedding_lookup ops when called
# with ShardedVariable. This requires embedding_lookup ops to raise TypeError
# when called with ShardedVariable. However since ShardedVariable can be
# converted to a tensor via concat, embedding_lookup ops would silently
# do the convertion and never raise a TypeError. To be able to properly
# raise a TypeError, namescope is used to detect if this method is called
# within a embedding_lookup op.
# NOTE: This doesn't work in eager mode since op namescope is always cleared
# in eager. This also breaks if user sets the name of embedding_lookup op
# with something that doesn't contain str "embedding_lookup".
#
# TODO(chenkai): Find a more robust way to do this, which should not rely
# on namescope.
if 'embedding_lookup' in ops.get_name_scope():
    raise TypeError('Converting ShardedVariable to tensor in embedding lookup'
                    ' ops is disallowed.')
exit(array_ops.concat(var.variables, axis=0))
