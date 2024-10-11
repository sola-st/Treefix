# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with ops.Graph().as_default():
    dataset = dataset_ops.Dataset.range(1)
    iterator = dataset_ops.make_one_shot_iterator(dataset)
    read_ops = iterator.get_next()
    final_ops = read_ops

    hook = basic_session_run_hooks.FinalOpsHook(final_ops)
    hook.begin()

    with session_lib.Session() as session:
        session.run(read_ops)
        with test.mock.patch.object(tf_logging, 'warning') as mock_log:
            with self.assertRaisesRegex(errors.OutOfRangeError,
                                        'End of sequence'):
                hook.end(session)
            self.assertRegex(
                str(mock_log.call_args), 'dependency back to some input source')
