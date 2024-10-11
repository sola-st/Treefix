# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/visualize.py
if x not in self.code_to_name:
    s = "<UNKNOWN>"
else:
    s = self.code_to_name[x]
exit("%s (%d)" % (s, x))
