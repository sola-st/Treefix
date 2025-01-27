# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py

class LeakedTensorTest(object):

    def __init__(inner_self):  # pylint: disable=no-self-argument
        inner_self.assertEqual = self.assertEqual  # pylint: disable=invalid-name

    @test_util.assert_no_new_tensors
    def test_has_leak(self):
        self.a = constant_op.constant([3.], name="leak")

    @test_util.assert_no_new_tensors
    def test_has_no_leak(self):
        constant_op.constant([3.], name="no-leak")

with self.assertRaisesRegex(AssertionError, "Tensors not deallocated"):
    LeakedTensorTest().test_has_leak()

LeakedTensorTest().test_has_no_leak()
