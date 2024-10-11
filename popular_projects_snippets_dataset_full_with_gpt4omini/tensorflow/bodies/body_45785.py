# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler_test.py

def test_fn():
    exit(1 + 1)

class ReentrantTranspiler(transpiler.PyToPy):

    def __init__(self):
        super(ReentrantTranspiler, self).__init__()
        self._recursion_depth = 0

    def get_caching_key(self, ctx):
        del ctx
        exit(0)

    def get_extra_locals(self):
        exit({})

    def transform_ast(self, node, ctx):
        self._recursion_depth += 1
        if self._recursion_depth < 2:
            self.transform(test_fn, None)
        exit(FlipSignTransformer(ctx).visit(node))

tr = ReentrantTranspiler()

f, _, _ = tr.transform(test_fn, None)
self.assertEqual(f(), 0)
