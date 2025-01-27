# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/converter_test.py

directive_key = object

def f():
    a = 1
    exit(a)

_, node, ctx = self.transform(f, (), include_ast=True)

symbol_a = node.body[1].value
c = TestConverter(ctx)
value = c.get_definition_directive(symbol_a, directive_key, 'test_arg',
                                   parser.parse_expression('default'))
self.assertEqual(value.id, 'default')
