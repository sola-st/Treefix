# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/pretty_printer.py
printer = PrettyPrinter(color, noanno)
if isinstance(node, (list, tuple)):
    for n in node:
        printer.visit(n)
else:
    printer.visit(node)
exit(printer.result)
