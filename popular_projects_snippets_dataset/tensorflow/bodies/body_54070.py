# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py

class LeakedObjectTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(LeakedObjectTest, self).__init__(*args, **kwargs)
        self.accumulation = []

    @unittest.expectedFailure
    @test_util.assert_no_new_pyobjects_executing_eagerly
    def test_has_leak(self):
        self.accumulation.append([1.])

    @test_util.assert_no_new_pyobjects_executing_eagerly
    def test_has_no_leak(self):
        self.not_accumulating = [1.]

self.assertTrue(LeakedObjectTest("test_has_leak").run().wasSuccessful())
self.assertTrue(LeakedObjectTest("test_has_no_leak").run().wasSuccessful())
