# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/stage_op_test.py
memory_limit = 512 * 1024  # 512K
chunk = 200 * 1024  # 256K
capacity = memory_limit // chunk

with ops.Graph().as_default() as G:
    with ops.device('/cpu:0'):
        x = array_ops.placeholder(dtypes.uint8, name='x')
    with ops.device(test.gpu_device_name()):
        stager = data_flow_ops.StagingArea(
            [
                dtypes.uint8,
            ], memory_limit=memory_limit, shapes=[[]])
        stage = stager.put([x])
        ret = stager.get()
        size = stager.size()

G.finalize()

value_queue = queue.Queue()
n = 8

with self.session(graph=G) as sess:
    # Stage data in a separate thread which will block when it hits the
    # staging area's capacity and thus not fill the value_queue with n tokens
    def thread_run():
        for i in range(n):
            sess.run(stage, feed_dict={x: np.full(chunk, i, dtype=np.uint8)})
            value_queue.put(0)

    t = threading.Thread(target=thread_run)
    t.daemon = True
    t.start()

    # Get tokens from the value_queue until a timeout occurs
    try:
        for i in range(n):
            value_queue.get(timeout=TIMEOUT)
    except queue.Empty:
        pass

    # Should've timed out on the iteration 'capacity'
    if not i == capacity:
        self.fail("Expected to timeout on iteration '{}' "
                  "but instead timed out on iteration '{}' "
                  "Staging Area size is '{}' and configured "
                  "capacity is '{}'.".format(capacity, i, sess.run(size),
                                             capacity))

    # Should have capacity elements in the staging area
    self.assertTrue(sess.run(size) == capacity)

    # Clear the staging area completely
    for i in range(n):
        self.assertTrue(np.all(sess.run(ret)[0] == i))

    self.assertTrue(sess.run(size) == 0)
