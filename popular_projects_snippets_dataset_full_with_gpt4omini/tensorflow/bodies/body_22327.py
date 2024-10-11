# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
t = constant_op.constant(42.0, name='foo')
train_op = constant_op.constant(3)

hook = basic_session_run_hooks.LoggingTensorHook(
    tensors=[t.name], every_n_secs=1.0, at_end=at_end)
hook.begin()
mon_sess = monitored_session._HookedSession(sess, [hook])
self.evaluate(variables_lib.global_variables_initializer())

mon_sess.run(train_op)
self.assertRegex(str(self.logged_message), t.name)

# assertNotRegexpMatches is not supported by python 3.1 and later
self.logged_message = ''
mon_sess.run(train_op)
self.assertEqual(str(self.logged_message).find(t.name), -1)
mock_time.return_value += 1.0

self.logged_message = ''
mon_sess.run(train_op)
self.assertRegex(str(self.logged_message), t.name)

self.logged_message = ''
hook.end(sess)
if at_end:
    self.assertRegex(str(self.logged_message), t.name)
else:
    # assertNotRegexpMatches is not supported by python 3.1 and later
    self.assertEqual(str(self.logged_message).find(t.name), -1)
