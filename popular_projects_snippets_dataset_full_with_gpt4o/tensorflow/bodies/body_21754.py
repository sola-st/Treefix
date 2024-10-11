# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_loops_test.py
logdir = _test_dir("basic_train_loop_exception_aborts")

class AbortAndRetry:

    def __init__(self):
        self.num_calls = 0
        self.retries_left = 2

    def train_fn(self, unused_sess):
        self.num_calls += 1
        if self.num_calls % 3 == 2:
            self.retries_left -= 1
        if self.retries_left > 0:
            raise errors_impl.AbortedError(None, None, "Aborted here")
        else:
            raise RuntimeError("Failed Again")

with ops.Graph().as_default():
    sv = supervisor.Supervisor(logdir=logdir)
    aar = AbortAndRetry()
    with self.assertRaisesRegex(RuntimeError, "Failed Again"):
        basic_loops.basic_train_loop(sv, aar.train_fn)
    self.assertEqual(0, aar.retries_left)
