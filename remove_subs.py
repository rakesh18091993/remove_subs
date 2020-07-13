import os
path = "E:\\Complete Python Bootcamp"
folders = os.listdir(path)
for folder in folders:
    inside_folder = path + '\\' + folder
    files = [f for f in os.listdir(inside_folder) if f.endswith('.srt')]
    for file in files:
        if file.endswith('tr.srt'): # or 'ja.srt', 'en.srt'
            del_file = inside_folder + '\\' + file
            os.remove(del_file)
