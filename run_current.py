# run_current.py

# usage: <leader> e
# python run_current.py fileBasenameNoExtension relativeFileDirname fileExt
# run python or cargo project based on file extension
import sys
import subprocess
import os

base_name = sys.argv[1].split(".")[0]
file_ext = sys.argv[1].split(".")[-1]
dir_name = sys.argv[2]


if file_ext == "rs":
    if str(dir_name) != ".":
        if "\\" in str(dir_name):
            dir = dir_name.split("\\")[0]
            module = dir_name.split("\\")[-1]
        else:
            dir = dir_name.split("/")[0]
            module = dir_name.split("/")[-1]
        os.chdir(dir)
    if module == "src":
        print("cargo run")
        subprocess.run(["cargo", "run"])
    elif module == "examples":
        print(f"cargo run --example {base_name}")
        # release for long running examples
        subprocess.run(["cargo", "run", "--example", f"{base_name}", "--release"])

else:
    # Python: run as module if in subdirectory, else run directly
    if str(dir_name) != ".":
        if "\\" in str(dir_name):
            module = ".".join(str(dir_name).split("\\")) + f".{base_name}"
        else:
            module = ".".join(str(dir_name).split("/")) + f".{base_name}"
        subprocess.run(["python", "-m", module])
    else:
        print(f"python {base_name}.py")
        subprocess.run(["python", f"{base_name}.py"])

