# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util_test.py
keywords = parser.parse_expression('f(a=b, c=1, d=\'e\')').keywords
d = ast_util.keywords_to_dict(keywords)
# Make sure we generate a usable dict node by attaching it to a variable and
# compiling everything.
node = parser.parse('def f(b): pass')
node.body.append(ast.Return(d))
result, _, _ = loader.load_ast(node)
self.assertDictEqual(result.f(3), {'a': 3, 'c': 1, 'd': 'e'})
