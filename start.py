import os, shutil

path_dir = {'input': '', 'output': ''}
errors = []

def define_path():
    with open('path.txt', 'r') as path_config:
        line = path_config.read()
        configs = line.split(',')
        path_dir['input'] = configs[0].strip()
        path_dir['output'] = configs[1].strip()

def logs_error():
    if len(errors) > 0:
        with open('error.txt', 'w') as error_file:
            for item in errors:
                error_file.write(item + '\n')

def start_copying():
    with open('files.txt', 'r') as files:
        for line in files:
            file_name = line.strip()
            file_path = os.path.join(path_dir['input'], file_name)

            try:
                shutil.copy(file_path, path_dir['output'])
            except:
                errors.append(file_name)

define_path()
start_copying()
logs_error()
