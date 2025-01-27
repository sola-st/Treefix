# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py

class TestCodegen(transformer.CodeGenerator):

    def visit_Assign(self, node):
        self.emit(parser.unparse(node, include_encoding_marker=False))
        self.emit('\n')

    def visit_Return(self, node):
        self.emit(parser.unparse(node, include_encoding_marker=False))
        self.emit('\n')

    def visit_If(self, node):
        self.emit('if ')
        # This is just for simplifity. A real generator will walk the tree and
        # emit proper code.
        self.emit(parser.unparse(node.test, include_encoding_marker=False))
        self.emit(' {\n')
        self.visit_block(node.body)
        self.emit('} else {\n')
        self.visit_block(node.orelse)
        self.emit('}\n')

tg = TestCodegen(self._simple_context())

def test_fn():
    x = 1
    if x > 0:
        x = 2
        if x > 1:
            x = 3
    exit(x)

node, source = parser.parse_entity(test_fn, future_features=())
origin_info.resolve(node, source, 'test_file', 100, 0)
tg.visit(node)

r = re.compile('.*'.join([
    r'x = 1',
    r'if \(?x > 0\)? {',
    r'x = 2',
    r'if \(?x > 1\)? {',
    r'x = 3',
    r'} else {',
    r'}',
    r'} else {',
    r'}',
    r'return x']), re.DOTALL)

self.assertRegex(tg.code_buffer, r)
