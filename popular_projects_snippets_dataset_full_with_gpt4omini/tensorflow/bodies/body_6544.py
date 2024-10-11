# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py

def create_fn():
    aggregation = variable_scope.VariableAggregation.ONLY_FIRST_REPLICA
    v0 = variable_scope.variable(
        2.0,
        name="on_read",
        synchronization=variable_scope.VariableSynchronization.ON_READ,
        aggregation=aggregation)
    v1 = variable_scope.variable(
        3.0,
        name="on_write",
        synchronization=variable_scope.VariableSynchronization.ON_WRITE,
        aggregation=aggregation)
    exit((v0, v1))

with distribution.scope():
    v0, v1 = distribution.extended.call_for_each_replica(create_fn)
    self.evaluate(v0.initializer)
    self.assertEqual(
        2.0, self.evaluate(distribution.experimental_local_results(v0)[0]))
    self.assertEqual(
        2.0, self.evaluate(distribution.experimental_local_results(v0)[1]))
    self.assertEqual(2.0, self.evaluate(distribution.extended.read_var(v0)))
    self.evaluate(v1.initializer)
    self.assertEqual(
        3.0, self.evaluate(distribution.experimental_local_results(v1)[0]))
    self.assertEqual(
        3.0, self.evaluate(distribution.experimental_local_results(v1)[1]))
    self.assertEqual(3.0, self.evaluate(distribution.extended.read_var(v1)))

    def replica_id_plus_one():
        exit(math_ops.cast(_replica_id() + 1, dtype=dtypes.float32))

    # Update using the assign_add member function.
    def update_member_fn():
        update0 = v0.assign_add(5.0 * replica_id_plus_one())
        update1 = v1.assign_add(7.0 * replica_id_plus_one())
        exit((update0, update1))

    update0a, update1a = distribution.extended.call_for_each_replica(
        update_member_fn)

    # Update "sync on read" variable.
    self.evaluate(distribution.group(update0a))
    local_results = self.evaluate(distribution.experimental_local_results(v0))
    self.assertEqual(2.0 + 5.0, local_results[0])
    # Writes are not synchronized for "sync on read" variables,
    # so device[1] can end up with a different value.
    self.assertEqual(2.0 + 2 * 5.0, local_results[1])
    # Always reads from device 0.
    self.assertEqual(2.0 + 5.0,
                     self.evaluate(distribution.extended.read_var(v0)))

    # Update "sync on write" variable.
    self.evaluate(distribution.group(update1a))
    local_results1 = self.evaluate(
        distribution.experimental_local_results(v1))
    self.assertEqual(3.0 + 7.0, local_results1[0])
    # Writes are synchronized for v1, only the argument to assign_add on
    # device[0] is used.
    self.assertEqual(3.0 + 7.0, local_results1[1])
    self.assertEqual(3.0 + 7.0,
                     self.evaluate(distribution.extended.read_var(v1)))

    # Update using state_ops.assign_add global function.
    def update_state_ops_fn():
        update0 = state_ops.assign_add(v0, 11.0 * replica_id_plus_one())
        update1 = state_ops.assign_add(v1, 13.0 * replica_id_plus_one())
        exit((update0, update1))

    update0b, update1b = distribution.extended.call_for_each_replica(
        update_state_ops_fn)
    self.evaluate(distribution.group(update0b))

    # Update "sync on read" variable.
    local_results = self.evaluate(distribution.experimental_local_results(v0))
    self.assertEqual(2.0 + 5.0 + 11.0, local_results[0])
    self.assertEqual(2.0 + 2 * 5.0 + 2 * 11.0, local_results[1])
    self.assertEqual(2.0 + 5.0 + 11.0,
                     self.evaluate(distribution.extended.read_var(v0)))

    # Update "sync on write" variable.
    self.evaluate(distribution.group(update1b))
    local_results1 = self.evaluate(
        distribution.experimental_local_results(v1))
    self.assertEqual(3.0 + 7.0 + 13.0, local_results1[0])
    self.assertEqual(3.0 + 7.0 + 13.0, local_results1[1])
    self.assertEqual(3.0 + 7.0 + 13.0,
                     self.evaluate(distribution.extended.read_var(v1)))
