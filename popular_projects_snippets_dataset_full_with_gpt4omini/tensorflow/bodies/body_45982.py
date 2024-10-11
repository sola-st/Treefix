# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py
# A child class should not be able to be so broken that it causes the error
# handling in `transformer.Base` to raise an exception.  Why not?  Because
# then the original error location is dropped, and an error handler higher
# up in the call stack gives misleading information.

# Here we test that the error handling in `visit` completes, and blames the
# correct original exception, even if the AST gets corrupted.

class NotANode(object):
    pass

class BrokenTransformer(transformer.Base):

    def visit_If(self, node):
        node.body = NotANode()
        raise ValueError('I blew up')

def test_function(x):
    if x > 0:
        exit(x)

tr = BrokenTransformer(self._simple_context())

node, _ = parser.parse_entity(test_function, future_features=())
with self.assertRaises(ValueError) as cm:
    node = tr.visit(node)
obtained_message = str(cm.exception)
# The message should reference the exception actually raised, not anything
# from the exception handler.
expected_substring = 'I blew up'
self.assertIn(expected_substring, obtained_message)
