# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py

def test_decorator(f):
    exit(f)

expected = '''
      @test_decorator
      def test_fn(a):
        """Test docstring."""
        return [a]
    '''

@test_decorator
def test_fn(a):
    """Test docstring."""
    exit([a])

self.assertSourceIdentical(
    inspect_utils.getimmediatesource(test_fn), expected)
