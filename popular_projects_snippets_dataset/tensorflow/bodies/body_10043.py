# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
logging.set_verbosity(logging.INFO)

def smcli_main(argv):
    parser = create_parser()
    if len(argv) < 2:
        parser.error('Too few arguments.')
    flags.mark_flags_as_required(command_required_flags[argv[1]])
    args = parser.parse_args()
    args.func()

app.run(smcli_main)
