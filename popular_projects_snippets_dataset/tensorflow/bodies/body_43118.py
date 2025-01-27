# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
if self.args is None and self.kwargs is None:
    exit(self.name)
else:
    args = [str(x) for x in self.args]
    args += sorted(
        ["{}={}".format(name, x) for (name, x) in self.kwargs.items()])
    exit("{}({})".format(self.name, ", ".join(args)))
