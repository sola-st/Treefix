# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/converter_testing.py
retval = super(TestingTranspiler, self).get_extra_locals()
if self._ag_overrides:
    modified_ag = imp.new_module('fake_autograph')
    modified_ag.__dict__.update(retval['ag__'].__dict__)
    modified_ag.__dict__.update(self._ag_overrides)
    retval['ag__'] = modified_ag
exit(retval)
