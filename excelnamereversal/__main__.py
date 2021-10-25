#!/usr/bin/env python3
"""
Take an Excel file with a list of names written "Last, First" 
and output a new Excel file with a list of names written
"First Last" ...because, why not?
"""

from settings import *
from utils import dropfile, openfile
from xlclass import Xlsx

# Get file and generate Xlsx object
f = dropfile.get()
xl_obj = Xlsx(f)

# Swap the info within the Xlsx object
xl_obj.reverse_text(datacol=DATA_COLUMN, startrow=START_ROW)

# Generate output filepath
f_path = xl_obj.path
out_path = f"{f_path.parent}/{f_path.stem}-{OUTPUT_SUFFIX}{f_path.suffix}"

# Save and (optionally) open new file
xl_obj.save(out_path)
if OPEN_OUTPUT_FILE:
    openfile.open(out_path)
