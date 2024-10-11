# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
train_filename = os.path.join(test_dir, "train_metafile")
saver0_ckpt = os.path.join(test_dir, "saver0.ckpt")
with self.session(graph=ops_lib.Graph()) as sess:
    # Restores from MetaGraphDef.
    new_saver = saver_module.import_meta_graph(train_filename)
    # Restores from checkpoint.
    new_saver.restore(sess, saver0_ckpt)
    train_op = ops_lib.get_collection("train_op")[0]
    self.evaluate(train_op)
