import os
import gzip

#Search phrase stored in variable list. Can have multiple values.
keep_phrases = ["eventID:4624"]

# Set input dir
input_dir = './input/'

#set output dir
output_dir = './output/'

# Create the output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


def main_check(content, output_file):
    # Count required for loop count at end for relevant values
    count = 0 
    print("Main checker running")

    # Seperating content by new line
    content = content.split("\n")

    # Iterating over content split by new line
    for line in content:
        #print(f"{line} \n")
        # Checking for phrases we are wanting to find
        for phrase in keep_phrases:
            # Stripping out quotes to avoid issues
            newline = ''.join(i for i in line if i not in '"')
            #print(f"{newline} \n")
            # If phrase found, put in txt file
            if phrase in newline: 
                #print(newline)
                output_file.write(f"{str(newline)} \n\n")
                count += 1 
    print("Count = " + str(count))


for file_name in os.listdir(input_dir):
    # File check for .gz file
    if file_name.endswith('.log') or file_name.endswith('.gz'):
        print(f"Filename: {file_name}")
        file_path = os.path.join(input_dir, file_name)
        # Check if the file is compressed and open it accordingly
        if file_name.endswith('.gz'):
            output_name = f"{file_name}-output"
            with open(os.path.join(output_dir, f'{output_name}.txt'), 'w') as output_file:
                with gzip.open(file_path, 'rt') as input_file:
                    content = input_file.read()
                    main_check(content, output_file)
        else:
            output_name = f"{file_name}-output"
            with open(os.path.join(output_dir, f'{output_name}.txt'), 'w') as output_file:
                with open(file_path, 'r') as input_file:
                    content = input_file.read()
                    main_check(content, output_file)

