# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
evaluate = lambda x: sess.run(x) if sess else self.evaluate(x)
evaluate(iterator.initializer)

for expected_value in expected_values:
    next_element = iterator.get_next()
    computed_value = evaluate(
        [distribute_utils.select_replica(r, next_element) for r in
         range(len(devices))])
    if ignore_order:
        self.assertCountEqual(expected_value, computed_value)
    else:
        self.assertEqual(expected_value, computed_value)

with self.assertRaises(errors.OutOfRangeError):
    next_element = iterator.get_next()
    evaluate(
        [distribute_utils.select_replica(r, next_element) for r in
         range(len(devices))])

# After re-initializing the iterator, should be able to iterate again.
if test_reinitialize:
    evaluate(iterator.initializer)

    for expected_value in expected_values:
        next_element = iterator.get_next()
        computed_value = evaluate([
            distribute_utils.select_replica(r, next_element) for r in
            range(len(devices))
        ])
        if ignore_order:
            self.assertCountEqual(expected_value, computed_value)
        else:
            self.assertEqual(expected_value, computed_value)
