# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
"""Tests that reading does not block main execution threads."""
config = config_pb2.ConfigProto(
    inter_op_parallelism_threads=1, intra_op_parallelism_threads=1)
with self.session(config=config) as sess:
    thread_data_t = collections.namedtuple("thread_data_t",
                                           ["thread", "queue", "output"])
    thread_data = []

    # Create different readers, each with its own queue.
    for i in range(3):
        queue = data_flow_ops.FIFOQueue(99, [dtypes.string], shapes=())
        reader = io_ops.TextLineReader()
        _, line = reader.read(queue)
        output = []
        t = threading.Thread(
            target=AsyncReaderTest._RunSessionAndSave,
            args=(sess, [line], output))
        thread_data.append(thread_data_t(t, queue, output))

    # Start all readers. They are all blocked waiting for queue entries.
    self.evaluate(variables.global_variables_initializer())
    for d in thread_data:
        d.thread.start()

    # Unblock the readers.
    for i, d in enumerate(reversed(thread_data)):
        fname = os.path.join(self.get_temp_dir(), "deadlock.%s.txt" % i)
        with open(fname, "wb") as f:
            f.write(("file-%s" % i).encode())
        self.evaluate(d.queue.enqueue_many([[fname]]))
        d.thread.join()
        self.assertEqual([[("file-%s" % i).encode()]], d.output)
