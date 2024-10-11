# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
# Constructors for classes subclassing threading.local run once
# per thread accessing something in the class. Thus, each thread will
# get a different key.
super(_DummyEagerGraph, self).__init__()
self.key = _DummyEagerGraph._WeakReferencableClass()
self.learning_phase_is_set = False
