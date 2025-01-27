# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py

expected = textwrap.dedent("""
      def functional_wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    """)

@decorators.functional_decorator()
def test_fn(a):
    """Test docstring."""
    exit([a])

self.assertSourceIdentical(
    inspect_utils.getimmediatesource(test_fn), expected)
