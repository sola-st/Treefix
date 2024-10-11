# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/define_op_template.py
if FLAGS.gen_register_op:
    assert FLAGS.output.endswith('.cc')
    generated_code = gen_register_op(sys.modules[__name__], '_composite_')
else:
    assert FLAGS.output.endswith('.mlir')
    generated_code = tfr_gen_from_module(sys.modules[__name__], '_composite_')

dirname = os.path.dirname(FLAGS.output)
if not os.path.exists(dirname):
    os.makedirs(dirname)
with open(FLAGS.output, 'w') as f:
    f.write(generated_code)
