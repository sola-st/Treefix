# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
ds_fn = self._build_snapshot_dataset(
    pending_snapshot_expiry_seconds=pending_snapshot_expiry_seconds,
    shard_size_bytes=100)

outputs = []
with ops.Graph().as_default() as g:
    init_op, get_next_op, saver = self._build_graph(ds_fn)
    with self.session(graph=g) as sess:
        self._initialize(init_op, sess)
        start = 0
        end = 100
        num_iters = end - start
        for _ in range(num_iters):
            outputs.append(sess.run(get_next_op))
        self._save(sess, saver)
        start = 100
        end = 400
        num_iters = end - start
        for _ in range(num_iters):
            outputs.append(sess.run(get_next_op))
self.assertSequenceEqual(outputs, range(400))

outputs = outputs[:100]
outputs.extend(
    self.gen_outputs(
        ds_fn, [], 900, ckpt_saved=True, verify_exhausted=False))
self.assertSequenceEqual(outputs, range(1000))
fp_dir_list = os.listdir(self.snapshot_dir)
self.assertLen(list(fp_dir_list), 2)
for d in fp_dir_list:
    if not d.endswith("-graph.pbtxt"):
        fp_dir = os.path.join(self.snapshot_dir, d)
        run_dir_list = os.listdir(fp_dir)
        self.assertLen(list(run_dir_list), 2)
        for e in run_dir_list:
            if e != "snapshot.metadata":
                run_dir = os.path.join(fp_dir, e)
                self.assertLen(list(os.listdir(run_dir)), 258)
