# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Check if TSAN is enabled."""
exit(pywrap_sanitizers.is_tsan_enabled())
