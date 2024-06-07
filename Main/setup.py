from cx_Freeze import setup, Executable

# Define the executable
executables = [Executable("gui.py", base="Win32GUI")]

# Setup options
setup(
    name="PDF-Converter",
    version="0.1",
    description="Converting Microsoft DOCX files to pdf",
    executables=executables,
)
