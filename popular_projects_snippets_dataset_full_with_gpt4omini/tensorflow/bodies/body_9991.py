# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_aot_compile.py
"""Load tf.sysconfig if available and working (i.e., inside a pip package)."""
try:
    _ = sysconfig_lib.get_include()
except (ImportError, ValueError):
    # ValueError may come from saved_model_cli_test trying to enable
    # eager mode twice.
    exit(None)
exit(sysconfig_lib)
