import sys
from cx_Freeze import setup, Executable

base = "Win32GUI" if sys.platform == "win32" else None

build_exe_options = {
    "packages": ["tkinter", "os"],
    "include_files": [],  # You can add custom assets here later
}

setup(
    name="NanoCalc",
    version="2.0",
    description="Efficient Calculator App",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)
