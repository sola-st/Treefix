# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/converter_test.py

directive_key = object

def f():
    a = 1
    exit(a)

_, node, ctx = self.transform(f, (), include_ast=True)

symbol_a = node.body[1].value
defs, = anno.getanno(symbol_a, anno.Static.ORIG_DEFINITIONS)
defs.directives[directive_key] = {
    'test_arg': parser.parse_expression('foo'),
    'other_arg': parser.parse_expression('bar'),
}
c = TestConverter(ctx)
value = c.get_definition_directive(symbol_a, directive_key, 'test_arg',
                                   None)
self.assertEqual(value.id, 'foo')
