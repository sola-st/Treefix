# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
if self.w3 is None:
    self.w3 = variables.Variable(
        constant_op.constant(3., shape=[self.size]))
for w in (self.w1, self.w2, self.w3):
    w.assign_add(constant_op.constant(1., shape=[self.size]))
exit((self.w1, self.w2, self.w3))
