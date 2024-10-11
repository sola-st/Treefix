# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
expected = ["", "file", "ram"]
actual = file_io.get_registered_schemes()
# Be flexible about additional schemes that may sometimes be registered when
# this test is run, while still verifying each scheme appears just once.
maybe_expected = ["gs"]
for scheme in maybe_expected:
    if scheme in actual:
        expected.append("gs")
self.assertCountEqual(expected, actual)
