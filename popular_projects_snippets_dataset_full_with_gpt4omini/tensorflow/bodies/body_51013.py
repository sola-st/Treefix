# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/method_name_updater_test.py
path = os.path.join(
    compat.as_bytes(self._saved_model_path),
    compat.as_bytes(constants.SAVED_MODEL_FILENAME_PBTXT))
file_io.write_string_to_file(path, str(_SAVED_MODEL_PROTO))

updater = method_name_updater.MethodNameUpdater(self._saved_model_path)
updater.replace_method_name(
    signature_key="foo", method_name="regress", tags="serve")
updater.replace_method_name(
    signature_key="bar", method_name="classify", tags=["gpu", "serve"])

new_export_dir = tempfile.mkdtemp(prefix=test.get_temp_dir())
updater.save(new_export_dir)

self.assertTrue(
    file_io.file_exists(
        os.path.join(
            compat.as_bytes(new_export_dir),
            compat.as_bytes(constants.SAVED_MODEL_FILENAME_PBTXT))))
actual = loader.parse_saved_model(new_export_dir)
self.assertProtoEquals(
    actual,
    text_format.Parse(
        """
        saved_model_schema_version: 1
        meta_graphs {
          meta_info_def {
            tags: "serve"
          }
          signature_def: {
            key: "serving_default"
            value: {
              inputs: {
                key: "inputs"
                value { name: "input_node:0" }
              }
              method_name: "predict"
              outputs: {
                key: "outputs"
                value {
                  dtype: DT_FLOAT
                  tensor_shape {
                    dim { size: -1 }
                    dim { size: 100 }
                  }
                }
              }
            }
          }
          signature_def: {
            key: "foo"
            value: {
              inputs: {
                key: "inputs"
                value { name: "input_node:0" }
              }
              method_name: "regress"
              outputs: {
                key: "outputs"
                value {
                  dtype: DT_FLOAT
                  tensor_shape { dim { size: 1 } }
                }
              }
            }
          }
        }
        meta_graphs {
          meta_info_def {
            tags: "serve"
            tags: "gpu"
          }
          signature_def: {
            key: "serving_default"
            value: {
              inputs: {
                key: "inputs"
                value { name: "input_node:0" }
              }
              method_name: "predict"
              outputs: {
                key: "outputs"
                value {
                  dtype: DT_FLOAT
                  tensor_shape {
                    dim { size: -1 }
                  }
                }
              }
            }
          }
          signature_def: {
            key: "bar"
            value: {
              inputs: {
                key: "inputs"
                value { name: "input_node:0" }
              }
              method_name: "classify"
              outputs: {
                key: "outputs"
                value {
                  dtype: DT_FLOAT
                  tensor_shape { dim { size: 1 } }
                }
              }
            }
          }
        }
    """, saved_model_pb2.SavedModel()))
