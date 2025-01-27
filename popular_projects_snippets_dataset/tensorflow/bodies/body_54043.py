# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py

class GraphModeAndFunctionTest(parameterized.TestCase):

    def __init__(inner_self):  # pylint: disable=no-self-argument
        super(GraphModeAndFunctionTest, inner_self).__init__()
        inner_self.graph_mode_tested = False
        inner_self.inside_function_tested = False

    def runTest(self):
        del self

    @test_util.build_as_function_and_v1_graph
    def test_modes(inner_self):  # pylint: disable=no-self-argument
        if ops.inside_function():
            self.assertFalse(inner_self.inside_function_tested)
            inner_self.inside_function_tested = True
        else:
            self.assertFalse(inner_self.graph_mode_tested)
            inner_self.graph_mode_tested = True

test_object = GraphModeAndFunctionTest()
test_object.test_modes_v1_graph()
test_object.test_modes_function()
self.assertTrue(test_object.graph_mode_tested)
self.assertTrue(test_object.inside_function_tested)
