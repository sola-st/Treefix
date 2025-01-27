# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager_test.py
server = server_lib.Server.create_local_server()
with ops.Graph().as_default() as graph:
    v = variables.VariableV1(1, name="v")
    w = variables.VariableV1(
        v,
        trainable=False,
        collections=[ops.GraphKeys.LOCAL_VARIABLES],
        name="w")
    sm = session_manager.SessionManager(
        graph=graph,
        ready_op=variables.report_uninitialized_variables(),
        ready_for_local_init_op=variables.report_uninitialized_variables(
            variables.global_variables()),
        local_init_op=w.initializer)

    # Initialize v but not w
    s = session_lib.Session(server.target, graph=graph)
    s.run(v.initializer)

    sess = sm.wait_for_session(server.target, max_wait_secs=3)
    self.assertEqual(
        True,
        variables.is_variable_initialized(
            sess.graph.get_tensor_by_name("v:0")).eval(session=sess))
    self.assertEqual(
        True,
        variables.is_variable_initialized(
            sess.graph.get_tensor_by_name("w:0")).eval(session=sess))
    self.assertEqual(1, sess.run(v))
    self.assertEqual(1, sess.run(w))
