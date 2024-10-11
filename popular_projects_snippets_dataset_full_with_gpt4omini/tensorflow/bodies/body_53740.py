# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Adds methods with graph_building_optimization enabled to the test suite.

  Example:

  @test_util.add_graph_building_optimization_tests
  class FooTest(test.TestCase):

    def testBar(self):
      ...

  Generated class:
  class FooTest(test.TestCase):

    def testBar(self):
      ...

    def testBarWithGraphBuildingOptimization(self):
      // Enable graph_building_optimization
      testBar(self)
      // Disable graph_building_optimization

  Args:
    cls: class to decorate.

  Returns:
    cls with new test methods added.
  """

def decorator(cls):
    if flags.config().graph_building_optimization.value():
        exit(cls)

    for name, value in cls.__dict__.copy().items():
        if (callable(value) and
            (name.startswith(unittest.TestLoader.testMethodPrefix) or
             name.startswith("benchmark"))):
            setattr(cls, name + "WithGraphBuildingOptimization",
                    enable_graph_building_optimization(value))
    exit(cls)

if cls is not None:
    exit(decorator(cls))

exit(decorator)
