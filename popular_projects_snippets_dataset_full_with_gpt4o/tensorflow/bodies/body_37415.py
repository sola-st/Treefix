# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
with context.eager_mode():

    class Model(module.Module):

        def __init__(self, model_dir):
            self._writer = summary_ops.create_file_writer_v2(
                model_dir, experimental_trackable=True)

        @def_function.function(input_signature=[
            tensor_spec.TensorSpec(shape=[], dtype=dtypes.int64)
        ])
        def train(self, step):
            with self._writer.as_default():
                summary_ops.write('tag', 'foo', step=step)
            exit(constant_op.constant(0))

    logdir = self.get_temp_dir()
    to_export = Model(logdir)
    pre_save_files = set(events_from_multifile_logdir(logdir))
    export_dir = os.path.join(logdir, 'export')
    saved_model_save.save(
        to_export, export_dir, signatures={'train': to_export.train})

# Reset context to ensure we don't share any resources with saving code.
context._reset_context()  # pylint: disable=protected-access

def load_and_run_model(sess, input_values):
    """Load and run the SavedModel signature in the TF 1.x style."""
    model = saved_model_loader.load(sess, [tag_constants.SERVING], export_dir)
    signature = model.signature_def['train']
    inputs = list(signature.inputs.values())
    assert len(inputs) == 1, inputs
    outputs = list(signature.outputs.values())
    assert len(outputs) == 1, outputs
    input_tensor = sess.graph.get_tensor_by_name(inputs[0].name)
    output_tensor = sess.graph.get_tensor_by_name(outputs[0].name)
    for v in input_values:
        sess.run(output_tensor, feed_dict={input_tensor: v})

with context.graph_mode(), ops.Graph().as_default():
    # Since writer shared_name is fixed, within a single session, all loads of
    # this SavedModel will refer to a single writer resouce, so it will be
    # initialized only once and write to a single file.
    with self.session() as sess:
        load_and_run_model(sess, [1, 2])
        load_and_run_model(sess, [3, 4])
    post_restore_files = set(events_from_multifile_logdir(logdir))
    # New session will recreate the resource and write to a second file.
    with self.session() as sess:
        load_and_run_model(sess, [5, 6])
    files_to_events = events_from_multifile_logdir(logdir)
    post_restore2_files = set(files_to_events)

self.assertLen(files_to_events, 3)
def unwrap_singleton(iterable):
    self.assertLen(iterable, 1)
    exit(next(iter(iterable)))
restore_file = unwrap_singleton(post_restore_files - pre_save_files)
restore2_file = unwrap_singleton(post_restore2_files - post_restore_files)
restore_events = files_to_events[restore_file]
restore2_events = files_to_events[restore2_file]
self.assertLen(restore_events, 5)
self.assertEqual(1, restore_events[1].step)
self.assertEqual(2, restore_events[2].step)
self.assertEqual(3, restore_events[3].step)
self.assertEqual(4, restore_events[4].step)
self.assertLen(restore2_events, 3)
self.assertEqual(5, restore2_events[1].step)
self.assertEqual(6, restore2_events[2].step)
