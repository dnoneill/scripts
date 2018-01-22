|combine_xlsx_spreadsheets| combine_csv_spreadsheets | populate |
|--|--|--|
|combines all csv files in a particular folder|combines all xls and xlsx files in a particular folder. Assumes that columns are in same format across files| takes a files spreadsheet and matches a metadata spreadsheet filepath column|
|1. Install Pandas requirements| 1. Install unicodecsv| 1. Install unicodecsv|
|`$ pip install pandas`| `$ pip install unicodecsv`|
|`$ pip install xlrd` |2. Run script | 2. Run script |
|`$ pip install openpyxl`|`$ python combine_csv_spreadsheets.py`|`$ python populate.py`|
| 2. Run Script |3. Enter filepath to where the csv files are located  | 2. Enter the filepath with filename of file list csv |
|`$ python combine_xlsx_spreadsheets.py`  | | 3. Enter the filepath with the filename name of metadata csv|
| 2. Enter the filepath to where the excel files are located | | 4. Enter name of output file (exclude extension) |
|3. Enter file name of the saved file without extension|||


