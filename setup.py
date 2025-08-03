from cx_Freeze import setup, Executable


setup(
    name="NanoCalc",
    version="2.0",
    description="Efficient Calculator App",
    executables=[Executable("main.py")],
)
