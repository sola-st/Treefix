# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
exit((any(tensor is t for t in inputs) and
        any(tensor is t for t in outputs)))
