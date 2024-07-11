from zipfile import ZipFile
from pathlib import Path


def merge_zips(zip_files, output_zip):
    sequence_number = 1
    with ZipFile(output_zip, "w") as output_zf:
        for zip_file in zip_files:
            with ZipFile(zip_file, "r") as input_zf:
                for file_name in input_zf.namelist():
                    with input_zf.open(file_name) as f:
                        new_file_name = f"{sequence_number:03}.{Path(file_name).suffix}"
                        output_zf.writestr(new_file_name, f.read())
                        sequence_number += 1


zips = [f"example/{i}.zip" for i in range(1, 3)]
output_name = "output.zip"

if __name__ == "__main__":
    merge_zips(zips, output_name)
