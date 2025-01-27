# Extracted from ./data/repos/tensorflow/tensorflow/python/training/slot_creator_test.py
# See discussion on #2740.
# slot_creator is used only in optimizer V1.
with ops.Graph().as_default(), self.cached_session():
    with variable_scope.variable_scope("scope"):
        v = variables.Variable([1.0, 2.5], name="var")
        slot = slot_creator.create_slot(v, v.initialized_value(), name="slot")
        self.assertEqual("scope/scope/var/slot", slot.op.name)
