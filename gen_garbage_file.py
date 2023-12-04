import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate a garbage file of the specified size."
    )
    parser.add_argument(
        "-size",
        dest="size",
        help="Size in MBs of the garbage file to generate.",
        type=int,
        default=1
    )
    parser.add_argument(
        "-folder",
        dest="folder",
        help='Folder to generate the garbage file in. Defaults to the current folder.',
        default=".",
    )
    parser.add_argument(
        "-name",
        dest="name",
        help='Name of the garbage file to generate. Defaults to "garbage.txt".',
        default="garbage.txt",
    )
    return parser.parse_args()


def generate_file(path, size):
    size_in_bytes = size * 1024 * 1024
    with open(path, "wb") as f:
        f.write(os.urandom(size_in_bytes))
    print(f"Done generating {size} MB garbage file {path}")


def validate_path(path):
    if not os.path.exists(path):
        exit(f"{path} doesn't exist")


def build_file_path(folder, name):
    folder = os.path.abspath(os.path.normpath(folder))
    validate_path(folder)
    return os.path.join(folder, name)


if __name__ == "__main__":
    args = parse_args()
    file_path = build_file_path(args.folder, args.name)
    generate_file(file_path, args.size)
