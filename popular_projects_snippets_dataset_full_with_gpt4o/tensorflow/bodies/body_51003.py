# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir(
    "test_strip_default_attrs_no_consumer_defaults")
builder = saved_model_builder._SavedModelBuilder(export_dir)

# Add a graph with a single variable and a test op with a defaultless
# float32 attr, "test_attr".
with session.Session(graph=ops.Graph()) as sess:
    variables.VariableV1(1.0, dtype=dtypes.float64, name="var")
    test_ops.test_attr(T=dtypes.float32, name="test_attr")
    self.evaluate(variables.global_variables_initializer())
    builder.add_meta_graph_and_variables(sess, ["foo"])

# Save the SavedModel to disk in text format.
builder.save(as_text=True)

# Rewrite the SavedModel to remove the T attr from "test_attr".
saved_model_file = os.path.join(
    export_dir, constants.SAVED_MODEL_FILENAME_PBTXT)
with open(saved_model_file) as f:
    original_saved_model = f.read()

no_attr_saved_model = original_saved_model.replace("""
      attr {
        key: "T"
        value {
          type: DT_FLOAT
        }
      }""", "")
with open(saved_model_file, "w") as f:
    f.write(no_attr_saved_model)

# Loading the SavedModel via the loader must fail because the SavedModel
# does not have any attr values for the "TestAttr" node, and there is no
# default specified in the TestAttr OpDef.
sess = session.Session(graph=ops.Graph())
with self.assertRaisesRegex(
    ValueError, "NodeDef missing attr 'T' from Op<name=TestAttr"):
    loader.load(sess, ["foo"], export_dir)

# Rewrite the SavedModel to change the type of the T attr in "test_attr"
bad_type_saved_model = original_saved_model.replace("""
      attr {
        key: "T"
        value {
          type: DT_FLOAT
        }
      }""", """
      attr {
        key: "T"
        value {
          type: DT_DOUBLE
        }
      }""")
with open(saved_model_file, "w") as f:
    f.write(bad_type_saved_model)

# Loading the SavedModel via the loader must fail because there is no
# OpKernel registered to handle T = double.
sess = session.Session(graph=ops.Graph())
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "(?s)No OpKernel was registered.*DOUBLE"):
    loader.load(sess, ["foo"], export_dir)
