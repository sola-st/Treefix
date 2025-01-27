# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared_test.py
tf_error = errors.OpError(None, self.var_a.initializer, "foo description",
                          None)

error_intro = cli_shared.get_error_intro(tf_error)

self.assertEqual("!!! An error occurred during the run !!!",
                 error_intro.lines[1])
self.assertEqual([(0, len(error_intro.lines[1]), "blink")],
                 error_intro.font_attr_segs[1])

self.assertEqual(2, error_intro.lines[4].index("ni -a -d -t a/Assign"))
self.assertEqual(2, error_intro.font_attr_segs[4][0][0])
self.assertEqual(22, error_intro.font_attr_segs[4][0][1])
self.assertEqual("ni -a -d -t a/Assign",
                 error_intro.font_attr_segs[4][0][2][0].content)
self.assertEqual("bold", error_intro.font_attr_segs[4][0][2][1])

self.assertEqual(2, error_intro.lines[6].index("li -r a/Assign"))
self.assertEqual(2, error_intro.font_attr_segs[6][0][0])
self.assertEqual(16, error_intro.font_attr_segs[6][0][1])
self.assertEqual("li -r a/Assign",
                 error_intro.font_attr_segs[6][0][2][0].content)
self.assertEqual("bold", error_intro.font_attr_segs[6][0][2][1])

self.assertEqual(2, error_intro.lines[8].index("lt"))
self.assertEqual(2, error_intro.font_attr_segs[8][0][0])
self.assertEqual(4, error_intro.font_attr_segs[8][0][1])
self.assertEqual("lt", error_intro.font_attr_segs[8][0][2][0].content)
self.assertEqual("bold", error_intro.font_attr_segs[8][0][2][1])

self.assertStartsWith(error_intro.lines[11], "Op name:")
self.assertTrue(error_intro.lines[11].endswith("a/Assign"))

self.assertStartsWith(error_intro.lines[12], "Error type:")
self.assertTrue(error_intro.lines[12].endswith(str(type(tf_error))))

self.assertEqual("Details:", error_intro.lines[14])
self.assertStartsWith(error_intro.lines[15], "foo description")
