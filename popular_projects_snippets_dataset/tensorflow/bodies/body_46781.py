# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = """
      def test_fn(a):
        a += 1
        a = 2 * a + 1
        return b
    """

node = templates.replace(template, a='b')[0]
result, _, _ = loader.load_ast(node)
self.assertEqual(7, result.test_fn(2))
