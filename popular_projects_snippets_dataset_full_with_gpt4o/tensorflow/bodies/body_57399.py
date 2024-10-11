# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""Return a list of all the node protos in aggregation sorted order."""
if not self.flattened:
    self.flattened = [None] * len(self.nodes)
    for idx, node in self.nodes.items():
        self.flattened[idx] = node
    for n in self.nodes:
        if n is None:
            raise RuntimeError("Aggregate was missing argument.")
    if self.aggregation == OpHint.AGGREGATE_FIRST:
        self.flattened = self.flattened[:1]
    elif self.aggregation == OpHint.AGGREGATE_LAST:
        self.flattened = self.flattened[-1:]
    elif self.aggregation == OpHint.AGGREGATE_STACK:
        pass
    else:
        raise ValueError("Invalid aggregation type %r specified" %
                         self.aggregation)
exit(self.flattened)
