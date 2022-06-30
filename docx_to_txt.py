import docx2txt
import glob


def docx_to_txt(file):
    """Processes a .docx file to a .txt file.
    """
    txt=docx2txt.process(file)
    txt=txt.replace("\n", "").replace("\t","")
    return txt


def write_txt(directory, file_name, text):
    """Writes a .txt file in a chosen directory.
    """
    with open(directory+file_name+".txt", 'w') as f:  
        f.write(text)

       
def process_docx_to_txt(directory):
    """Processes all .docx files in given directory to .txt files.
    """
    docx_files=[file for file in glob.iglob(directory+"*docx")]
    for file in docx_files:
        text=docx_to_txt(file)
        file_name=file.partition("\\")[2].partition(".")[0]
        write_txt(directory, file_name, text)
       
