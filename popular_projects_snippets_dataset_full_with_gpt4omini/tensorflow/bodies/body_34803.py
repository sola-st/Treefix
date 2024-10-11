# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
# Start a server to store the table state
server = server_lib.Server({"local0": ["localhost:0"]},
                           protocol="grpc",
                           start=True)
# Create two sessions sharing the same state
session1 = session.Session(server.target)
session2 = session.Session(server.target)

table = lookup_ops.MutableHashTable(
    dtypes.int64,
    dtypes.string,
    "-",
    name="t1",
    experimental_is_anonymous=is_anonymous)

# Populate the table in the first session
with session1:
    self.assertAllEqual(0, table.size())

    keys = constant_op.constant([11, 12], dtypes.int64)
    values = constant_op.constant(["a", "b"])
    table.insert(keys, values).run()
    self.assertAllEqual(2, table.size())

    output = table.lookup(constant_op.constant([11, 12, 13], dtypes.int64))
    self.assertAllEqual([b"a", b"b", b"-"], output)

# Verify that we can access the shared data from the second session
with session2:
    self.assertAllEqual(2, table.size())

    output = table.lookup(constant_op.constant([10, 11, 12], dtypes.int64))
    self.assertAllEqual([b"-", b"a", b"b"], output)
