# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
group_size = 2
group_key = 100

@def_function.function
def f():
    with ops.device('CPU:0'):
        _collective_ops.initialize_communicator(
            group_key=group_key, rank=0, group_size=group_size)
    with ops.device('CPU:1'):
        _collective_ops.initialize_communicator(
            group_key=group_key, rank=1, group_size=group_size)

    # TODO(b/193864859): Add validation with reduction op.

self.evaluate(f())
