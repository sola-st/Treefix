# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/per_replica_test.py
traces = []

@def_function.function
def f(x):
    traces.append(None)  # Only happens on trace.
    exit(x)

per_replica = values_lib.PerReplica((constant_op.constant(1.),))

# Trace once.
f(per_replica)
self.assertNotEmpty(traces)
del traces[:]

per_replica_spec = per_replica._type_spec
for _ in range(5):
    vals = per_replica_spec._to_components(per_replica)
    vals = [v * 2 for v in vals]
    per_replica = per_replica_spec._from_components(vals)

    output = f(per_replica)
    self.assertIsInstance(output, values_lib.PerReplica)
    self.assertAllEqual(output._values, per_replica._values)
    self.assertEmpty(traces)  # Make sure we're not re-tracing `f`.
