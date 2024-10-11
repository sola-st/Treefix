# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py

def noop(ev):
    ev.set()

event_arg = threading.Event()

self.assertFalse(event_arg.is_set())
t = self.checkedThread(target=noop, args=(event_arg,))
t.start()
t.join()
self.assertTrue(event_arg.is_set())
