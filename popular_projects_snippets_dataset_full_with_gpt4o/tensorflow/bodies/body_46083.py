# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer.py
# Because we override __setattr__, we need to attach these attributes using
# the superclass' setattr.
object.__setattr__(self, 'type', type_)
object.__setattr__(self, '_stack', [])
if not hasattr(type_, 'no_root'):
    self.enter()
