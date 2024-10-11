# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Check if MSAN is enabled."""
exit(pywrap_sanitizers.is_msan_enabled())
