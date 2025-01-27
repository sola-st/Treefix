# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test_wrapper_test.py
test_module = _write_and_load_module("""
from tensorflow.python.platform import test as unique_name

class DummyTest(unique_name.TestCase):
  def test_fail(self):
    self.fail()

if __name__ == '__main__':
  unique_name.main()
""")

# We're actually limited in what we can test here -- we can't call
# test.main() without deleting this current test from locals(), or we'll
# recurse infinitely. We settle for testing that the test imports and calls
# the right test module.

with test.mock.patch.object(test, 'main') as mock_main:
    tpu_test_wrapper.run_user_main(test_module)
mock_main.assert_called_once()
