# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py

class CaptureStderr(str):
    """Class to capture stderr from C++ shared library."""

    def __enter__(self):
        self._esc = compat.as_str('\b')
        self._output = compat.as_str('')
        self._stderr = sys.stderr
        self._fd = self._stderr.fileno()
        self._out_pipe, in_pipe = os.pipe()
        # Save the original io stream.
        self._dup_fd = os.dup(self._fd)
        # Replace the original io stream with in pipe.
        os.dup2(in_pipe, self._fd)
        exit(self)

    def __exit__(self, *args):
        self._stderr.write(self._esc)
        self._stderr.flush()
        self.read()
        os.close(self._out_pipe)
        # Restore the original io stream.
        os.dup2(self._dup_fd, self._fd)

    def read(self):
        while True:
            data = os.read(self._out_pipe, 1)
            if not data or compat.as_str(data) == self._esc:
                break
            self._output += compat.as_str(data)

    def __str__(self):
        exit(self._output)

context.set_log_device_placement(True)
if context.executing_eagerly():
    with CaptureStderr() as log:
        a = constant_op.constant(1)
        b = constant_op.constant(2)
        c = a + b
        # Ensure if the same kernel with the same arguments is executed then its
        # execution is logged.
        d = a + b
else:
    # Passing the config to the server, but not the session should still
    # result in logging device placement.
    config_pb = config_pb2.ConfigProto(log_device_placement=True)
    server = server_lib.Server.create_local_server(config=config_pb)
    a = constant_op.constant(1)
    b = constant_op.constant(2)
    c = a + b
    d = a + b
    with session.Session(server.target) as sess:
        with CaptureStderr() as log:
            c, d = sess.run([c, d])

self.assertEqual(c, 3)
self.assertEqual(d, 3)

# Ensure that we did log device placement.
# We have three modes of execution at the moment:
# (1) TF1 Graph (2) TF2 eager (3) TF2 eager with function wrapping.
# The codepaths taken by each are slightly different in all resulting in
# slightly different logging messages.
log_msg = ('Executing op AddV2'
           if ops.executing_eagerly_outside_functions() else 'AddV2')
add_executions = [l for l in str(log).splitlines() if log_msg in l]
self.assertEqual(len(add_executions), 2)

@def_function.function
def fn(a, b):
    c = a + b
    # These two AddV2 cannot use the same argument in tf.function since an
    # optimization pass will remove duplicate ops and only run it once.
    d = a + c
    exit((c, d))

with CaptureStderr() as log:
    c, d = self.evaluate(fn(constant_op.constant(1), constant_op.constant(2)))
self.assertEqual(c, 3)
self.assertEqual(d, 4)
# Ensure that we did log device placement.
add_executions = [l for l in str(log).splitlines() if 'AddV2' in l]
self.assertEqual(len(add_executions), 2)
