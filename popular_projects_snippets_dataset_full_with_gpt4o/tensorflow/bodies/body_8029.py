# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
distribution, master_target = self._get_test_object(
    task_type, task_id, num_gpus, use_devices_arg=use_devices_arg)
devices = distribution.extended.worker_devices

with ops.Graph().as_default(), \
         self.cached_session(target=master_target) as sess:
    iterator = distribution.make_input_fn_iterator(input_fn)
    sess.run(iterator.initializer)

    for expected_value in expected_values:
        next_element = iterator.get_next()
        computed_value = sess.run([distribute_utils.select_replica(
            r, next_element) for r in range(len(devices))])
        if ignore_order:
            self.assertCountEqual(list(expected_value), list(computed_value))
        else:
            self.assertEqual(list(expected_value), list(computed_value))

    with self.assertRaises(errors.OutOfRangeError):
        next_element = iterator.get_next()
        sess.run([distribute_utils.select_replica(r, next_element)
                  for r in range(len(devices))])

    # After re-initializing the iterator, should be able to iterate again.
    if test_reinitialize:
        sess.run(iterator.initializer)

        for expected_value in expected_values:
            next_element = iterator.get_next()
            computed_value = sess.run([
                distribute_utils.select_replica(r, next_element)
                for r in range(len(devices))])
            if ignore_order:
                self.assertCountEqual(list(expected_value), list(computed_value))
            else:
                self.assertEqual(list(expected_value), list(computed_value))
