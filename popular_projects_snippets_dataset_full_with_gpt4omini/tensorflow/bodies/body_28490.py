# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
results = []
for _ in range(2):
    with ops.Graph().as_default() as g:
        random_seed.set_random_seed(graph_seed)
        dataset = dataset_ops.Dataset.range(10).shuffle(
            10, seed=op_seed, reshuffle_each_iteration=reshuffle).repeat(3)
        iterator = dataset_ops.make_one_shot_iterator(dataset)
        next_element = iterator.get_next()

        run_results = []
        with self.session(graph=g) as sess:
            for _ in range(30):
                run_results.append(sess.run(next_element))
            with self.assertRaises(errors.OutOfRangeError):
                sess.run(next_element)
        results.append(run_results)

self.assertAllEqual(results[0], results[1])
