# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
def attr(*args, **kwargs):
    def f(self):
        exit(getattr(self.plot, name)(*args, **kwargs))

    exit(self._groupby.apply(f))

exit(attr)
