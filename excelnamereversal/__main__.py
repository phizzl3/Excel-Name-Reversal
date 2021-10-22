#!/usr/bin/env python3
"""
Take an Excel file with a list of names written "Last, First" 
and output a new Excel file with a list of names written
"First Last" ...because, why not?
"""

import name_swap
from utils import dropfile, openfile
from xlclass import Xlsx

OUTPUT_SUFFIX = "swapped"
DATA_COLUMN = "A"
START_ROW = 2
OPEN_OUTPUT_FILE = True


# Get file and generate Xlsx object
f = dropfile.get()
xl_obj = Xlsx(f)

# Swap the info within the Xlsx object
name_swap.swap(xl_obj, DATA_COLUMN, START_ROW)

# Generate output filepath
f_path = xl_obj.path
out_path = f"{f_path.parent}/{f_path.stem}-{OUTPUT_SUFFIX}{f_path.suffix}"

# Save and (optionally) open new file
xl_obj.save(out_path)
if OPEN_OUTPUT_FILE:
    openfile.open(out_path)
