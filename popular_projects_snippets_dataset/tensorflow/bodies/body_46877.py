# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/loader_test.py
test_source = textwrap.dedent('')
_, filename = loader.load_source(test_source, delete_on_exit=True)
# Clean up the file before loader.py tries to remove it, to check that the
# latter can deal with that situation.
os.unlink(filename)
