# Extracted from ./data/repos/tensorflow/tensorflow/python/types/core.py
"""Returns compiler IR for the compiled function.

    This API is intended *only* for debugging as there are no guarantees on
    backwards compatibility of returned IR or the allowed values of `stage`.

    Args:
      *args: compilation args supports inputs either: (1) all inputs are
        TensorSpec or (2) all inputs are tf.Tensor/Python variables.
      **kwargs: Keyword arguments used for compilation. Same requirement as
        compiliation args.

    Returns:
      Function callable with the following kwargs:
        - `stage` at which the compiler IR should be serialized. Allowed values
          are:
           - `hlo`: HLO output after conversion from TF
            (https://www.tensorflow.org/xla/operation_semantics).
           - `hlo_serialized`: Like stage=`hlo`, but the output is a serialized
             HLO module proto (a bytes object).
           - `optimized_hlo`: HLO after compiler optimizations.
           - `optimized_hlo_serialized`: Like stage=`optimized_hlo`, but the
             output is a serialized HLO module proto (a bytes object).
           - `optimized_hlo_dot`: optimized HLO in DOT format suitable for
             Graphviz.
        - `device_name` can be either None, in which case the preferred device
          is used for compilation, or a device name. It can be a full device
          name, or a partial one, e.g., `/device:CPU:0`.

      For example, for

      ```python
      @tf.function(jit_compile=True)
      def f(x):
        return x + 1

      f.experimental_get_compiler_ir(tf.random.normal([10, 10])(stage='hlo')
      ```

      the output is:

      ```
      HloModule a_inference_f_13__.9

      ENTRY %a_inference_f_13__.9 (arg0.1: f32[10,10]) -> f32[10,10] {
        %arg0.1 = f32[10,10]{1,0} parameter(0), parameter_replication={false}
        %reshape.2 = f32[10,10]{1,0} reshape(f32[10,10]{1,0} %arg0.1)
        %constant.3 = f32[] constant(1)
        %broadcast.4 = f32[10,10]{1,0} broadcast(f32[] %constant.3)
        %add.5 = f32[10,10]{1,0} add(f32[10,10]{1,0} %reshape.2,
                                     f32[10,10]{1,0} %broadcast.4)
        %reshape.6 = f32[10,10]{1,0} reshape(f32[10,10]{1,0} %add.5)
        %tuple.7 = (f32[10,10]{1,0}) tuple(f32[10,10]{1,0} %reshape.6)
        ROOT %get-tuple-element.8 = f32[10,10]{1,0}
          get-tuple-element((f32[10,10]{1,0}) %tuple.7), index=0
      }
      ```

    Raises:
      ValueError:
        (1) If an invalid `stage` is selected
        (2) or if applied to a function which is not compiled
        (`jit_compile=True` is not set).
        (3) or if input shapes are not fully defined for tf.TensorSpec inputs
      TypeError: When called with input in graph mode.
    """
pass
