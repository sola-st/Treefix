# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
server = self._cached_server

with ops.Graph().as_default():
    init_value = array_ops.placeholder(dtypes.int32)
    v = variables.VariableV1(init_value, validate_shape=False, name="v")

    sharing_config = config_pb2.ConfigProto(isolate_session_state=False)
    sharing_sess_0 = session.Session(server.target, config=sharing_config)
    sharing_sess_1 = session.Session(server.target, config=sharing_config)

    isolate_config = config_pb2.ConfigProto(isolate_session_state=True)
    isolate_sess_0 = session.Session(server.target, config=isolate_config)
    isolate_sess_1 = session.Session(server.target, config=isolate_config)

    # Initially all variables are initialized.
    for sess in [
        sharing_sess_0, sharing_sess_1, isolate_sess_0, isolate_sess_1
    ]:
        with self.assertRaises(errors_impl.FailedPreconditionError):
            sess.run(v)

      # Shared sessions will see each other's updates, but isolated sessions
      # will not.
    sharing_sess_0.run(v.initializer, feed_dict={init_value: 86})
    self.assertAllEqual(86, sharing_sess_0.run(v))
    self.assertAllEqual(86, sharing_sess_1.run(v))
    with self.assertRaises(errors_impl.FailedPreconditionError):
        isolate_sess_0.run(v)
    with self.assertRaises(errors_impl.FailedPreconditionError):
        isolate_sess_1.run(v)

    # Changing the shape works because `validate_shape` is False.
    sharing_sess_1.run(v.initializer, feed_dict={init_value: [86, 99]})
    self.assertAllEqual([86, 99], sharing_sess_0.run(v))
    self.assertAllEqual([86, 99], sharing_sess_1.run(v))
    with self.assertRaises(errors_impl.FailedPreconditionError):
        isolate_sess_0.run(v)
    with self.assertRaises(errors_impl.FailedPreconditionError):
        isolate_sess_1.run(v)

    # Initializing in an isolated session will only affect the state in that
    # session.
    isolate_sess_0.run(v.initializer, feed_dict={init_value: 37})
    self.assertAllEqual([86, 99], sharing_sess_0.run(v))
    self.assertAllEqual([86, 99], sharing_sess_1.run(v))
    self.assertAllEqual(37, isolate_sess_0.run(v))
    with self.assertRaises(errors_impl.FailedPreconditionError):
        isolate_sess_1.run(v)

    # Isolated sessions can have different shapes for the same variable.
    isolate_sess_1.run(v.initializer, feed_dict={init_value: [19, 86]})
    self.assertAllEqual([86, 99], sharing_sess_0.run(v))
    self.assertAllEqual([86, 99], sharing_sess_1.run(v))
    self.assertAllEqual(37, isolate_sess_0.run(v))
    self.assertAllEqual([19, 86], isolate_sess_1.run(v))
