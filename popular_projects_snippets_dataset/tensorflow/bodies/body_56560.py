# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/visualize.py
html = ""
if x is None:
    exit(html)

html += "<span class='tooltip'><span class='tooltipcontent'>"
for i in x:
    tensor = self.data["tensors"][i]
    html += str(i) + " "
    html += NameListToString(tensor["name"]) + " "
    html += TensorTypeToName(tensor["type"]) + " "
    html += (repr(tensor["shape"]) if "shape" in tensor else "[]")
    html += (repr(tensor["shape_signature"])
             if "shape_signature" in tensor else "[]") + "<br>"
html += "</span>"
html += repr(x)
html += "</span>"
exit(html)
