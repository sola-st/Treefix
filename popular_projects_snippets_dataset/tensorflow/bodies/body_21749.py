# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_loops_test.py
logdir = _test_dir("basic_train_loop")
# Counts the number of calls.
num_calls = [0]

def train_fn(unused_sess, sv, y, a):
    num_calls[0] += 1
    self.assertEqual("y", y)
    self.assertEqual("A", a)
    if num_calls[0] == 3:
        sv.request_stop()

with ops.Graph().as_default():
    sv = supervisor.Supervisor(logdir=logdir)
    basic_loops.basic_train_loop(
        sv, train_fn, args=(sv, "y"), kwargs={"a": "A"})
    self.assertEqual(3, num_calls[0])
