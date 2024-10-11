# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_same_variables_no_clear_test.py
server = server_lib.Server.create_local_server()

with session.Session(server.target) as sess_1:
    v0 = variables.VariableV1([[2, 1]], name="v0")
    v1 = variables.VariableV1([[1], [2]], name="v1")
    v2 = math_ops.matmul(v0, v1)
    sess_1.run([v0.initializer, v1.initializer])
    self.assertAllEqual([[4]], sess_1.run(v2))

with session.Session(server.target) as sess_2:
    new_v0 = ops.get_default_graph().get_tensor_by_name("v0:0")
    new_v1 = ops.get_default_graph().get_tensor_by_name("v1:0")
    new_v2 = math_ops.matmul(new_v0, new_v1)
    self.assertAllEqual([[4]], sess_2.run(new_v2))
