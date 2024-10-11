# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
modes = []
mode_name = lambda: "eager" if context.executing_eagerly() else "graph"

class ExampleTest(test_util.TensorFlowTestCase):

    def runTest(self):
        pass

    def setUp(self):
        modes.append("setup_" + mode_name())

    @test_util.run_in_graph_and_eager_modes
    def testBody(self):
        modes.append("run_" + mode_name())

e = ExampleTest()
e.setUp()
e.testBody()

self.assertEqual(modes[1:2], ["run_graph"])
self.assertEqual(modes[2:], ["setup_eager", "run_eager"])
