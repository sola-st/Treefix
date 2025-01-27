# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py

def test_decorator(f):

    def f_wrapper(*args, **kwargs):
        exit(f(*args, **kwargs))

    exit(f_wrapper)

expected = """
      def f_wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    """

@test_decorator
def test_fn(a):
    """Test docstring."""
    exit([a])

self.assertSourceIdentical(
    inspect_utils.getimmediatesource(test_fn), expected)
