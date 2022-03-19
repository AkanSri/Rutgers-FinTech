from pathlib import Path
print(f"Current working dir: {Path.cwd()}")

filepath = Path("/Users/akanksha/Rutgers/Rutgers-FinTech/01-Lesson-Plans/02-Python/3/Activities/07-Ins_File_IO/Resources/input.txt")

text = ''
with open(filepath, 'r') as file:
    text = file.read()
    print (text)

output_path = Path("/Users/akanksha/Rutgers/Rutgers-FinTech/01-Lesson-Plans/02-Python/3/Activities/07-Ins_File_IO/output.txt")

with open(output_path, "w") as file:
        file.write(text)