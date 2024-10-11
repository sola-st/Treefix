# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
input_examples_str = 'inputs=[{"text":["foo"], "bytes":[b"bar"]}]'
input_dict = saved_model_cli.preprocess_input_examples_arg_string(
    input_examples_str)
feature = example_pb2.Example.FromString(input_dict['inputs'][0])
self.assertProtoEquals(
    """
          features {
            feature {
              key: "bytes"
              value {
                bytes_list {
                  value: "bar"
                }
              }
            }
            feature {
              key: "text"
              value {
                bytes_list {
                  value: "foo"
                }
              }
            }
          }
    """, feature)
