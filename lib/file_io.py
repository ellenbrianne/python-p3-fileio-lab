def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode='w', encoding='UTF-8') as text_file:
        text_file.write(file_content)

def append_file(file_name, append_content):
    text_file = open(f'{file_name}.txt', mode='a', encoding='UTF-8')
    text_file.write(append_content)
    text_file.close()

def read_file(file_name):
    with open(f"{file_name}.txt", encoding='UTF-8') as text_file:
        for line in text_file:
            return line

   
