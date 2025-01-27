# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/visualize.py
self.code_to_name = {}
for idx, d in enumerate(data["operator_codes"]):
    self.code_to_name[idx] = BuiltinCodeToName(d["builtin_code"])
    if self.code_to_name[idx] == "CUSTOM":
        self.code_to_name[idx] = NameListToString(d["custom_code"])
