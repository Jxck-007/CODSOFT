
import os
import shutil

class File_Automation():
    

    def __init__(self,upath):
        
        self.path=upath
        self.img_count = 0
        self.audio_count = 0
        self.video_count = 0
        self.doc_count = 0
        self.audio_extensions = ['.mp3', '.wav', '.aac']
        self.image_extensions = ['.png', '.jpg','.jpeg']
        self.video_extensions= [ '.mp4', '.mov', '.avi' ,'.mkv']
        self.document_extensions=['.txt', '.docx', '.pdf']
    def current(self):  
        current_directory = os.getcwd()
        print(f"The Current Directory : {current_directory}")
    
    def list(self):
        print("\n".join(os.listdir(self.path)))
            
    
    def sort(self):
        for _ in os.listdir(self.path):
            self.root,self.ext=os.path.splitext(_)
            fpath=os.path.join(self.path,_)
            if os.path.isdir(fpath):
                continue
            if self.ext.lower() in self.image_extensions :
                path=os.path.join(self.path,'Images')
                os.makedirs(path, exist_ok=True)
                try:
                    shutil.move(fpath,path)
                    print(f'Moved {_} Successfully to Images')
                    self.img_count += 1
                except Exception as e:
                    print(e)


            elif self.ext.lower() in self.audio_extensions:
                path=os.path.join(self.path,'Audio')
                os.makedirs(path, exist_ok=True)
                try:
                    shutil.move(fpath,path)
                    print(f'Moved {_}  Successfully to Audio')
                    self.audio_count += 1
                except Exception as e:
                    print(e)


            elif self.ext.lower() in self.video_extensions :
                path=os.path.join(self.path,'Video')
                os.makedirs(path, exist_ok=True)
                try:
                    shutil.move(fpath,path)
                    print(f'Moved {_} Successfully to Video')
                    self.video_count+=1
                except Exception as e:
                    print(e)


            elif self.ext.lower() in self.document_extensions :
                path=os.path.join(self.path,'Document')
                os.makedirs(path, exist_ok=True)
                try:
                    shutil.move(fpath,path)
                    print(f'Moved {_} Successfully to Docuement')
                    self.doc_count+=1
                except Exception as e:
                    print(e)
    def total(self):  
        print("\nSummary:")
        print(f"📸 Images moved: {self.img_count}")
        print(f"🎵 Audio moved: {self.audio_count}")
        print(f"🎬 Video moved: {self.video_count}")
        print(f"📄 Documents moved: {self.doc_count}")


                    
while True:
    upath=input("Enter the Path of The Folder:")
    A=File_Automation(upath)
    if os.path.exists(upath):
        print("Checking for The Path's Existence\n")
        A.current()
        print()
        print("Here Are the Items Folder Contains:")
        A.list()
    else:
        print("Enter The Correctt Directory.")
        break
    if input('Do You Wanna Organize The Current Directory (y/n):')[0].lower()=='y':
        A.sort()
        A.total()
    else:
        print()
        break

if __name__ == "__main__":
    debug=True