# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
# Testing the code bodies only.  Wrapping them in functions so the
# syntax highlights nicely, but Python doesn't try to execute the
# statements.
node, _ = parser.parse_entity(test_fn, future_features=())
orig_source = parser.unparse(node, indentation='  ')
orig_str = textwrap.dedent(orig_source).strip()
config = [(anf.ANY, anf.LEAVE)]  # Configuration to transform nothing
node = anf.transform(node, self._simple_context(), config=config)
new_source = parser.unparse(node, indentation='  ')
new_str = textwrap.dedent(new_source).strip()
self.assertEqual(orig_str, new_str)
