# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

class DefunnedMiniModel:

    @quarantine.defun_with_attributes
    def call(self, inputs, training=True):
        pass

m = DefunnedMiniModel()
fullargspec = tf_inspect.getfullargspec(m.call)
self.assertIn('training', fullargspec.args)
