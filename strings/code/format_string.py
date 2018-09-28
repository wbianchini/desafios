from string_manipulation import StringManipulation

string = StringManipulation()

with open("input_file.txt", "r") as file:
    string.set_input_text(file.read())

formatted_text = string.format()

print(formatted_text)

output_file = open("output_file.txt", "w")
output_file.write(formatted_text)
output_file.close()
