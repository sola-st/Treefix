# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py
defs = anno.getanno(node, anno.Static.DEFINITIONS)
self.assertEqual(len(defs), num)
for r in defs:
    self.assertIsInstance(r, reaching_definitions.Definition)
