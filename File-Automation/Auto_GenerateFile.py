import os

extensions = ['.jpg', '.mp3', '.mp4', '.pdf', '.txt']
names = ['file1', 'file2', 'file3', 'file4', 'file5']

folder = 'Sample_Files'
os.makedirs(folder, exist_ok=True)

for name, ext in zip(names, extensions):
    with open(os.path.join(folder, name + ext), 'w') as file:
        file.write("Dummy data")
