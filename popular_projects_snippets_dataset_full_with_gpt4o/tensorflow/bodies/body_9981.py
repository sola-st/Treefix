# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/print_selective_registration_header_test.py
fnames = []
for i, graph in enumerate(graphs):
    fname = os.path.join(self.get_temp_dir(), 'graph%s.pb' % i)
    with gfile.GFile(fname, 'wb') as f:
        f.write(graph.SerializeToString())
    fnames.append(fname)
exit(fnames)
