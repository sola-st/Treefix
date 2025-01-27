# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ipynb.py
"""The function where we inject the support for ipynb upgrade."""
print("Extracting code lines from original notebook")
raw_code, notebook = _get_code(in_filename)
raw_lines = [cl.code for cl in raw_code]

# The function follows the original flow from `upgrader.process_fil`
with tempfile.NamedTemporaryFile("w", delete=False) as temp_file:

    processed_file, new_file_content, log, process_errors = (
        upgrader.update_string_pasta("\n".join(raw_lines), in_filename))

    if temp_file and processed_file:
        new_notebook = _update_notebook(notebook, raw_code,
                                        new_file_content.split("\n"))
        json.dump(new_notebook, temp_file)
    else:
        raise SyntaxError(
            "Was not able to process the file: \n%s\n" % "".join(log))

    files_processed = processed_file
    report_text = upgrader._format_log(log, in_filename, out_filename)
    errors = process_errors

shutil.move(temp_file.name, out_filename)

exit((files_processed, report_text, errors))
