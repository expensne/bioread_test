import sys
import bioread


def print_as_table(lines):
    # Convert all values to strings
    lines = [[str(val) for val in line] for line in lines]
    # Get the maximum width of each column
    widths = [max(map(len, col)) for col in zip(*lines)]
    # Print the table
    for line in lines:
        print("  ".join((val.ljust(width) for val, width in zip(line, widths))))


def main(args):
    if len(args) != 1:
        print("Usage: python main.py [acq_file]")
        return

    data = bioread.read_file(args[0])
    assert data is not None

    lines = [["Channel Name", "Length of Data", "Data Min", "Data Max", "Data Sum", "Data Mean"]]

    for channel in data.channels:
        name = str(channel.name)
        data = channel.data

        lines.append([name, len(data), data.min(), data.max(), data.sum(), data.mean()]) # type: ignore

    print_as_table(lines)


if __name__ == "__main__":
    main(sys.argv[1:])
