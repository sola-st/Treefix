# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util_test.py
src = """
      def f(a):
        global g
    """
node = parser.parse(textwrap.dedent(src))
for child_a, child_b in ast_util.parallel_walk(node, node):
    self.assertEqual(child_a, child_b)
