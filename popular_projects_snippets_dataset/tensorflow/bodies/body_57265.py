# Extracted from ./data/repos/tensorflow/tensorflow/lite/toco/logging/gen_html.py
"""Generates the HTML report and writes it to local directory.

    This function uses the fields in `toco_conversion_log_before` and
    `toco_conversion_log_after` to populate the HTML content. Certain markers
    (placeholders) in the HTML template are then substituted with the fields
    from the protos. Once finished it will write the HTML file to the specified
    local file path.

    Args:
      toco_conversion_log_before: A `TocoConversionLog` protobuf generated
        before the model is converted by TOCO.
      toco_conversion_log_after: A `TocoConversionLog` protobuf generated after
        the model is converted by TOCO.
      post_training_quant_enabled: A boolean, whether post-training quantization
        is enabled.
      dot_before: A string, the dot representation of the model
        before the conversion.
      dot_after: A string, the dot representation of the model after
        the conversion.
      toco_err_log: A string, the logs emitted by TOCO during conversion. Caller
        need to ensure that this string is properly anonymized (any kind of
        user data should be eliminated).
      tflite_graph_path: A string, the filepath to the converted TFLite model.

    Raises:
      RuntimeError: When error occurs while generating the template.
    """
html_dict = {}
html_dict["<!--CONVERSION_STATUS-->"] = (
    r'<span class="label label-danger">Fail</span>'
) if toco_err_log else r'<span class="label label-success">Success</span>'
html_dict["<!--TOTAL_OPS_BEFORE_CONVERT-->"] = str(
    toco_conversion_log_before.model_size)
html_dict["<!--TOTAL_OPS_AFTER_CONVERT-->"] = str(
    toco_conversion_log_after.model_size)
html_dict["<!--BUILT_IN_OPS_COUNT-->"] = str(
    sum(toco_conversion_log_after.built_in_ops.values()))
html_dict["<!--SELECT_OPS_COUNT-->"] = str(
    sum(toco_conversion_log_after.select_ops.values()))
html_dict["<!--CUSTOM_OPS_COUNT-->"] = str(
    sum(toco_conversion_log_after.custom_ops.values()))
html_dict["<!--POST_TRAINING_QUANT_ENABLED-->"] = (
    "is" if post_training_quant_enabled else "isn't")

pre_op_profile = ""
post_op_profile = ""

# Generate pre-conversion op profiles as a list of HTML table rows.
for i in range(len(toco_conversion_log_before.op_list)):
    # Append operator name column.
    pre_op_profile += "<tr><td>" + toco_conversion_log_before.op_list[
        i] + "</td>"
    # Append input type column.
    if i < len(toco_conversion_log_before.op_signatures):
        pre_op_profile += "<td>" + get_input_type_from_signature(
            toco_conversion_log_before.op_signatures[i]) + "</td></tr>"
    else:
        pre_op_profile += "<td></td></tr>"

    # Generate post-conversion op profiles as a list of HTML table rows.
for op in toco_conversion_log_after.op_list:
    supported_type = get_operator_type(op, toco_conversion_log_after)
    post_op_profile += ("<tr><td>" + op + "</td><td>" + supported_type +
                        "</td></tr>")

html_dict["<!--REPEAT_TABLE1_ROWS-->"] = pre_op_profile
html_dict["<!--REPEAT_TABLE2_ROWS-->"] = post_op_profile
html_dict["<!--DOT_BEFORE_CONVERT-->"] = dot_before
html_dict["<!--DOT_AFTER_CONVERT-->"] = dot_after
if toco_err_log:
    html_dict["<!--TOCO_INFO_LOG-->"] = html_escape(toco_err_log)
else:
    success_info = ("TFLite graph conversion successful. You can preview the "
                    "converted model at: ") + tflite_graph_path
    html_dict["<!--TOCO_INFO_LOG-->"] = html_escape(success_info)

# Replace each marker (as keys of html_dict) with the actual text (as values
# of html_dict) in the HTML template string.
template = self.html_template
for marker in html_dict:
    template = template.replace(marker, html_dict[marker], 1)
    # Check that the marker text is replaced.
    if template.find(marker) != -1:
        raise RuntimeError("Could not populate marker text %r" % marker)

with _file_io.FileIO(self.export_report_path, "w") as f:
    f.write(template)
