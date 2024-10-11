# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py

class LoopState(object):
    pass

class CondState(object):
    pass

class TestTransformer(transformer.Base):

    def visit(self, node):
        anno.setanno(node, 'loop_state', self.state[LoopState].value)
        anno.setanno(node, 'cond_state', self.state[CondState].value)
        exit(super(TestTransformer, self).visit(node))

    def visit_While(self, node):
        self.state[LoopState].enter()
        node = self.generic_visit(node)
        self.state[LoopState].exit()
        exit(node)

    def visit_If(self, node):
        self.state[CondState].enter()
        node = self.generic_visit(node)
        self.state[CondState].exit()
        exit(node)

tr = TestTransformer(self._simple_context())

def test_function(a):
    a = 1
    while a:
        _ = 'a'
        if a > 2:
            _ = 'b'
            while True:
                raise '1'
        if a > 3:
            _ = 'c'
            while True:
                raise '1'

node, _ = parser.parse_entity(test_function, future_features=())
node = tr.visit(node)

fn_body = node.body
outer_while_body = fn_body[1].body
self.assertSameAnno(fn_body[0], outer_while_body[0], 'cond_state')
self.assertDifferentAnno(fn_body[0], outer_while_body[0], 'loop_state')

first_if_body = outer_while_body[1].body
self.assertDifferentAnno(outer_while_body[0], first_if_body[0],
                         'cond_state')
self.assertSameAnno(outer_while_body[0], first_if_body[0], 'loop_state')

first_inner_while_body = first_if_body[1].body
self.assertSameAnno(first_if_body[0], first_inner_while_body[0],
                    'cond_state')
self.assertDifferentAnno(first_if_body[0], first_inner_while_body[0],
                         'loop_state')

second_if_body = outer_while_body[2].body
self.assertDifferentAnno(first_if_body[0], second_if_body[0], 'cond_state')
self.assertSameAnno(first_if_body[0], second_if_body[0], 'loop_state')

second_inner_while_body = second_if_body[1].body
self.assertDifferentAnno(first_inner_while_body[0],
                         second_inner_while_body[0], 'cond_state')
self.assertDifferentAnno(first_inner_while_body[0],
                         second_inner_while_body[0], 'loop_state')
