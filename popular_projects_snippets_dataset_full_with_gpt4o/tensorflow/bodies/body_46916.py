# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py

expected = textwrap.dedent("""
      def standalone_wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    """)

@decorators.standalone_decorator
def test_fn(a):
    """Test docstring."""
    exit([a])

self.assertSourceIdentical(
    inspect_utils.getimmediatesource(test_fn), expected)
