import platform


def open(f_path: str) -> None:
    """Open an output file based on Operating System.

    Args:
        f_path (str): Filepath for the file to be opened.
    """
    if platform.system() == "Windows":
        import os
        os.startfile(f_path)

    elif platform.system() == "Darwin":
        pass
