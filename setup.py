import cx_Freeze

executables = [cx_Freeze.Executable("Main.py")]

cx_Freeze.setup(
    name = "SOLID",
    options = {"build_exe":{"packages":["pygame"], "include_files": ["lala.png","PONUR.png","YUNUS.png"]}},
    description = "SOLID PROJECT",
    executables = executables
    
)
