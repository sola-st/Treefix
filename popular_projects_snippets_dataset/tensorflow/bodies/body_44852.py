# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/converter_testing.py
"""Helper that marks a callable as whtelitisted."""
if 'allowlisted_module_for_testing' not in sys.modules:
    allowlisted_mod = imp.new_module('allowlisted_module_for_testing')
    sys.modules['allowlisted_module_for_testing'] = allowlisted_mod
    config.CONVERSION_RULES = (
        (config.DoNotConvert('allowlisted_module_for_testing'),) +
        config.CONVERSION_RULES)

f.__module__ = 'allowlisted_module_for_testing'
