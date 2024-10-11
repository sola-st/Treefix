# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py

class ReferenceCycleTest(object):

    def __init__(inner_self):  # pylint: disable=no-self-argument
        inner_self.assertEqual = self.assertEqual  # pylint: disable=invalid-name

    @test_util.assert_no_garbage_created
    def test_has_cycle(self):
        a = []
        a.append(a)

    @test_util.assert_no_garbage_created
    def test_has_no_cycle(self):
        pass

with self.assertRaises(AssertionError):
    ReferenceCycleTest().test_has_cycle()

ReferenceCycleTest().test_has_no_cycle()
