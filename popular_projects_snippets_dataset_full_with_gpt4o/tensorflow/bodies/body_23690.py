# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
if not isinstance(self, weakref.ref):
    ref = weakref.ref(ref)
super(WeakTrackableReference, self).__init__(name=name, ref=ref)
