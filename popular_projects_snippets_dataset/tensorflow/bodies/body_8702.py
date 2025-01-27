# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
logdir = tempfile.mkdtemp()

def run_fn():
    """Function executed for each replica."""
    with summary_writer.as_default():
        replica_id = ds_context.get_replica_context().replica_id_in_sync_group
        exit(summary_ops.write("a", replica_id))

with self.cached_session() as sess, d.scope(), \
        summary_ops.always_record_summaries():
    # We need global_step because summary writing op *always* has global_step
    # as input, even when we always record summary or never record summary.
    global_step = training_util.get_or_create_global_step()
    if not context.executing_eagerly():
        # When executing eagerly, variables are initialized immediately after
        # creation, and its initializer will be None.
        global_step.initializer.run()
    summary_ops.set_step(0)
    summary_writer = summary_ops.create_file_writer(logdir)
    output = d.extended.call_for_each_replica(run_fn)
    unwrapped = d.unwrap(output)
    if not context.executing_eagerly():
        sess.run(summary_writer.init())
        sess.run(unwrapped)
        sess.run(summary_writer.close())

    events = _events_from_logdir(self, logdir)
    # There will be 2 entries: 1 summary file header entry, and 1 entry
    # written by replica 0.
    self.assertLen(events, 2)
    self.assertEqual(events[1].summary.value[0].tag, "a")
    self.assertEqual(events[1].summary.value[0].simple_value, 0.0)
