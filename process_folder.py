import os
import subprocess
import argparse

# python3 process_folder.py -folder ~/Downloads/print -command 'lpr -U dileepkusuma -o sides=two-sided-long-edge'
def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate a garbage file of the specified size."
    )
    parser.add_argument(
        "-folder",
        dest="folder",
        help='Files in folder that needs to be processed.',
        default=".",
    )
    parser.add_argument(
        "-command",
        dest="command",
        help='Command used to process the files in the folder.',
        default="ls",
    )
    return parser.parse_args()


def validate_folder(path):
    folder = os.path.abspath(os.path.normpath(path))
    if not os.path.exists(folder):
        exit(f"{folder} doesnt exist")
    else:
        return folder


def process_folder(folder_path, command):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            try:
                subprocess_args = command.split(' ')
                subprocess_args.append(file_path)
                subprocess.run(subprocess_args, check=True)
                print(f"Processed file: {file_name}")
            except subprocess.CalledProcessError as e:
                print(f"Error processing file {file_name}: {e}")


# Example usage:
if __name__ == "__main__":
    args = parse_args()
    folder = validate_folder(args.folder)
    process_folder(folder, args.command)
