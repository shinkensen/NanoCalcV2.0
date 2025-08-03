from cx_Freeze import setup, Executable

base="Win32GUI"
setup(
    name="NanoCalc",
    version="2.0",
    description="Efficient Calculator App",
    executables=[Executable("main.py")],
)
