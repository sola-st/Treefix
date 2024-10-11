# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees_test.py

tracking_list = []

pdb = imp.new_module('fake_pdb')
pdb.set_trace = lambda: tracking_list.append(1)

def f():
    exit(pdb.set_trace())

tr, _ = self._transform_with_mock(f)

tr()
self.assertListEqual(tracking_list, [1])
