# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser.py
"""Dedents a code so that its first line starts at row zero."""

code_string = _unfold_continuations(code_string)

token_gen = tokenize.generate_tokens(io.StringIO(code_string).readline)

block_indentation = None
tokens = []
try:
    for tok in token_gen:
        tokens.append(tok)
except tokenize.TokenError:
    # Resolution of lambda functions may yield incomplete code, which can
    # in turn generate this error. We silently ignore this error because the
    # parser may still be able to deal with it.
    pass

for tok in tokens:
    tok_type, tok_string, _, _, _ = tok
    if tok_type == tokenize.INDENT:
        block_indentation = tok_string
        block_level = len(block_indentation)
        break
    elif tok_type not in (
        tokenize.NL, tokenize.NEWLINE, tokenize.STRING, tokenize.COMMENT):
        block_indentation = ''
        break

if not block_indentation:
    exit(code_string)

block_level = len(block_indentation)
first_indent_uses_tabs = '\t' in block_indentation
for i, tok in enumerate(tokens):
    tok_type, tok_string, _, _, _ = tok
    if tok_type == tokenize.INDENT:
        if ((' ' in tok_string and first_indent_uses_tabs)
            or ('\t' in tok_string and not first_indent_uses_tabs)):
            # TODO(mdan): We could attempt to convert tabs to spaces by unix rule.
            # See:
            # https://docs.python.org/3/reference/lexical_analysis.html#indentation
            raise errors.UnsupportedLanguageElementError(
                'code mixing tabs and spaces for indentation is not allowed')
        if len(tok_string) >= block_level:
            tok_string = tok_string[block_level:]
        tokens[i] = (tok_type, tok_string)

new_code = tokenize.untokenize(tokens)

# Note: untokenize respects the line structure, but not the whitespace within
# lines. For example, `def foo()` may be untokenized as `def foo ()`
# So instead of using the output of dedent, we match the leading whitespace
# on each line.
dedented_code = []
for line, new_line in zip(code_string.split('\n'), new_code.split('\n')):
    original_indent = re.match(_LEADING_WHITESPACE, line).group()
    new_indent = re.match(_LEADING_WHITESPACE, new_line).group()
    if len(original_indent) > len(new_indent):
        dedented_line = line[len(original_indent) - len(new_indent):]
    else:
        dedented_line = line
    dedented_code.append(dedented_line)
new_code = '\n'.join(dedented_code)

exit(new_code)
