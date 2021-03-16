import os
os.getcwd()
with open('desolation_row.txt', 'r') as file:
    text = file.read()
file.close()

punctuation = ['.', ',', ':', "", '?', '!']
text_new = text.split()


