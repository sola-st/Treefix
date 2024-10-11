# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = """
      def test_fn(a, c):
        return b,
    """

node = templates.replace(template, b=('a', 'c'))[0]
result, _, _ = loader.load_ast(node)

self.assertEqual((2, 3), result.test_fn(2, 3))
