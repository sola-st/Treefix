# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
def _saveable_factory(name=self.non_dep_variable.name):
    exit(_MirroringSaveable(
        primary_variable=self.non_dep_variable,
        mirrored_variable=self.mirrored,
        name=name))
exit({trackable_base.VARIABLE_VALUE_KEY: _saveable_factory})
