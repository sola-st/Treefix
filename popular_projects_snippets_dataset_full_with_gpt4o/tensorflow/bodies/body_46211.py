# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util_test.py
node_1 = parser.parse(
    textwrap.dedent("""
      def f(a):
        return a + 1
    """))
node_2 = parser.parse(
    textwrap.dedent("""
      def f(a):
        return a + (a * 2)
    """))
node_3 = parser.parse(
    textwrap.dedent("""
      def f(a):
        return a + 2
    """))
with self.assertRaises(ValueError):
    for _ in ast_util.parallel_walk(node_1, node_2):
        pass
    # There is not particular reason to reject trees that differ only in the
    # value of a constant.
    # TODO(mdan): This should probably be allowed.
with self.assertRaises(ValueError):
    for _ in ast_util.parallel_walk(node_1, node_3):
        pass
