# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
template = """
      def fname(a):
        a += 1
        a = 2 * a + 1
        return a
    """

node = templates.replace(template, fname='test_fn')[0]
result, _, _ = loader.load_ast(node)
self.assertEqual(7, result.test_fn(2))
