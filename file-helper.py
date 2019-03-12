#!/usr/bin/python

import tarfile
import argparse

class fileStatusObject:
    def __init__(self):
        self.status_dict = {}
        self.expected_files_count = 0
        self.present_files_in_tar_count = 0
        self.extra_files_in_tar_count = 0

    def load_filelist(self, filelist_filename):
        # Dictionary to store file status for availability of the file in provided .tar file
        # Format:
        # {
        #   <file_name> : <status>
        # }
        # Initially, all <status> are 'false' and if found in .tar file will be set to 'true'
        with open(filelist_filename) as files:
            for f in files:
                self.status_dict[f.rstrip('\n')] = False
                self.expected_files_count = self.expected_files_count + 1
        

class tarFileObject:
    def __init__(self, filename):
        self.tar = tarfile.open(filename)
    
    def verify_files(self, fileStatusObj):
        for member in self.tar:
            if member.isfile():
                member = member.name.split("/")[1]
                if member in fileStatusObj.status_dict:
                    # Update the status_dict 'fileStatusObj', to reflect the availibility of the file in .tar
                    fileStatusObj.status_dict[member] = True
                    fileStatusObj.present_files_in_tar_count = fileStatusObj.present_files_in_tar_count + 1
                else:
                    fileStatusObj.extra_files_in_tar_count = fileStatusObj.extra_files_in_tar_count + 1
        return fileStatusObj

def main(_files_list, _tar_file):
    # Reading .txt file contents
    files_status = fileStatusObject()
    files_status.load_filelist(_files_list)

    # Reading .tar file contents
    tar_file = tarFileObject(_tar_file)
    files_status = tar_file.verify_files(files_status)

    if(files_status.expected_files_count>files_status.present_files_in_tar_count):
        print("All files from the list are not present in the .tar file")   
    elif(files_status.expected_files_count==files_status.present_files_in_tar_count):
        print("All files from the list are present in the .tar files")
    print("\nExpected file count: " + str(files_status.expected_files_count))
    print("Files from list that are present in .tar: " + str(files_status.present_files_in_tar_count))
    print("Extra files present in .tar : " + str(files_status.extra_files_in_tar_count))
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', help='File name of text file containing filelist')
    parser.add_argument('--tar', help='File name of .tar file containing files generated after build')
    args = parser.parse_args()
    if(args.text and args.tar):
        main(args.text, args.tar)
    else:
        print("Please provide filesname for .txt and .tar files using --text and --tar arguments respectively")
