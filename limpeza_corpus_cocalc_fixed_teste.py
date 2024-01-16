import glob
import re

def delete_lines(file_pattern):
    filepaths = glob.glob(file_pattern)
    for filepath in filepaths:
        # Read the contents of the file
        with open(filepath, 'r') as file:
            lines = file.readlines()

        # Remove extra spaces
        lines = [re.sub(r'\s+', ' ', line) for line in lines]
        # Remove extra spaces before period punctuations
        # lines = [re.sub(r'\s*\.', '.', line) for line in lines] 


        # Write the modified lines back to the file
        with open(filepath, 'w') as file:
            file.writelines(lines)

        print(f"Lines modified in {filepath}.")


file_pattern = '/Users/lucianadiasdemacedo/Downloads/limpeza_espacos/limpeza_espaco/*.txt' 
delete_lines(file_pattern)
