import glob
import re


def delete_lines(file_pattern):
    filepaths = glob.glob(file_pattern)
    for filepath in filepaths:

            # Read the contents of the file
        with open(filepath, 'r') as file:
            lines = file.read()


        lines = re.sub('(?<=[a-z])\n(?=([A-Z][a-z]))', ' ', lines)
        lines = re.sub('(?<=[a-z] )\n(?=([A-Z][a-z]))', '', lines)
        lines = re.sub('\n(?=[a-z])', '', lines)
        lines = re.sub('\n:', ' : ', lines)
        lines = re.sub(' +', ' ', lines)


#        lines = lines.split('\n')
            # Remove extra spaces before period punctuations
        #        lines = [re.sub(r'\u000D\u000A', ' ', line) for line in lines] 
#        lines = [re.sub('\n[a-z]', ' ', line) for line in lines] 
                #lines = [re.sub(r'(\u000D\u000A\u003A)', ' : ', line) for line in lines] 


        # Write the modified lines back to the file
        with open(filepath.replace('.txt', 'new.txt'), 'w') as file:
            file.write(lines)

        print(f"Lines modified in {filepath}.")


file_pattern = '/Users/lucianadiasdemacedo/Downloads/limpeza_espacos/limpeza_espaco/*.txt' 
delete_lines(file_pattern)


