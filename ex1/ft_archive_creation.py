import sys
import typing


def read_file(filename: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    try:
        file: typing.IO[str] | None = None
        file = open(sys.argv[1])
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return
    print("---", end="\n\n")
    content: str = file.read()
    print(content, end="\n\n")
    text = content.read()
    print("---")
    file.close()
    print(f"File '{filename}' closed.", end="\n\n")
    print("Transform data:")
    print("---", end="\n\n")
    new_text = ""
    for letter in text:
        if letter == '\n':
            new_text += "#\n"
        else:
            new_text += letter
            if len(text) > 0 and text[-1] != '\n':
                    new_text += "#"
    if len(text) > 0 and text[-1] != '\n':
        new_text += "#"
    print(f"{new_text}")
    print()
    print("---", end="\n\n")
    new_folder = input("Enter new file name (or empty): ")
    if new_folder == "":
        print("Not saving data.")
    else:
        folder_two: typing.IO[str] = open(new_folder, "w")
        print(f"Saving data to '{new_folder}'")
        print(f"Data saved in file '{new_folder}'.")
        folder_two.write(new_text)
        folder_two.close()


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    read_file(sys.argv[1])


if __name__ == "__main__":
    main()
