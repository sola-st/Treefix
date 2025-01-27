# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
exit(np.any(np.isnan(tensor)) or np.any(np.isinf(tensor)))
