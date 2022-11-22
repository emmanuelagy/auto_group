import os, sys
sys.path.insert(0, sys)
from turtle import dot

class create_folder:
    dot_location='.'

    def __init__(self, extensiondictionary, file_ending):
        self.ext_and_files=extensiondictionary
        self.folder_names=file_ending

    def cleaning_dot(self):
        
        for item in self.folder_names:
            global dot_location
            dot_index= item.index(dot_location)
            if dot_location in item:
                del item[dot_index]

        return self.folder_names            
                    
    def user_confirm_folders(self):
        ''' this function is to ask the user if they are happy for the created folder names of if they want to change'''
        print('files have been created')
        for items in self.file_ending:
            answer=input('there has beena folder created for ')
    
    def main():
        pass

if __name__ == '__main__':
    create_folder