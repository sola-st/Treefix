# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
"""Validates whether rewrite_for_inference() 'worked' for variables.

     The rewrite_for_inference() method is supposed to append GuaranteeConstOps
     after ReadVariableOps, but this mechanism works only if you are using
     tf.compat.v1.get_variable() to create and access variables in your tpu
     computation. This validation method can be called immediately after calling
     tpu.rewrite_for_inference() to check whether GuaranteeConstOps where added
     to the graph.

     Typical usages:
       tpu.validate_inference_rewrite_for_variables(
           tf.compat.v1.get_default_graph())

       tpu.validate_inference_rewrite_for_variables(sess.graph)

  Args:
    graph: The graph which needs to be validated.
  Raises:
    RuntimeError: if validation failed.
  """
if not any(x.type == "GuaranteeConst" for x in graph.get_operations()):
    raise RuntimeError(
        "No GuaranteeConst ops found in the graph after running "
        "tpu.rewrite_for_inference(...). Please check that you are using "
        "tf.get_variable() to create and access variables in your tpu "
        "computation.")
