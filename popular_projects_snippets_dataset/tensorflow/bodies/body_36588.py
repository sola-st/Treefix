# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
serialized = """node {
      name: "Const"
      op: "Const"
      attr {
        key: "dtype"
        value {
          type: DT_FLOAT
        }
      }
      attr {
        key: "value"
        value {
          tensor {
            dtype: DT_FLOAT
            tensor_shape {
            }
            float_val: 1.0
          }
        }
      }
    }
    node {
      name: "while/maximum_iterations"
      op: "Const"
      attr {
        key: "dtype"
        value {
          type: DT_INT32
        }
      }
      attr {
        key: "value"
        value {
          tensor {
            dtype: DT_INT32
            tensor_shape {
            }
            int_val: -1
          }
        }
      }
    }
    node {
      name: "while/loop_counter"
      op: "Const"
      attr {
        key: "dtype"
        value {
          type: DT_INT32
        }
      }
      attr {
        key: "value"
        value {
          tensor {
            dtype: DT_INT32
            tensor_shape {
            }
            int_val: 0
          }
        }
      }
    }
    node {
      name: "while"
      op: "StatelessWhile"
      input: "while/loop_counter"
      input: "while/maximum_iterations"
      input: "Const"
      attr {
        key: "T"
        value {
          list {
            type: DT_INT32
            type: DT_INT32
            type: DT_FLOAT
          }
        }
      }
      attr {
        key: "_lower_using_switch_merge"
        value {
          b: true
        }
      }
      attr {
        key: "_num_original_outputs"
        value {
          i: 3
        }
      }
      attr {
        key: "_read_only_resource_inputs"
        value {
          list {
          }
        }
      }
      attr {
        key: "body"
        value {
          func {
            name: "while_body_822"
          }
        }
      }
      attr {
        key: "cond"
        value {
          func {
            name: "while_cond_821"
          }
        }
      }
      attr {
        key: "output_shapes"
        value {
          list {
            shape {
            }
            shape {
            }
            shape {
            }
          }
        }
      }
      attr {
        key: "parallel_iterations"
        value {
          i: 10
        }
      }
    }
    node {
      name: "while/Identity"
      op: "Identity"
      input: "while"
      attr {
        key: "T"
        value {
          type: DT_INT32
        }
      }
    }
    node {
      name: "while/Identity_1"
      op: "Identity"
      input: "while:1"
      attr {
        key: "T"
        value {
          type: DT_INT32
        }
      }
    }
    node {
      name: "while/Identity_2"
      op: "Identity"
      input: "while:2"
      attr {
        key: "T"
        value {
          type: DT_FLOAT
        }
      }
    }
    library {
      function {
        signature {
          name: "while_body_822"
          input_arg {
            name: "while_loop_counter"
            type: DT_INT32
          }
          input_arg {
            name: "while_maximum_iterations_0"
            type: DT_INT32
          }
          input_arg {
            name: "placeholder"
            type: DT_FLOAT
          }
          output_arg {
            name: "add"
            type: DT_INT32
          }
          output_arg {
            name: "while_maximum_iterations"
            type: DT_INT32
          }
          output_arg {
            name: "partitionedcall"
            type: DT_FLOAT
          }
        }
        node_def {
          name: "PartitionedCall"
          op: "PartitionedCall"
          input: "placeholder"
          attr {
            key: "Tin"
            value {
              list {
                type: DT_FLOAT
              }
            }
          }
          attr {
            key: "Tout"
            value {
              list {
                type: DT_FLOAT
              }
            }
          }
          attr {
            key: "_collective_manager_ids"
            value {
              list {
              }
            }
          }
          attr {
            key: "_read_only_resource_inputs"
            value {
              list {
              }
            }
          }
          attr {
            key: "config"
            value {
              s: ""
            }
          }
          attr {
            key: "config_proto"
            value {
              s: ""
            }
          }
          attr {
            key: "executor_type"
            value {
              s: ""
            }
          }
          attr {
            key: "f"
            value {
              func {
                name: "__inference_f_841"
              }
            }
          }
          experimental_debug_info {
            original_node_names: "PartitionedCall"
          }
        }
        node_def {
          name: "add/y"
          op: "Const"
          attr {
            key: "dtype"
            value {
              type: DT_INT32
            }
          }
          attr {
            key: "value"
            value {
              tensor {
                dtype: DT_INT32
                tensor_shape {
                }
                int_val: 1
              }
            }
          }
          experimental_debug_info {
            original_node_names: "add/y"
          }
        }
        node_def {
          name: "add_0"
          op: "AddV2"
          input: "while_loop_counter"
          input: "add/y:output:0"
          attr {
            key: "T"
            value {
              type: DT_INT32
            }
          }
          experimental_debug_info {
            original_node_names: "add"
          }
        }
        ret {
          key: "add"
          value: "add_0:z:0"
        }
        ret {
          key: "partitionedcall"
          value: "PartitionedCall:output:0"
        }
        ret {
          key: "while_maximum_iterations"
          value: "while_maximum_iterations_0"
        }
        arg_attr {
          key: 0
          value {
            attr {
              key: "_output_shapes"
              value {
                list {
                  shape {
                  }
                }
              }
            }
          }
        }
        arg_attr {
          key: 1
          value {
            attr {
              key: "_output_shapes"
              value {
                list {
                  shape {
                  }
                }
              }
            }
          }
        }
        arg_attr {
          key: 2
          value {
            attr {
              key: "_output_shapes"
              value {
                list {
                  shape {
                  }
                }
              }
            }
          }
        }
      }
      function {
        signature {
          name: "while_cond_821"
          input_arg {
            name: "while_loop_counter"
            type: DT_INT32
          }
          input_arg {
            name: "while_maximum_iterations"
            type: DT_INT32
          }
          input_arg {
            name: "placeholder"
            type: DT_FLOAT
          }
          output_arg {
            name: "less"
            type: DT_BOOL
          }
        }
        node_def {
          name: "Less/y"
          op: "Const"
          attr {
            key: "dtype"
            value {
              type: DT_FLOAT
            }
          }
          attr {
            key: "value"
            value {
              tensor {
                dtype: DT_FLOAT
                tensor_shape {
                }
                float_val: 5.0
              }
            }
          }
          experimental_debug_info {
            original_node_names: "Less/y"
          }
        }
        node_def {
          name: "Less"
          op: "Less"
          input: "placeholder"
          input: "Less/y:output:0"
          attr {
            key: "T"
            value {
              type: DT_FLOAT
            }
          }
          experimental_debug_info {
            original_node_names: "Less"
          }
        }
        ret {
          key: "less"
          value: "Less:z:0"
        }
        arg_attr {
          key: 0
          value {
            attr {
              key: "_output_shapes"
              value {
                list {
                  shape {
                  }
                }
              }
            }
          }
        }
        arg_attr {
          key: 1
          value {
            attr {
              key: "_output_shapes"
              value {
                list {
                  shape {
                  }
                }
              }
            }
          }
        }
        arg_attr {
          key: 2
          value {
            attr {
              key: "_output_shapes"
              value {
                list {
                  shape {
                  }
                }
              }
            }
          }
        }
      }
      function {
        signature {
          name: "__inference_f_841"
          input_arg {
            name: "mul_placeholder"
            type: DT_FLOAT
          }
          output_arg {
            name: "identity"
            type: DT_FLOAT
          }
        }
        node_def {
          name: "mul/y"
          op: "Const"
          attr {
            key: "dtype"
            value {
              type: DT_FLOAT
            }
          }
          attr {
            key: "value"
            value {
              tensor {
                dtype: DT_FLOAT
                tensor_shape {
                }
                float_val: 2.0
              }
            }
          }
          experimental_debug_info {
            original_node_names: "mul/y"
          }
        }
        node_def {
          name: "mul"
          op: "Mul"
          input: "mul_placeholder"
          input: "mul/y:output:0"
          attr {
            key: "T"
            value {
              type: DT_FLOAT
            }
          }
          experimental_debug_info {
            original_node_names: "mul"
          }
        }
        node_def {
          name: "Identity"
          op: "Identity"
          input: "mul:z:0"
          attr {
            key: "T"
            value {
              type: DT_FLOAT
            }
          }
          experimental_debug_info {
            original_node_names: "Identity"
          }
        }
        ret {
          key: "identity"
          value: "Identity:output:0"
        }
        arg_attr {
          key: 0
          value {
            attr {
              key: "_output_shapes"
              value {
                list {
                  shape {
                  }
                }
              }
            }
          }
        }
      }
    }
    versions {
      producer: 399
      min_consumer: 12
    }
    """
# Code for generating above graph:
#
# def Body(i):
#   @tf.function
#   def f():
#     return i * 2
#   return f()
# tf.while_loop(lambda i: i < 5., Body, [tf.constant(1.)])
graph_def = graph_pb2.GraphDef()
text_format.Parse(serialized, graph_def)
@def_function.function
def F():
    x, y = importer.import_graph_def(
        graph_def, return_elements=["Const:0", "while:2"])
    grad_out, = gradients_impl.gradients(y, x)
    exit(grad_out)
self.assertAllEqual(F(), 8.0)
