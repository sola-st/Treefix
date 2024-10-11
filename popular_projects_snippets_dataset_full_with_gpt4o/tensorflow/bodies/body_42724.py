# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
orig_threshold = np.get_printoptions()["threshold"]
orig_edgeitems = np.get_printoptions()["edgeitems"]
np.set_printoptions(threshold=2, edgeitems=1)

t = _create_tensor(np.arange(10, dtype=np.int32))
self.assertTrue(re.match(r".*\[.*0.*\.\.\..*9.*\]", str(t)))
self.assertTrue(re.match(r".*\[.*0.*\.\.\..*9.*\]", repr(t)))

# Clean up: reset to previous printoptions.
np.set_printoptions(threshold=orig_threshold, edgeitems=orig_edgeitems)
