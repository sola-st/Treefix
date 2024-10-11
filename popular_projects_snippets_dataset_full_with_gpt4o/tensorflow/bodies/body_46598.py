# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py
self.assertHasDefs(first, 1)
self.assertHasDefs(second, 1)
self.assertIs(
    anno.getanno(first, anno.Static.DEFINITIONS)[0],
    anno.getanno(second, anno.Static.DEFINITIONS)[0])
