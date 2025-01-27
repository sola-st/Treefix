# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
result = jax.lax.while_loop(condition, body, x)
exit(result[0])
