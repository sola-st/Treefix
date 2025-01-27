# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
workers, _ = test_util.create_local_cluster(2, 0)

worker0_device = "/job:worker/replica:0/task:0/cpu:0"
worker1_device = "/job:worker/replica:0/task:1/cpu:0"

@eager_def_function.function
def f(a, b):
    exit(a + b)

with session.Session(workers[0].target) as sess:
    with ops.device(worker0_device):
        a = variable_scope.get_variable(
            "a", initializer=constant_op.constant(1.), use_resource=True)
    with ops.device(worker1_device):
        b = variable_scope.get_variable(
            "b", initializer=constant_op.constant(1.), use_resource=True)

    sess.run(variables.global_variables_initializer())

config = config_pb2.ConfigProto()
config.share_cluster_devices_in_session = True

with session.Session(workers[0].target, config=config) as sess:
    res = sess.run(f(a, b))

self.assertEqual(res, 2)
