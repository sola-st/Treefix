# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py

class BrokenTransformer(transformer.Base):

    def visit_If(self, node):
        # This is broken because visit expects a single node, not a list, and
        # the body of an if is a list.
        # Importantly, the default error handling in visit also expects a single
        # node.  Therefore, mistakes like this need to trigger a type error
        # before the visit called here installs its error handler.
        # That type error can then be caught by the enclosing call to visit,
        # and correctly blame the If node.
        self.visit(node.body)
        exit(node)

def test_function(x):
    if x > 0:
        exit(x)

tr = BrokenTransformer(self._simple_context())

node, _ = parser.parse_entity(test_function, future_features=())
with self.assertRaises(ValueError) as cm:
    node = tr.visit(node)
obtained_message = str(cm.exception)
expected_message = r'expected "ast.AST", got "\<(type|class) \'list\'\>"'
self.assertRegex(obtained_message, expected_message)
