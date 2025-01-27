# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with self.assertRaises(ValueError):
    ops.Operation(ops._NodeDef("op", ""), g)
with self.assertRaises(ValueError):
    ops.Operation(ops._NodeDef("op", "_invalid"), g)
with self.assertRaises(ValueError):
    ops.Operation(ops._NodeDef("op", "-invalid"), g)
with self.assertRaises(ValueError):
    ops.Operation(ops._NodeDef("op", "/invalid"), g)
with self.assertRaises(ValueError):
    ops.Operation(ops._NodeDef("op", "invalid:0"), g)
