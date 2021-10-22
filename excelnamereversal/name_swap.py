"""
Get Xlsx object (Excel spreadsheet) containing string values
(formatted "Last, First") in a specified column, loop through
and replace those values with reformatted (First Last) text.
"""

from xlclass import Xlsx


def _split_rotate(val: str) -> str:
    """Get string input (formatted "Last, First"), split it on the ","
    and return it (formatted "First Last").

    Args:
        val (str): Text to be reformatted ("Last, First")

    Returns:
        str: Reformatted text ("First Last")
    """
    split_val = val.split(",")
    return f"{split_val[1]} {split_val[0]}"


def swap(xl: Xlsx, datacol: str = "A", startrow: int = 1) -> None:
    """Get Xlsx object (Excel spreadsheet) containing string values
    (formatted "Last, First") in a specified column, loop through
    and replace those values with reformatted (First Last) text.


    Args:
        xl (Xlsx): Xlsx object (Excel spreadsheet)
        datacol (str, optional): Excel column with values. Defaults to "A".
        startrow (int, optional): Excel row where values begin. Defaults to 1.
    """
    for row, cell in enumerate(xl.ws[datacol], 1):
        if row < startrow or not cell.value:
            continue
        # Swap info and write back to cell
        xl.ws[f"{datacol}{row}"] = _split_rotate(cell.value)
