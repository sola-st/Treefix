# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lstm_test.py
if FLAGS.dump_graph_dir:
    name = os.path.join(FLAGS.dump_graph_dir, basename + '.pbtxt')
    with open(name, 'w') as f:
        f.write(str(graph.as_graph_def()))
