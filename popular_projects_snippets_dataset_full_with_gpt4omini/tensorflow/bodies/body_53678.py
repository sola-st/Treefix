# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Check if UBSAN is enabled."""
exit(pywrap_sanitizers.is_ubsan_enabled())
