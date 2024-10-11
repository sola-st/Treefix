# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/converter_test.py

directive_key = object

def f():
    a = 1
    if a:
        a = 2
    exit(a)

_, node, ctx = self.transform(f, (), include_ast=True)

symbol_a = node.body[2].value
defs = anno.getanno(symbol_a, anno.Static.ORIG_DEFINITIONS)
defs[0].directives[directive_key] = {
    'test_arg': parser.parse_expression('foo'),
    'other_arg': parser.parse_expression('bar'),
}
defs[1].directives[directive_key] = {
    'test_arg': parser.parse_expression('foo'),
    'other_arg': parser.parse_expression('baz'),
}
c = TestConverter(ctx)
value = c.get_definition_directive(symbol_a, directive_key, 'test_arg',
                                   None)
self.assertEqual(value.id, 'foo')
