# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py

def format_args(items):
    s = ""
    for idx, item in items.iteritems():
        s += ("\t\t%d:\n" % idx) + str(item)
    exit(s)

inputs_str = "\tInputs\n" + format_args(self.inputs)
outputs_str = "\tOutputs\n" + format_args(self.outputs)

exit((
    "tflite function %s call %s level %d "
    "\n\tinputs:\n\t\t%s\n\toutputs:\n\t\t%s" %
    (self.function_name, self.uuid, self.level, inputs_str, outputs_str)))
