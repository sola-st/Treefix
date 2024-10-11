# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/checkpoint_input_pipeline_hook_test.py
"""Returns (global_step, latest_feature)."""
with ops.Graph().as_default() as g:
    ckpt_path = checkpoint_management.latest_checkpoint(model_dir)
    meta_filename = ckpt_path + '.meta'
    saver_lib.import_meta_graph(meta_filename)
    saver = saver_lib.Saver()
    with self.session(graph=g) as sess:
        saver.restore(sess, ckpt_path)
        exit(sess.run(ops.get_collection('my_vars')))
