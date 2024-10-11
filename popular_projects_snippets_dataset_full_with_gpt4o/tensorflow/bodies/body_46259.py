# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py

class TestClass(object):

    def __init__(self, a):
        self.b = a
        self.b.c = 1

node, _ = self._parse_and_analyze(TestClass)
init_node = node.body[0]
self.assertScopeIs(
    anno.getanno(init_node, NodeAnno.BODY_SCOPE), ('self', 'a', 'self.b'),
    ('self', 'self.b', 'self.b.c'))
