# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():
    _ = variable_scope.get_variable("testGetCollection_a", [])
    _ = variable_scope.get_variable(
        "testGetCollection_b", [], trainable=False)
    with variable_scope.variable_scope("testGetCollection_foo_") as scope1:
        _ = variable_scope.get_variable("testGetCollection_a", [])
        _ = variable_scope.get_variable(
            "testGetCollection_b", [], trainable=False)
        self.assertEqual([
            v.name
            for v in scope1.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES)
        ], ["testGetCollection_foo_/testGetCollection_a:0"])
        self.assertEqual([
            v.name
            for v in scope1.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
        ], [
            "testGetCollection_foo_/testGetCollection_a:0",
            "testGetCollection_foo_/testGetCollection_b:0"
        ])
    with variable_scope.variable_scope("testGetCollection_foo") as scope2:
        _ = variable_scope.get_variable("testGetCollection_a", [])
        _ = variable_scope.get_variable(
            "testGetCollection_b", [], trainable=False)
        self.assertEqual([
            v.name
            for v in scope2.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES)
        ], ["testGetCollection_foo/testGetCollection_a:0"])
        self.assertEqual([
            v.name
            for v in scope2.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
        ], [
            "testGetCollection_foo/testGetCollection_a:0",
            "testGetCollection_foo/testGetCollection_b:0"
        ])
    scope = variable_scope.get_variable_scope()
    self.assertEqual([
        v.name for v in scope.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    ], [
        "testGetCollection_a:0", "testGetCollection_b:0",
        "testGetCollection_foo_/testGetCollection_a:0",
        "testGetCollection_foo_/testGetCollection_b:0",
        "testGetCollection_foo/testGetCollection_a:0",
        "testGetCollection_foo/testGetCollection_b:0"
    ])
    self.assertEqual([
        v.name
        for v in scope.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES)
    ], [
        "testGetCollection_a:0",
        "testGetCollection_foo_/testGetCollection_a:0",
        "testGetCollection_foo/testGetCollection_a:0"
    ])
