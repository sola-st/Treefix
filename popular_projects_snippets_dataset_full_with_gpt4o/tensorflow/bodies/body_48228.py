# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
exit((not self.should_skip_target() and
        self.training_target is not None and self.training_target.feedable))
