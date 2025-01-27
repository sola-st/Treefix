# Extracted from ./data/repos/tensorflow/tensorflow/lite/experimental/acceleration/mini_benchmark/copy_associated_files.py
with open(model_path, 'rb') as input_file:
    with open(output_path, 'wb') as output_file:
        output_file.write(input_file.read())
if zipfile.is_zipfile(associated_files_path):
    zip_src = zipfile.ZipFile(associated_files_path, 'r')
    zip_tgt = zipfile.ZipFile(output_path, 'a')
    for info in zip_src.infolist():
        zip_tgt.writestr(info, zip_src.read(info))
