import os, shutil

PATH = {
    'input': 'input',
    'output': 'output'
}

errors = []

def logs_error():
    with open('error.txt', 'w') as error_file:
        for item in errors:
            error_file.write(item + '\n')

def start_copying():
    with open('files.txt', 'r') as files:
        for line in files:
            file_name = line.strip()
            file_path = os.path.join(PATH['input'], file_name)

            try:
                shutil.copy(file_path, PATH['output'])
            except:
                errors.append(file_name)

start_copying()
logs_error()
