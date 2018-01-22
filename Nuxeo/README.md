# nuxeo_get_metadata.py

This script gets all metadata from Nuxeo. It requires the following instructions from nuxeo_spreadsheet to be followed: https://github.com/ucldc/nuxeo_spreadsheet/wiki;

1. Install requirements
        $ pip install -r requirements.txt

2. run script
        $ python nuxeo_get_metadata.py
        
3. Enter the filepath of nuxeo assets (i.e. /asset-library/UCLA/)

4. Enter O or I for Object or Item level. Object level gets all metadata from the filepath; 
Item level gets all metadata for the items on step below the filepath.

5. Enter google sheet URL. If you want the data written to a tsv and not a google sheet 
simply hit enter.

6. Enter 'Y' if you want all headers, even columns with no data to be written to the 
spreadsheet. Otherwise enter 'N' and only columns with data will be downloaded.

7. File will be downloaded or written to Google sheet based on choices.
