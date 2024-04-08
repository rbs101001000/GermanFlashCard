import sys
from cx_Freeze import setup, Executable

# Dependencies to include
build_exe_options = {
    "includes": ["tkinter"],
    "include_files": ["C:/Users/SBR_PC/Desktop/farah1/images/front_card.png","C:/Users/SBR_PC/Desktop/farah1/images/light1.png","C:/Users/SBR_PC/Desktop/farah1/images/nextImage.png", "C:/Users/SBR_PC/Desktop/farah1/images/reset.png", "C:/Users/SBR_PC/Desktop/farah1/images/start.png", "C:/Users/SBR_PC/Desktop/farah1/csv/source.csv"]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use this option for a GUI application

setup(
    name="German flashcard",
    version="1.0",
    description="a birthday gift for my sweet sister",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)