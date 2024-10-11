# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
var = variables.Variable(1.0)
const = array_ops.guarantee_const(var)
also_const = array_ops.identity(const)
still_const = array_ops.identity(also_const)
not_const = still_const + var
also_not_const = array_ops.placeholder(dtypes.float32)

@function.Defun()
def CapturesGuaranteedConst():
    output = const + also_const + still_const + not_const + also_not_const
    first, second, third, fourth, fifth = function.get_extra_args()
    self.assertEqual("GuaranteeConst", first.consumers()[0].node_def.op)
    self.assertEqual("GuaranteeConst", second.consumers()[0].node_def.op)
    self.assertEqual("GuaranteeConst", third.consumers()[0].node_def.op)
    self.assertNotEqual("GuaranteeConst", fourth.consumers()[0].node_def.op)
    self.assertNotEqual("GuaranteeConst", fifth.consumers()[0].node_def.op)
    exit(output)

with self.session(use_gpu=False) as sess:
    self.evaluate(var.initializer)
    _ = sess.run(CapturesGuaranteedConst(), {also_not_const: 1.0})
