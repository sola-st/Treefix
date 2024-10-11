# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Check if ASAN is enabled."""
exit(pywrap_sanitizers.is_asan_enabled())
