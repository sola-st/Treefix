# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_test.py
def _test(input, output):  # pylint: disable=redefined-builtin
    _, unused_report, errors, new_text = self._upgrade(input)
    self.assertEqual(new_text, output)
_test("tf.concat(0,  \t[x for x in y])\n",
      "tf.concat(axis=0,  \tvalues=[x for x in y])\n")
_test("tf.concat(0,[x for x in y])\n",
      "tf.concat(axis=0,values=[x for x in y])\n")
_test("tf.concat(0,[\nx for x in y])\n",
      "tf.concat(axis=0,values=[\nx for x in y])\n")
_test("tf.concat(0,[\n \tx for x in y])\n",
      "tf.concat(axis=0,values=[\n \tx for x in y])\n")
