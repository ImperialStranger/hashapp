from pathlib import Path
import click, hashlib


__VERSION__ = "1.0"


# Gets the content and hash function from get_hash() and returns to it hash retrieved with the selected hash function
def getHash(content, hash_func):
    hash = None
    if hash_func == "md5":
        hash = hashlib.md5(content).hexdigest()
        return hash
    elif hash_func == "sha1":
        hash = hashlib.sha1(content).hexdigest()
        return hash
    elif hash_func == "sha224":
        hash = hashlib.sha224(content).hexdigest()
        return hash
    elif hash_func == "sha256":
        hash = hashlib.sha256(content).hexdigest()
        return hash
    elif hash_func == "sha384":
        hash = hashlib.sha384(content).hexdigest()
        return hash
    else:
        click.secho(f"[ ERROR ] Unknown hash function: '{hash_func}'", fg="red")


# This function checks existence of a file. If exists it returns True otherwise returns False
def check_file_existence(file):
    if Path(file).exists():
        return True
    else:
        return False


@click.group()
def hashapp():
    """An utitlity written in python that can check and verify hash of a file"""
    pass


# This function retrives hash of the user specified file and prints the hash found with the selected hash function
@click.command(name="get-hash", help="Gets the hash of a file")
@click.option("--file", "-f", help="Filename or path to the file")
@click.option("--hash_func", "-hf", default="sha256", help="Hash function")
def get_hash(file, hash_func):
    if check_file_existence(file):
        file = open(file, 'rb')
        buff = file.read()
        hash = getHash(buff, hash_func)
        click.secho(hash, fg="blue")
    else:
        click.secho(f"[ ERROR ] No such file: '{file}'", fg="red")


"""
This function verifies the user specified file with the user specified hash and prints '0' if the file is OK otherwise
prints '1'
"""
@click.command(name="verify", help="Verifies the hash of a file")
@click.option("--file", "-f", help="Filename or path to the file")
@click.option("--hash_func", "-hf", default="sha256", help="Hash function")
@click.option("--hash", "-h")
def verify(file, hash_func, hash):
    if check_file_existence(file):
        file = open(file, 'rb')
        buff = file.read()
        file_hash = getHash(buff, hash_func)
        if hash == file_hash:
            click.secho(0, fg="green")
        else:
            click.secho(1, fg="red")
    else:
        click.secho(f"[ ERROR ] No such file: '{file}'", fg="red") 


# This function prints out the installed HashApp version
@click.command(name="version", help="Prints the installed HashApp version")
def version():
    click.echo(f"HashApp {__VERSION__}")


hashapp.add_command(get_hash)
hashapp.add_command(verify)
hashapp.add_command(version)


if __name__ == "__main__":
    hashapp()
