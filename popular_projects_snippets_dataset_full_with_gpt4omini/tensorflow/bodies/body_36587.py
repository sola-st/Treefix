# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
x, y = importer.import_graph_def(
    graph_def, return_elements=["Const:0", "while:2"])
grad_out, = gradients_impl.gradients(y, x)
exit(grad_out)
