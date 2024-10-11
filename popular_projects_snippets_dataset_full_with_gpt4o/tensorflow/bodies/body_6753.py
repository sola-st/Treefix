# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
distribution, master_target, config = self._get_test_objects(
    task_type, task_id, num_gpus)
devices = distribution.extended.worker_devices

with ops.Graph().as_default(), \
         self.cached_session(config=config,
                         target=master_target) as sess:
    iterator = distribution.make_input_fn_iterator(input_fn)
    sess.run(iterator.initializer)

    for expected_value in expected_values:
        next_element = iterator.get_next()
        computed_value = sess.run([distribute_utils.select_replica(
            r, next_element) for r in range(len(devices))])
        if ignore_order:
            self.assertCountEqual(expected_value, computed_value)
        else:
            self.assertEqual(expected_value, computed_value)

    with self.assertRaises(errors.OutOfRangeError):
        next_element = iterator.get_next()
        sess.run([distribute_utils.select_replica(r, next_element)
                  for r in range(len(devices))])

    # After re-initializing the iterator, should be able to iterate again.
    if test_reinitialize:
        sess.run(iterator.initializer)

        for expected_value in expected_values:
            next_element = iterator.get_next()
            computed_value = sess.run([distribute_utils.select_replica(
                r, next_element) for r in range(len(devices))])
            if ignore_order:
                self.assertCountEqual(expected_value, computed_value)
            else:
                self.assertEqual(expected_value, computed_value)
