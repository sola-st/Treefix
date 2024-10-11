# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
with self.assertRaisesRegex(ValueError, "2 MetaGraphs"):
    load.load(self._v1_multi_metagraph_saved_model())
first_imported = load.load(self._v1_multi_metagraph_saved_model(),
                           tags=["first"])
self.assertEqual({"first_output": 42.},
                 self.evaluate(first_imported.signatures["first_key"](
                     first_start=constant_op.constant(2.))))
second_imported = load.load(self._v1_multi_metagraph_saved_model(),
                            tags=set(["second"]))
with self.assertRaisesRegex(TypeError, "second_start"):
    second_imported.signatures["second_key"](x=constant_op.constant(2.))
with self.assertRaisesRegex(TypeError, "second_start"):
    second_imported.signatures["second_key"](
        second_start=constant_op.constant(2.),
        x=constant_op.constant(2.))
self.assertEqual({"second_output": 21.},
                 self.evaluate(second_imported.signatures["second_key"](
                     second_start=constant_op.constant(2.))))
