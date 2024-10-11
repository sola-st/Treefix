# Extracted from ./data/repos/tensorflow/tensorflow/lite/toco/logging/gen_html.py
"""Reads the HTML template content.

    Args:
      html_template_path: A string, path to the template HTML file.
      export_report_path: A string, path to the generated HTML report. This path
        should point to a '.html' file with date and time in its name.
        e.g. 2019-01-01-10:05.toco_report.html.

    Raises:
      IOError: File doesn't exist.
    """
# Load the template HTML.
if not _file_io.file_exists(html_template_path):
    raise IOError("File '{0}' does not exist.".format(html_template_path))
with _file_io.FileIO(html_template_path, "r") as f:
    self.html_template = f.read()

_file_io.recursive_create_dir(os.path.dirname(export_report_path))
self.export_report_path = export_report_path
