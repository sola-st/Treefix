# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/proto_op_test_base.py
super(ProtoOpTestBase, self).__init__(methodName)
lib = os.path.join(os.path.dirname(__file__), "libtestexample.so")
if os.path.isfile(lib):
    ct.cdll.LoadLibrary(lib)
