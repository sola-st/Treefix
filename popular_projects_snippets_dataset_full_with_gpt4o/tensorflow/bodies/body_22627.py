# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_sparse_job_test.py
server = server_lib.Server({"local": {37: "localhost:0"}})
with ops.device("/job:local/task:37"):
    a = constant_op.constant(1.0)

with session.Session(server.target) as sess:
    self.assertEqual(1.0, self.evaluate(a))
