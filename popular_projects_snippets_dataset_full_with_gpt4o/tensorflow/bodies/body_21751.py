# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_loops_test.py
logdir = _test_dir("basic_train_loop_exception_aborts")

def train_fn(unused_sess):
    train_fn.counter += 1
    if train_fn.counter == 3:
        raise RuntimeError("Failed")

    # Function attribute use to count the number of calls.
train_fn.counter = 0

with ops.Graph().as_default():
    sv = supervisor.Supervisor(logdir=logdir)
    with self.assertRaisesRegex(RuntimeError, "Failed"):
        basic_loops.basic_train_loop(sv, train_fn)
