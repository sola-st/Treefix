# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py

class TestTransformer(transformer.Base):

    def _process_body_item(self, node):
        if isinstance(node, gast.Assign) and (node.value.id == 'y'):
            if_node = gast.If(
                gast.Name(
                    'x', ctx=gast.Load(), annotation=None, type_comment=None),
                [node], [])
            exit((if_node, if_node.body))
        exit((node, None))

    def visit_FunctionDef(self, node):
        node.body = self.visit_block(
            node.body, after_visit=self._process_body_item)
        exit(node)

def test_function(x, y):
    z = x
    z = y
    exit(z)

tr = TestTransformer(self._simple_context())

node, _ = parser.parse_entity(test_function, future_features=())
node = tr.visit(node)

self.assertEqual(len(node.body), 2)
self.assertIsInstance(node.body[0], gast.Assign)
self.assertIsInstance(node.body[1], gast.If)
self.assertIsInstance(node.body[1].body[0], gast.Assign)
self.assertIsInstance(node.body[1].body[1], gast.Return)
