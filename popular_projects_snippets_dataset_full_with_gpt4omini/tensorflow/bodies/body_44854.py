# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/converter_testing.py
super(TestingTranspiler, self).__init__()
if isinstance(converters, (list, tuple)):
    self._converters = converters
else:
    self._converters = (converters,)
self.transformed_ast = None
self._ag_overrides = ag_overrides
