# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
# Start a server
server = server_lib.Server({"local0": ["localhost:0"]},
                           protocol="grpc",
                           start=True)
# Create two sessions sharing the same state
session1 = session.Session(server.target)
session2 = session.Session(server.target)

default_val = -1
keys = constant_op.constant(["brain", "salad", "surgery"])
values = constant_op.constant([0, 1, 2], dtypes.int64)
table = self.getHashTable()(
    lookup_ops.KeyValueTensorInitializer(keys, values),
    default_val,
    name="t1",
    experimental_is_anonymous=is_anonymous)

# Init the table in the first session.
with session1:
    self.initialize_table(table)
    self.assertAllEqual(3, self.evaluate(table.size()))

# Init the table in the second session and verify that we do not get a
# "Table already initialized" error.
with session2:
    self.evaluate(table.initializer)
    self.assertAllEqual(3, self.evaluate(table.size()))
