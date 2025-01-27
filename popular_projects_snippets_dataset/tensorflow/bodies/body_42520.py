# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
saver_lib.import_meta_graph(save_prefix + '.meta')
exit(ops.get_default_graph().as_graph_element('output:0'))
