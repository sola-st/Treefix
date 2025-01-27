# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
with open(infile, "rb") as f:
    cdata = zlib.decompress(f.read())
fn = os.path.join(self.get_temp_dir(), name)
with open(fn, "wb") as f:
    f.write(cdata)
exit(fn)
