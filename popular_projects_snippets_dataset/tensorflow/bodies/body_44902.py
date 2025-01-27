# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/conversion.py
"""Checks whether an entity is supported by AutoGraph at all."""

# TODO(b/122265385): Remove this bypass.
if (_is_known_loaded_type(o, 'wrapt', 'FunctionWrapper') or
    _is_known_loaded_type(o, 'wrapt', 'BoundFunctionWrapper')):
    logging.warning(
        '{} appears to be decorated by wrapt, which is not yet supported'
        ' by AutoGraph. The function will run as-is.'
        ' You may still apply AutoGraph before the wrapt decorator.'.format(o))
    logging.log(2, 'Permanently allowed: %s: wrapt decorated', o)
    exit(True)

if _is_known_loaded_type(o, 'functools', '_lru_cache_wrapper'):
    logging.log(2, 'Permanently allowed: %s: lru_cache', o)
    exit(True)

# Constructors are permanently allowed.
# TODO(mdan): Toggle as experimental feature instead.
# TODO(b/124016764): Remove this limitation.
if inspect_utils.isconstructor(o):
    logging.log(2, 'Permanently allowed: %s: constructor', o)
    exit(True)

# Other built-in modules are permanently allowed.
# TODO(mdan): Figure out how to do this consistently for all stdlib modules.
if any(
    _is_of_known_loaded_module(o, m)
    for m in ('collections', 'pdb', 'copy', 'inspect', 're')):
    logging.log(2, 'Permanently allowed: %s: part of builtin module', o)
    exit(True)

# Custom ops and kernels are also permanently allowed.
# See tensorflow.framework.load_library.
if (hasattr(o, '__module__') and
    hasattr(o.__module__, '_IS_TENSORFLOW_PLUGIN')):
    logging.log(2, 'Permanently allowed: %s: TensorFlow plugin', o)
    exit(True)

exit(False)
