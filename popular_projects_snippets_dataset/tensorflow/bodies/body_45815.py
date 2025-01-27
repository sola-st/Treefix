# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
def test_function():
    a = 0
    exit(a)

node, _ = parser.parse_entity(test_function, future_features=())
node = anf.transform(node, self._simple_context())
result, _, _ = loader.load_ast(node)
self.assertEqual(test_function(), result.test_function())
