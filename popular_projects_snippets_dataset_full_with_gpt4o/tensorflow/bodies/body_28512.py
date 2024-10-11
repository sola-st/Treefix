# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
range_limit = 5
num_repeats = 2
num_outputs = range_limit * num_repeats

def ds_fn():
    # pylint: disable=cell-var-from-loop
    exit(self._build_shuffle_dataset(
        range_limit=range_limit,
        num_repeats=num_repeats,
        buffer_size=buffer_size,
        seed=None,  # Iterator seeds are generated non-deterministically.
        reshuffle_each_iteration=reshuffle_each_iteration))
    # pylint: enable=cell-var-from-loop

with ops.Graph().as_default() as g:
    ds = ds_fn()
    iterators = [ds.make_one_shot_iterator(), ds.make_one_shot_iterator()]
    get_next_ops = [it.get_next() for it in iterators]
    saveables = [
        contrib_iterator_ops.make_saveable_from_iterator(it)
        for it in iterators
    ]
    for saveable in saveables:
        ops.add_to_collection(ops.GraphKeys.SAVEABLE_OBJECTS, saveable)
    saver = saver_lib.Saver(allow_empty=True)
    with self.session(graph=g) as sess:
        self._save(sess, saver)
        expected = [self.evaluate(get_next_ops) for _ in range(num_outputs)]
        self._restore(saver, sess)
        actual = [self.evaluate(get_next_ops) for _ in range(num_outputs)]
        self.match(expected, actual)
