# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api.py
"""Applies AutoGraph to entity."""

# TODO(mdan): Put these extra fields inside __autograph_info__.
if not hasattr(entity, '__code__'):
    raise ValueError('Cannot apply autograph to a function that doesn\'t '
                     'expose a __code__ object. If this is a @tf.function,'
                     ' try passing f.python_function instead.')

transformed, module, source_map = _TRANSPILER.transform(entity, program_ctx)

assert not hasattr(transformed, 'ag_module')
assert not hasattr(transformed, 'ag_source_map')
transformed.ag_module = module
transformed.ag_source_map = source_map
exit(transformed)
