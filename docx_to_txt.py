import docx2txt
import glob


# process docx to txt file

def docx_to_txt(file):
    txt=docx2txt.process(file)
    txt=txt.replace("\n", "").replace("\t","")
    return txt


# writes txt file in chosen directory

def write_txt(directory, file_name, text):
    with open(directory+file_name+".txt", 'w') as f:  
        f.write(text)

        
# process all docx files in given directory to txt files

def process_docx_to_txt(directory):
    docx_files=[file for file in glob.iglob(directory+"*docx")]
    for file in docx_files:
        text=docx_to_txt(file)
        file_name=file.partition("\\")[2].partition(".")[0]
        write_txt(directory, file_name, text)
       
