# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/generate_examples_report.py
"""Make an HTML report of the success/failure reports.

  Args:
    fp: File-like object in which to put the html.
    title: "Title of the zip file this pertains to."
    reports: a list of conversion attempts. (report_args, report_vals) i.e.
      ({"shape": [1,2,3], "type": "tf.float32"},
       {"tf": "SUCCESS", "tflite_converter": "FAILURE",
        "tf_log": "", "tflite_converter_log": "Unsupported type."})
  """
# sort reports by if TFLite converter failure and then TF failure (reversed)
reports.sort(key=lambda x: x[1]["tflite_converter"], reverse=False)
reports.sort(key=lambda x: x[1]["tf"], reverse=True)
def result_cell(x, row, col):
    """Produce a cell with the condition string `x`."""
    s = html.escape(repr(x), quote=True)
    color = "#44ff44" if x == SUCCESS else (
        "#ff4444" if x == FAILED else "#eeeeee")
    handler = "ShowLog(%d, %d)" % (row, col)
    fp.write("<td style='background-color: %s' onclick='%s'>%s</td>\n" % (
        color, handler, s))

fp.write("""<html>
<head>
<title>tflite report</title>
<style>
body { font-family: Arial; }
th { background-color: #555555; color: #eeeeee; }
td { vertical-align: top; }
td.horiz {width: 50%;}
pre { white-space: pre-wrap; word-break: keep-all; }
table {width: 100%;}
</style>
</head>
""")
# Write the log data to a javascript variable and also make a function
# in javascript to show the log when an item is clicked.
fp.write("<script> \n")
fp.write("""
function ShowLog(row, col) {

var log = document.getElementById("log");
log.innerHTML = "<pre>" + data[row][col]  + "</pre>";
}
""")
fp.write("var data = \n")
logs = json.dumps([[escape_and_normalize(x[1]["tf_log"]),
                    escape_and_normalize(x[1]["tflite_converter_log"])
                   ] for x in reports])
fp.write(logs)
fp.write(";</script>\n")

# Write the main table and use onclick on the items that have log items.
fp.write("""
<body>
<h1>TensorFlow Lite Conversion</h1>
<h2>%s</h2>
""" % title)

# Get a list of keys that are in any of the records.
param_keys = {}
for params, _ in reports:
    for k in params.keys():
        param_keys[k] = True

fp.write("<table>\n")
fp.write("<tr><td class='horiz'>\n")
fp.write("<div style='height:1000px; overflow:auto'>\n")
fp.write("<table>\n")
fp.write("<tr>\n")
for p in param_keys:
    fp.write("<th>%s</th>\n" % html.escape(p, quote=True))
fp.write("<th>TensorFlow</th>\n")
fp.write("<th>TensorFlow Lite Converter</th>\n")
fp.write("</tr>\n")
for idx, (params, vals) in enumerate(reports):
    fp.write("<tr>\n")
    for p in param_keys:
        fp.write("  <td>%s</td>\n" %
                 html.escape(repr(params.get(p, None)), quote=True))

    result_cell(vals["tf"], idx, 0)
    result_cell(vals["tflite_converter"], idx, 1)
    fp.write("</tr>\n")
fp.write("</table>\n")
fp.write("</div>\n")
fp.write("</td>\n")
fp.write("<td class='horiz' id='log'></td></tr>\n")
fp.write("</table>\n")
fp.write("<script>\n")
fp.write("</script>\n")
fp.write("""
    </body>
    </html>
    """)
