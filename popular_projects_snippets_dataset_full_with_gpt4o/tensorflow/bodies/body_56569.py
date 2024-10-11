# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/visualize.py
try:
    tflite_input = argv[1]
    html_output = argv[2]
except IndexError:
    print("Usage: %s <input tflite> <output html>" % (argv[0]))
else:
    html = create_html(tflite_input)
    with open(html_output, "w") as output_file:
        output_file.write(html)
