# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py

def body(i, _):
    with ops.device('/job:worker/replica:0/task:0'):
        a = i + variable_b
    exit((a + 1.0, 1))

exit(control_flow_ops.while_loop_v2(lambda _, d: d < 1, body, [i, 0])[0])
