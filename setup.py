import sys
from cx_Freeze import setup, Executable

# Only use GUI mode on Windows to suppress console
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="NanoCalc",
    version="2.0",
    description="Efficient Calculator App",
    executables=[Executable("main.py", base=base)]
)
