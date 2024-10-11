# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_path = os.path.join(self.get_temp_dir(), "restore_unsharded_iterators")

# Build a graph with 2 parameter nodes on different devices and save.
with session.Session(
    target="",
    config=config_pb2.ConfigProto(device_count={"CPU": 2})) as sess:
    with sess.graph.device("/cpu:0"):
        ds0 = dataset_ops.Dataset.range(10)
        it0 = dataset_ops.make_initializable_iterator(ds0)
        get_next0 = it0.get_next()
    saveable0 = iterator_ops._IteratorSaveable(
        it0._iterator_resource, name="saveable_it0")

    with sess.graph.device("/cpu:1"):
        ds1 = dataset_ops.Dataset.range(20)
        it1 = dataset_ops.make_initializable_iterator(ds1)
        get_next1 = it1.get_next()
    saveable1 = iterator_ops._IteratorSaveable(
        it1._iterator_resource, name="saveable_it1")
    saver = saver_module.Saver({
        "it0": saveable0,
        "it1": saveable1
    },
                               write_version=self._WRITE_VERSION,
                               sharded=True)
    self.evaluate(it0.initializer)
    self.evaluate(it1.initializer)
    self.assertEqual(0, self.evaluate(get_next0))
    self.assertEqual(1, self.evaluate(get_next0))
    self.assertEqual(0, self.evaluate(get_next1))
    val = saver.save(sess, save_path)
    self.assertEqual(save_path, val)
    data_files = glob.glob(save_path + ".data*")
    self.assertEqual(2, len(data_files))

# Restore
with session.Session(
    target="",
    config=config_pb2.ConfigProto(device_count={"CPU": 2})) as sess:
    with sess.graph.device("/cpu:0"):
        ds0 = dataset_ops.Dataset.range(10)
        it0 = dataset_ops.make_initializable_iterator(ds0)
        get_next0 = it0.get_next()
    saveable0 = iterator_ops._IteratorSaveable(
        it0._iterator_resource, name="saveable_it0")

    with sess.graph.device("/cpu:1"):
        ds1 = dataset_ops.Dataset.range(20)
        it1 = dataset_ops.make_initializable_iterator(ds1)
        get_next1 = it1.get_next()
    saveable1 = iterator_ops._IteratorSaveable(
        it1._iterator_resource, name="saveable_it1")
    saver = saver_module.Saver({
        "it0": saveable0,
        "it1": saveable1
    },
                               write_version=self._WRITE_VERSION,
                               sharded=False)
    self.evaluate(it0.initializer)
    self.evaluate(it1.initializer)
    saver.restore(sess, save_path)
    self.assertEqual(2, self.evaluate(get_next0))
    self.assertEqual(1, self.evaluate(get_next1))
