# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
exit((self.should_skip_target() or self.training_target is None or
        self.training_target.skip_target_weights))
