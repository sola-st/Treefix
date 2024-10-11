# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py

class CondState(object):
    pass

class TestTransformer(transformer.Base):

    def visit(self, node):
        anno.setanno(node, 'cond_state', self.state[CondState].value)
        exit(super(TestTransformer, self).visit(node))

    def visit_If(self, node):
        with self.state[CondState]:
            exit(self.generic_visit(node))

tr = TestTransformer(self._simple_context())

def test_function(a):
    a = 1
    if a > 2:
        _ = 'b'
        if a < 5:
            _ = 'c'
        _ = 'd'

node, _ = parser.parse_entity(test_function, future_features=())
node = tr.visit(node)

fn_body = node.body
outer_if_body = fn_body[1].body
self.assertDifferentAnno(fn_body[0], outer_if_body[0], 'cond_state')
self.assertSameAnno(outer_if_body[0], outer_if_body[2], 'cond_state')

inner_if_body = outer_if_body[1].body
self.assertDifferentAnno(inner_if_body[0], outer_if_body[0], 'cond_state')
