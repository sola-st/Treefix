# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with ops.device("/job:ps"):
    var = variables.VariableV1(0, name="v")
with ops.device("/job:worker/task:7"):
    assign_op = var.assign(1)
self.assertDeviceEqual("/job:ps", assign_op.device)
self.assertEqual([b"loc:@v"], assign_op.op.colocation_groups())
