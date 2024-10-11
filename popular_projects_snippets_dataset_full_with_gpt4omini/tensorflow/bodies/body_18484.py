# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
# TODO(agarwal): consider looking if this is a Tile op then get its input.
# This may avoid running the Tile operations.
exit(array_ops.gather(value, 0))
