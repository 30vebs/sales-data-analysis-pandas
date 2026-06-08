def clean_line(line):
    cleaned = ""

    for char in line:
        if char.isalnum() or char.isspace():
            cleaned += char

     # remove extra spaces
    cleaned ="".join(cleaned.split())
    return cleaned


def clean_file(input_file, output_file):
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            cleaned_line = clean_line(line)
            if cleaned_line:
                outfile.write(cleaned_line + "\n")

# run the program
clean_file("input.txt", " output.txt")
print("✅ File Cleaned Succesfully!")


