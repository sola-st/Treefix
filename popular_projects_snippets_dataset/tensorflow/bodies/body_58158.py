# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util_test.py
source, header = util.convert_bytes_to_c_source(
    b"\x00\x01\x02\x23", "foo", 16, use_tensorflow_license=False)
self.assertTrue(
    source.find("const unsigned char foo[] DATA_ALIGN_ATTRIBUTE = {"))
self.assertTrue(source.find("""    0x00, 0x01,
    0x02, 0x23,"""))
self.assertNotEqual(-1, source.find("const int foo_len = 4;"))
self.assertEqual(-1, source.find("/* Copyright"))
self.assertEqual(-1, source.find("#include " ""))
self.assertNotEqual(-1, header.find("extern const unsigned char foo[];"))
self.assertNotEqual(-1, header.find("extern const int foo_len;"))
self.assertEqual(-1, header.find("/* Copyright"))

source, header = util.convert_bytes_to_c_source(
    b"\xff\xfe\xfd\xfc",
    "bar",
    80,
    include_guard="MY_GUARD",
    include_path="my/guard.h",
    use_tensorflow_license=True)
self.assertNotEqual(
    -1, source.find("const unsigned char bar[] DATA_ALIGN_ATTRIBUTE = {"))
self.assertNotEqual(-1, source.find("""    0xff, 0xfe, 0xfd, 0xfc,"""))
self.assertNotEqual(-1, source.find("/* Copyright"))
self.assertNotEqual(-1, source.find("#include \"my/guard.h\""))
self.assertNotEqual(-1, header.find("#ifndef MY_GUARD"))
self.assertNotEqual(-1, header.find("#define MY_GUARD"))
self.assertNotEqual(-1, header.find("/* Copyright"))
