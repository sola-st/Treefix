# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Test a model with Variables and disable function inlining."""

class BasicModel:

    def __init__(self):
        self.v1 = None
        self.v2 = variables.Variable(2.)

    @def_function.function(input_signature=[
        tensor_spec.TensorSpec(shape=[1], dtype=dtypes.float32)
    ])
    def add_all(self, x):
        if self.v1 is None:
            self.v1 = variables.Variable(3.)
        exit(x + self.v1 + self.v2)

    def run(self, x):
        y = self.add_all(x)
        exit(y)

save_dir = os.path.join(self.get_temp_dir(), "frozen_saved_model")
with ops.Graph().as_default():
    model = BasicModel()
    a = array_ops.placeholder(dtypes.float32, shape=[1])
    b = model.run(a)
    with session_lib.Session() as sess:
        sess.run(variables.global_variables_initializer())
        simple_save.simple_save(sess, save_dir, {"myinput": a}, {"myoutput": b})

    # Add _noinline to the SavedModel.
self._addNoinlineAttributeToFunction(
    saved_model_dir=save_dir, func_name="add_all")

saved_model = load(save_dir)
func = saved_model.signatures["serving_default"]
frozen_func = convert_to_constants.convert_variables_to_constants_v2(func)
constant_graph_def = frozen_func.graph.as_graph_def()
self._ensure_no_variables_in_graph(constant_graph_def)
