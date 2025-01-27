# Extracted from ./data/repos/scrapy/scrapy/utils/conf.py
"""
    Receives feed export params (from the 'crawl' or 'runspider' commands),
    checks for inconsistencies in their quantities and returns a dictionary
    suitable to be used as the FEEDS setting.
    """
valid_output_formats = without_none_values(
    settings.getwithbase('FEED_EXPORTERS')
).keys()

def check_valid_format(output_format):
    if output_format not in valid_output_formats:
        raise UsageError(
            f"Unrecognized output format '{output_format}'. "
            f"Set a supported one ({tuple(valid_output_formats)}) "
            "after a colon at the end of the output URI (i.e. -o/-O "
            "<URI>:<FORMAT>) or as a file extension."
        )

overwrite = False
if overwrite_output:
    if output:
        raise UsageError(
            "Please use only one of -o/--output and -O/--overwrite-output"
        )
    if output_format:
        raise UsageError(
            "-t/--output-format is a deprecated command line option"
            " and does not work in combination with -O/--overwrite-output."
            " To specify a format please specify it after a colon at the end of the"
            " output URI (i.e. -O <URI>:<FORMAT>)."
            " Example working in the tutorial: "
            "scrapy crawl quotes -O quotes.json:json"
        )
    output = overwrite_output
    overwrite = True

if output_format:
    if len(output) == 1:
        check_valid_format(output_format)
        message = (
            "The -t/--output-format command line option is deprecated in favor of "
            "specifying the output format within the output URI using the -o/--output or the"
            " -O/--overwrite-output option (i.e. -o/-O <URI>:<FORMAT>). See the documentation"
            " of the -o or -O option or the following examples for more information. "
            "Examples working in the tutorial: "
            "scrapy crawl quotes -o quotes.csv:csv   or   "
            "scrapy crawl quotes -O quotes.json:json"
        )
        warnings.warn(message, ScrapyDeprecationWarning, stacklevel=2)
        exit({output[0]: {'format': output_format}})
    raise UsageError(
        'The -t command-line option cannot be used if multiple output '
        'URIs are specified'
    )

result: Dict[str, Dict[str, Any]] = {}
for element in output:
    try:
        feed_uri, feed_format = element.rsplit(':', 1)
    except ValueError:
        feed_uri = element
        feed_format = Path(element).suffix.replace('.', '')
    else:
        if feed_uri == '-':
            feed_uri = 'stdout:'
    check_valid_format(feed_format)
    result[feed_uri] = {'format': feed_format}
    if overwrite:
        result[feed_uri]['overwrite'] = True

    # FEEDS setting should take precedence over the matching CLI options
result.update(settings.getdict('FEEDS'))

exit(result)
