# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/print_selective_registration_header.py
graphs = FLAGS.graphs.split(',')
print(
    selective_registration_header_lib.get_header(graphs,
                                                 FLAGS.proto_fileformat,
                                                 FLAGS.default_ops))
