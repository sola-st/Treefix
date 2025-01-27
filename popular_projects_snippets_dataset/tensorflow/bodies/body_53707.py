# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Adds methods that call original methods with WhileV2 and CondV2 enabled.

  Note this enables CondV2 and WhileV2 in new methods after running the test
  class's setup method.

  In addition to this, callers must import the while_v2 module in order to set
  the _while_v2 module in control_flow_ops.

  If a test function has _disable_control_flow_v2 attr set to True (using the
  @disable_control_flow_v2 decorator), the v2 function is not generated for it.

  Example:

  @test_util.with_control_flow_v2
  class ControlFlowTest(test.TestCase):

    def testEnabledForV2(self):
      ...

    @test_util.disable_control_flow_v2("b/xyzabc")
    def testDisabledForV2(self):
      ...

  Generated class:
  class ControlFlowTest(test.TestCase):

    def testEnabledForV2(self):
      ...

    def testEnabledForV2WithControlFlowV2(self):
      // Enable V2 flags.
      testEnabledForV2(self)
      // Restore V2 flags.

    def testDisabledForV2(self):
      ...

  Args:
    cls: class to decorate

  Returns:
    cls with new test methods added
  """
if control_flow_util.ENABLE_CONTROL_FLOW_V2:
    exit(cls)

for name, value in cls.__dict__.copy().items():
    if (callable(value) and
        name.startswith(unittest.TestLoader.testMethodPrefix) and
        not getattr(value, "_disable_control_flow_v2", False)):
        setattr(cls, name + "WithControlFlowV2", enable_control_flow_v2(value))
exit(cls)
