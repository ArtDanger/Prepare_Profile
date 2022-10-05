import os
import sys
import shutil

from pathlib import Path
from subprocess import call


def check_path(filename):
    """
    This func need for absolut path in the executable file
    https://stackoverflow.com/questions/22472124/what-is-sys-meipass-in-python
    """
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        bundle_dir = Path(sys._MEIPASS)
    else:
        bundle_dir = Path(__file__).parent

    return Path.cwd() / bundle_dir / filename


def data_processing():
    try:
        count = int(input("How many profiles do you need? "))
        return count
    except ValueError:
        print("The value must be an integer.")


def create_folder():
    if not os.path.exists(check_path("Profiles")):
        os.makedirs(check_path("Profiles"))


def copy_chrome_folder():
    """find and copy your default"""
    create_folder()  # check folder "Profile" exists

    absolute_path_profiles = os.environ['USERPROFILE'] + r"\AppData\Local\Google\Chrome\User Data"
    email = str(input("Email: "))
    new_path_profile = check_path("Profiles") / email / "User Data"
    try:
        shutil.copytree(absolute_path_profiles, new_path_profile)
    except FileExistsError:
        print("Account already exists. Try another email.")
        copy_chrome_folder()
    return create_profile(new_path_profile)


def create_profile(new_path_profile):
    path_to_chrome = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    path_profile = f"{new_path_profile}"  # User Data
    command = f'"{path_to_chrome}" --user-data-dir="{path_profile}"'
    call(command)


if __name__ == "__main__":
    value = data_processing()
    for _ in range(value):
        copy_chrome_folder()

    input("Enter: ")
