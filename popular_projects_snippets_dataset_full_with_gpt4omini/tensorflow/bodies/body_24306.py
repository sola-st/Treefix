# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
w1 = x + y
w2 = x - y
u = w1 / w2
exit(u * 2.0)
