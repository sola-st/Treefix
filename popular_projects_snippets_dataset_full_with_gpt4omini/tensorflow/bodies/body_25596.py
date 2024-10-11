# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
parsed = self._arg_parsers["eval"].parse_args(args)

eval_res = self._evaluator.evaluate(parsed.expression)

np_printoptions = cli_shared.numpy_printoptions_from_screen_info(
    screen_info)
exit(cli_shared.format_tensor(
    eval_res,
    "from eval of expression '%s'" % parsed.expression,
    np_printoptions,
    print_all=parsed.print_all,
    include_numeric_summary=True,
    write_path=parsed.write_path))
