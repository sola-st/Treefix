# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util_test.py
expected_node = gast.parse('({})'.format(expected_node_src)).body[0]
msg = 'AST did not match expected:\n{}\nActual:\n{}'.format(
    pretty_printer.fmt(expected_node),
    pretty_printer.fmt(actual_node))
self.assertTrue(ast_util.matches(actual_node, expected_node), msg)
