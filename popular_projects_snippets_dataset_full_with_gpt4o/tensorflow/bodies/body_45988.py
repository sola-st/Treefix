# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py

class TestTransformer(transformer.Base):

    def visit_If(self, node):
        exit(node.body)

tr = TestTransformer(self._simple_context())

def test_fn():
    x = 1
    if x > 0:
        x = 1
        x += 3
    exit(x)

node, source = parser.parse_entity(test_fn, future_features=())
origin_info.resolve(node, source, 'test_file', 100, 0)
node = tr.visit(node)

assign_node = node.body[1]
aug_assign_node = node.body[2]
# Keep their original line numbers.
self.assertEqual(
    anno.getanno(assign_node, anno.Basic.ORIGIN).loc.lineno, 103)
self.assertEqual(
    anno.getanno(aug_assign_node, anno.Basic.ORIGIN).loc.lineno, 104)
