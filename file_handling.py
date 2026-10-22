
"""Working with text files in Python."""

from pathlib import Path

FILE_PATH = Path("student_notes.txt")


def main():
    # Create a file and write some information
    FILE_PATH.write_text(
        "Python makes programming easier.\n"
        "It is widely used in data science and AI.\n",
        encoding="utf-8",
    )

    # Read and display the saved information
    text_content = FILE_PATH.read_text(encoding="utf-8")
    print("Saved file content:")
    print(text_content)

    # Search for a particular word in the file
    lines = text_content.splitlines()
    keyword = "Python"

    matching_lines = [
        line_number
        for line_number, line in enumerate(lines, start=1)
        if keyword.lower() in line.lower()
    ]

    if matching_lines:
        print(f"'{keyword}' appears on line(s): {matching_lines}")
    else:
        print(f"'{keyword}' was not found in the file.")

    # Add another line without removing existing content
    with FILE_PATH.open("a", encoding="utf-8") as file:
        file.write("These are my Python practice notes.\n")

    print("\nContent after appending:")
    print(FILE_PATH.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
