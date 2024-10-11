# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/registry_test.py
myreg = registry.Registry('testbar')
myreg.register(bar, 'Bar')
with self.assertRaisesRegex(
    KeyError, r'Registering two testbar with name \'Bar\'! '
    r'\(Previous registration was in [^ ]+ .*.py:[0-9]+\)'):
    myreg.register(bar, 'Bar')
