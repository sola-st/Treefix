# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
with ops.Graph().as_default() as g:
    dataset = dataset_ops.Dataset.range(100).shuffle(
        10, reshuffle_each_iteration=reshuffle).repeat(3)

    if initializable:
        iterators = [dataset_ops.make_initializable_iterator(dataset)
                     for _ in range(2)]
    else:
        iterators = [dataset_ops.make_one_shot_iterator(dataset)
                     for _ in range(2)]

    results = []
    with self.session(graph=g) as sess:
        for iterator in iterators:
            if initializable:
                sess.run(iterator.initializer)
            next_element = iterator.get_next()
            run_results = []
            for _ in range(300):
                run_results.append(sess.run(next_element))
            with self.assertRaises(errors.OutOfRangeError):
                sess.run(next_element)

            results.append(run_results)

        self.assertNotEqual(results[0], results[1])
