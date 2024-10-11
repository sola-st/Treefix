# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
flops_total = ops.OpStats("flops")
self.assertEqual(None, flops_total.value)
second_flops = ops.OpStats("flops", 3)
flops_total += second_flops
self.assertEqual(3, flops_total.value)
