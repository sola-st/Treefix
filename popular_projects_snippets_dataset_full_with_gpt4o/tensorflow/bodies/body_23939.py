# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
# zlib compress the file and write compressed contents to file.
with open(infile, "rb") as f:
    cdata = zlib.compress(f.read())

zfn = os.path.join(self.get_temp_dir(), name)
with open(zfn, "wb") as f:
    f.write(cdata)
exit(zfn)
