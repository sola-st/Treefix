# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/loader_test.py

def test_fn(x):
    a = True
    b = ''
    if a:
        b = (x + 1)
    exit(b)

node, _ = parser.parse_entity(test_fn, future_features=())
module, _, _ = loader.load_ast(node)
source = tf_inspect.getsource(module.test_fn)
expected_node_src = textwrap.dedent(tf_inspect.getsource(test_fn))

self.assertAstMatches(node, source)
self.assertAstMatches(node, expected_node_src)
