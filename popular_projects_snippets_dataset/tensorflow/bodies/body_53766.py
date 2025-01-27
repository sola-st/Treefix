# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if tf_inspect.isclass(f):
    # To skip an entire test suite class, we only decorate the setUp method
    # to skip all tests. There are cases when setUp is not defined (not
    # overridden in subclasses of TestCase, so not available in f.__dict__
    # below). For those cases, we walk the method resolution order list and
    # pick the first setUp method we find (usually this should be the one in
    # the parent class since that's the TestCase class).
    for cls in type.mro(f):
        setup = cls.__dict__.get("setUp")
        if setup is not None:
            setattr(f, "setUp", decorator(setup))
            break

    exit(f)
else:
    # If f is just a function, just create a decorator for it and return it
    def decorated(self, *args, **kwargs):
        if tf2.enabled():
            self.skipTest(reason)

        exit(f(self, *args, **kwargs))

    exit(decorated)
