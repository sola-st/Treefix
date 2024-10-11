# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""DEPRECATED TF 1.x ONLY."""
with self.scope():
    args = (input_iterator.get_next(),) if input_iterator is not None else ()
exit(self.run(fn, args=args))
