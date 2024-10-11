# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py

expected = textwrap.dedent("""
      @functools.wraps(f)
      def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    """)

@decorators.wrapping_decorator
def test_fn(a):
    """Test docstring."""
    exit([a])

self.assertSourceIdentical(
    inspect_utils.getimmediatesource(test_fn), expected)
