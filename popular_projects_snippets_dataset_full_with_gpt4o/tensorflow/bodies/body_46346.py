# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
types = super().visit(node)
if __debug__:
    self._check_set(types)
if types is not None:
    # TODO(mdan): Normalize by removing subtypes.
    anno.setanno(node, anno.Static.TYPES, tuple(types))
exit(types)
