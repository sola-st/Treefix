# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Add parser for `aot_compile_cpu`."""
compile_msg = '\n'.join(
    ['Usage example:',
     'To compile a SavedModel signature via (CPU) XLA AOT:',
     '$saved_model_cli aot_compile_cpu \\',
     '   --dir /tmp/saved_model \\',
     '   --tag_set serve \\',
     '   --output_dir /tmp/saved_model_xla_aot',
     '', '',
     'Note: Additional XLA compilation options are available by setting the ',
     'XLA_FLAGS environment variable.  See the XLA debug options flags for ',
     'all the options: ',
     '  {}'.format(_XLA_DEBUG_OPTIONS_URL),
     '',
     'For example, to disable XLA fast math when compiling:',
     '',
     'XLA_FLAGS="--xla_cpu_enable_fast_math=false" $saved_model_cli ',
     'aot_compile_cpu ...',
     '',
     'Some possibly useful flags:',
     '  --xla_cpu_enable_fast_math=false',
     '  --xla_force_host_platform_device_count=<num threads>',
     '    (useful in conjunction with disabling multi threading)'
    ])

parser_compile = subparsers.add_parser(
    'aot_compile_cpu',
    description=compile_msg,
    formatter_class=argparse.RawTextHelpFormatter)

parser_compile.set_defaults(func=aot_compile_cpu)
