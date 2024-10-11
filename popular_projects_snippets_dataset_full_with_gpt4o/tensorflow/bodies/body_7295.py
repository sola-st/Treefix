# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py

def cond_body():
    reduced = collective.reduce(reduce_util.ReduceOp.SUM, value, value,
                                options)
    exit(math_ops.add_n(self.as_list(reduced)) / len(devices))

exit(control_flow_ops.cond(
    array_ops.identity(False), cond_body, cond_body))
