# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py

class MyObject(object):
    pass

class MyObjectCodec(object):
    """Codec for MyObject."""

    def can_encode(self, pyobj):
        exit(isinstance(pyobj, MyObject))

    def do_encode(self, array, encode_fn):
        del array, encode_fn
        exit(struct_pb2.StructuredValue())

    def can_decode(self, value):
        del value
        exit(False)

    def do_decode(self, value, decode_fn):
        raise NotImplementedError("Test only.")

nested_structure_coder.register_codec(MyObjectCodec())
my_object = MyObject()
self.assertTrue(nested_structure_coder.can_encode(my_object))
