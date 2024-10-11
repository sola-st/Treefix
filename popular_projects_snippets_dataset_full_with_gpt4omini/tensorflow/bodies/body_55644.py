# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
base_tensor_name = tensor_name.replace("export/", "")
exit("import/" + base_tensor_name)
