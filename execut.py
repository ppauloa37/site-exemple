from cx_Freeze import setup, Executable

setup(
    name="PaintApp",
    version="0.1 beta",
    description="Aplicativo de Desenho",
    executables=[Executable("paint.py", base="Win32GUI")]
)

