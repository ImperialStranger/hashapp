# HashApp
An utitlity written in python that can check and verify hash of a file

# Installation Instructions

## <img src="https://cdn.worldvectorlogo.com/logos/microsoft-windows-11.svg" alt="drawing" width="20" height="20"/> Windows
- Download the ZIP file for Windows from [Releases](https://github.com/NabilSadik2003/hashapp/releases/latest](https://github.com/NabilSadik2003/hashapp/releases).
- Extract the ZIP file.
- Copy `hashapp.exe` to your desired location.
- Add the `hashapp.exe` location to your `PATH` environment variable. If you don't know how do that, check this [link](https://www.google.com/search?q=windows+add+path+to+path+environment+variable).

## <img src="https://cdn-icons-png.flaticon.com/512/518/518713.png" alt="drawing" width="30" height="30"/> Linux
Coming Soon

# Usage
## Getting hash of a file
```bash
hashapp get-hash --file filename/or/path/to/your/file --hash_func sha256
```
It will print out the hash of the file.

**NOTE:** You can use `-f` instead of `--file` and `-hf` instead of `--hash-func`. `--hash-func` is optional. Default value of it is `sha256`.

## Verifying hash of a file
```bash
hashapp verify --file filename/or/path/to/your/file --hash_func sha256 --hash 1719b9ed2519f52da363bef16266c80c679be1c3ad3b481722938a8f1a9c589b
```
It will print out `0` if the file is OK otherwise it will print out `1`.

**NOTE:** You can use `-f` instead of `--file`, `-hf` instead of `--hash-func` and `-h` instead of `--hash`. `--hash-func` is optional. Default value of it is `sha256`.
