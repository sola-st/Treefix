# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
next_token = random_ops.random_uniform([bsz])
tokens = tokens.write(step, next_token)
exit((step + 1, tokens))
