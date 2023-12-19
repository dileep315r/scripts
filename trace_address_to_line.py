import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(
        description="Given a stack trace and a binary/library, trace_address_to_line.py will resolve "
                    "the hex addresses in the stack trace to the line numbers in the source files. "
                    "Make sure that the binutils are installed on the system and are available in the PATH."
    )
    parser.add_argument(
        "-b",
        dest="binary_file_path",
        help="Path to the binary/library file.",
        required=True,
    )
    parser.add_argument(
        "-t",
        dest="trace_file_path",
        help='Trace file to parse. Defaults to "trace.txt".',
        default="trace.txt",
    )
    parser.add_argument(
        "-a",
        dest="address_index",
        help='Index of the address in the trace file. Defaults to 8. Index starts from 0.',
        default=8,
        type=int,
    )
    parser.add_argument(
        "-i",
        dest="num_lines_to_ignore",
        help='Ignore first n lines in the trace file. Defaults to 1.',
        default=1,
        type=int,
    )

    return parser.parse_args()


def validate_path(path):
    if not os.path.exists(path):
        exit(f"{path} doesn't exist")


def expand_path(folder):
    return os.path.abspath(os.path.normpath(folder))


def extract_addresses(trace_path, address_index, num_lines_to_ignore):
    count = 0
    with open(trace_path) as f:
        while True:
            line = f.readline()
            if not line:
                break
            count += 1

            if count <= num_lines_to_ignore:
                continue

            address = line.split()[address_index]
            yield address


def resolve_address_to_line(binary_path, trace_path, address_index, num_lines_to_ignore):
    for address in extract_addresses(trace_path, address_index, num_lines_to_ignore):
        os.system(f"addr2line -e {binary_path} {address}")


if __name__ == "__main__":
    args = parse_args()
    binary_file_path = expand_path(args.binary_file_path)
    validate_path(binary_file_path)

    trace_file_path = expand_path(args.trace_file_path)
    validate_path(trace_file_path)

    resolve_address_to_line(binary_file_path, trace_file_path, args.address_index, args.num_lines_to_ignore)
