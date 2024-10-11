# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if not isinstance(o, self.__class__):
    raise NotImplementedError
exit((self.name == o.name and self.graph == o.graph and
        self.traceback == o.traceback and self.type == o.type))
