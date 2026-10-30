import os, shutil
# auto-file-organizer - portfolio S.Kom
folders = {'Images': ['.jpg','.png'], 'Docs': ['.pdf','.docx'], 'Code': ['.js','.py','.sh']}
for file in os.listdir('.'):
    for folder, exts in folders.items():
        if any(file.lower().endswith(ext) for ext in exts):
            os.makedirs(folder, exist_ok=True)
            try:
                shutil.move(file, os.path.join(folder, file))
            except: pass
print("Done organizing!")
