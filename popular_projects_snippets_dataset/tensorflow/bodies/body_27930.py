# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/text_line_dataset_test.py
filename = os.path.join(self.get_temp_dir(), "text.txt")
with open(filename, "wt") as f:
    for i in range(3):
        f.write("%d\n" % (i,))
first_iterator = iter(readers.TextLineDataset(filename))
self.assertEqual(b"0", next(first_iterator).numpy())
second_iterator = iter(readers.TextLineDataset(filename))
self.assertEqual(b"0", next(second_iterator).numpy())
# Eager kernel caching is based on op attributes, which includes the
# Dataset's output shape. Create a different kernel to test that they
# don't create resources with the same names.
different_kernel_iterator = iter(
    readers.TextLineDataset(filename).repeat().batch(16))
self.assertEqual([16], next(different_kernel_iterator).shape)
# Remove our references to the Python Iterator objects, which (assuming no
# reference cycles) is enough to trigger DestroyResourceOp and close the
# partially-read files.
del first_iterator
del second_iterator
del different_kernel_iterator
if not psutil_import_succeeded:
    self.skipTest(
        "psutil is required to check that we've closed our files.")
open_files = psutil.Process().open_files()
self.assertNotIn(filename, [open_file.path for open_file in open_files])
