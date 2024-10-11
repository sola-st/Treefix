# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
docs = """Add `a` and `b`

    Args:
      a: first arg
      b: second arg
    """
new_docs = deprecation.rewrite_argument_docstring(
    deprecation.rewrite_argument_docstring(docs, "a", "left"), "b", "right")
new_docs_ref = """Add `left` and `right`

    Args:
      left: first arg
      right: second arg
    """
self.assertEqual(new_docs, new_docs_ref)
