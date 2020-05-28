import os.path
import time
from pathlib import Path


def check_modified(file):
    return "{:<20}".format(file) + "| Last Modified: " + time.ctime(os.path.getmtime(file))


def check_more_recent(filename, filename2):
    if time.ctime(os.path.getmtime(filename)) > time.ctime(os.path.getmtime(filename2)):
        return filename
    else:
        return filename2


def overwriter(filename, filename2):
    action = False

    while not action:
        print(check_modified(filename))
        print(check_modified(filename2))
        print()
        print(check_more_recent(filename, filename2), "has been modified more recently.")

        choice = input("Overwrite the older file? Y/N")
        if choice == "Y":
            action = True
            print("Overwriting...")
        elif choice == "N":
            action = True
            print("Keeping original file...")
        else:
            print("Invalid choice. Try again.\n")


#should be able to change the local and remote directories but hard coding will be fine for now
local_dir = Path('c:/users/eklyps/Documents/PycharmProjects/CloudSyncer')
remote_dir = Path('c:/users/eklyps/Documents/PycharmProjects/CloudSyncer/someFolder')

#file in question
file_name = 'test.txt'

# local_file = Path(local_dir / 'test.txt').is_file()
local_file = Path(local_dir / file_name)
remote_file = Path(remote_dir / file_name)

if local_file.name == remote_file.name:
    overwriter(local_file.name, remote_file.name)
else:
    print("No need to overwrite.")