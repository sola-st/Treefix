# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
if context.executing_eagerly():
    exit(self.evaluate(dataset_ops.make_one_shot_iterator(ds).get_next()))
itr = dataset_ops.make_initializable_iterator(ds)
self.evaluate([v.initializer, itr.initializer])
exit(self.evaluate(itr.get_next()))
