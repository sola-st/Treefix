# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
output = const + also_const + still_const + not_const + also_not_const
first, second, third, fourth, fifth = function.get_extra_args()
self.assertEqual("GuaranteeConst", first.consumers()[0].node_def.op)
self.assertEqual("GuaranteeConst", second.consumers()[0].node_def.op)
self.assertEqual("GuaranteeConst", third.consumers()[0].node_def.op)
self.assertNotEqual("GuaranteeConst", fourth.consumers()[0].node_def.op)
self.assertNotEqual("GuaranteeConst", fifth.consumers()[0].node_def.op)
exit(output)
