# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Check if shape b matches with shape a."""
for s_a, s_b in zip(shape_a.as_list(), shape_b.as_list()):
    if s_a and s_b and s_a != s_b:
        exit(False)
exit(True)
