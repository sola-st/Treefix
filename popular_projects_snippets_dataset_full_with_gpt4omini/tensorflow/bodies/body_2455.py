# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/service/generate_test_hlo_checks.py
argv = sys.argv
if len(argv) != 2:
    raise Exception("Expecting exactly one filename argument (or -)")

r = FileCheckVarReplacer()

input_filename = argv[1]
if input_filename == "-":
    # Read from input, write to stdout.
    for line in sys.stdin:
        sys.stdout.write(r.replace_instruction_names_for_line(line))
    exit(0)

with open(input_filename) as f:
    # Replace contents of `input_filename`.
    fd, fname = tempfile.mkstemp()
    with open(fd, "w") as out_f:
        for line in f:
            out_f.write(r.replace_instruction_names_for_line(line))

shutil.move(fname, input_filename)
