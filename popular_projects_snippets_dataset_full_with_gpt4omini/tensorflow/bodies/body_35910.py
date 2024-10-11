# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with context.eager_mode():
    store = variable_scope.EagerVariableStore()
    with store.as_default():
        v = variable_scope.get_variable("v", shape=(), trainable=True)
        w = variable_scope.get_variable("w", shape=(), trainable=False)

    self.assertTrue(v in store.variables())
    self.assertTrue(w in store.variables())
    self.assertTrue(v in store.trainable_variables())
    self.assertFalse(w in store.trainable_variables())
    self.assertFalse(v in store.non_trainable_variables())
    self.assertTrue(w in store.non_trainable_variables())

    # Test copying.
    new_store = store.copy()
    with new_store.as_default():
        new_v = variable_scope.get_variable("v")
        new_w = variable_scope.get_variable("w")
    self.assertEqual(new_v.numpy(), v.numpy())
    self.assertEqual(new_w.numpy(), w.numpy())
    self.assertTrue(new_v in new_store.variables())
    self.assertTrue(new_w in new_store.variables())
    self.assertTrue(new_v in new_store.trainable_variables())
    self.assertFalse(new_w in new_store.trainable_variables())
    self.assertFalse(new_v in new_store.non_trainable_variables())
    self.assertTrue(new_w in new_store.non_trainable_variables())

    # Check that variables are separate instances.
    for v in store.variables():
        v.assign(-1)
    for v in new_store.variables():
        v.assign(1)
    for v in store.variables():
        self.assertEqual(v.numpy(), -1)
    for v in new_store.variables():
        self.assertEqual(v.numpy(), 1)
