from hdwallet.utils import is_mnemonic
import os
import argparse
import docx
from PyPDF2 import PdfReader


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# intro
print(color.YELLOW + "Welcome to seedsearch.py! Let\'s hunt for some BIP39 mnemonic seed\n" + color.END)
print(color.RED + 'DISCLAIMER: ' + color.END + 'This tool works with BIP39 seed')
print('            It is intended to make searches in a quick way, but it has not to be considered exhaustive\n')
print(color.PURPLE + 'This is a lite version, it will only look for seeds, without trying to check them online\n' + color.END)

parser = argparse.ArgumentParser(description='Mnemonic seed finder')
parser.add_argument('-d', metavar='directory', type=str, required=True, help='Directory to scan')
args = parser.parse_args()
directory = args.d

# Quits if directory does not exist
if not os.path.exists(directory):
    quit(color.RED + 'Directory does not exist!' + color.END)


def getListOfFiles(dirName):
    # create a list of file and sub directories
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles


def check_lang(word):
    f = open('Wordlists/b39en')
    if word in f.read():
        f.close()
        return('english')
    f = open('Wordlists/b39it')
    if word in f.read():
        f.close()
        return('italian')
    f = open('Wordlists/b39cz')
    if word in f.read():
        f.close()
        return('czech')
    f = open('Wordlists/b39es')
    if word in f.read():
        f.close()
        return('spanish')
    f = open('Wordlists/b39fr')
    if word in f.read():
        f.close()
        return('french')
    f = open('Wordlists/b39pr')
    if word in f.read():
        f.close()
        return('portuguese')
    f = open('Wordlists/b39cn')
    if word in f.read():
        f.close()
        return('chinese_simplified')
    f = open('Wordlists/b39cn2')
    if word in f.read():
        f.close()
        return('chinese_traditional')
    f = open('Wordlists/b39jp')
    if word in f.read():
        f.close()
        return('japanese')
    f = open('Wordlists/b39kr')
    if word in f.read():
        f.close()
        return('korean')
    f.close()
    return ('none')


def check_word(word, language):
    if (language == 'english'):
        f = open('Wordlists/b39en')
        if word in f.read():
            f.close()
            return True
        else:
            f.close()
            return False
    if (language == 'italian'):
        f = open('Wordlists/b39it')
        if word in f.read():
            f.close()
            return True
        else:
            f.close()
            return False
    if (language == 'czech'):
        f = open('Wordlists/b39cz')
        if word in f.read():
            f.close()
            return True
        else:
            f.close()
            return False
    if (language == 'spanish'):
        f = open('Wordlists/b39es')
        if word in f.read():
            f.close()
            return True
        else:
            f.close()
            return False
    if (language == 'french'):
        f = open('Wordlists/b39fr')
        if word in f.read():
            f.close()
            return True
        else:
            f.close()
            return False
    if (language == 'portuguese'):
        f = open('Wordlists/b39pr')
        if word in f.read():
            f.close()
            return True
        else:
            f.close()
            return False
    if (language == 'chinese_simplified'):
        f = open('Wordlists/b39cn')
        if word in f.read():
            f.close()
            return True
        else:
            f.close()
            return False
    if (language == 'chinese_traditional'):
        f = open('Wordlists/b39cn2')
        if word in f.read():
            f.close()
            return True
        else:
            f.close()
            return False
    if (language == 'japanese'):
        f = open('Wordlists/b39jp')
        if word in f.read():
            f.close()
            return True
        else:
            f.close()
            return False
    if (language == 'korean'):
        f = open('Wordlists/b39kr')
        if word in f.read():
            f.close()
            return True
        else:
            f.close()
            return False


# Get text from docx files
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


# Get the list of all files in the fiven path
listOfFiles = getListOfFiles(directory)

# Changes working directory to avoid issues with file opening
# use full path to open wordlists or full path to open files
user_folder = os.getlogin()
os.chdir('/opt/Tools/Recovery/SeedSearch')


temp_seed = []  # list that stores the seed during execution
seed_out = []
seed2check = []

n_files = len(listOfFiles)
print(color.BLUE + f'There are {n_files} files to scan' + color.END)
i = 0
# iterate through all the files
while i < n_files:
    # manage docx files
    if '.docx' in listOfFiles[i]:
        with open(directory + 'fgrtgdtegd', 'w') as f:  # random filename to avoid conflicts
            f.write(getText(listOfFiles[i]))
        f.close()
        f = open(directory + 'fgrtgdtegd', 'r')
        f.seek(0)
    # manage pdf files
    elif '.pdf' in listOfFiles[i]:
        reader = PdfReader(listOfFiles[i])
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        with open(directory + 'fgrtgdtegd', 'w') as f:
            f.write(text)
        f.close()
        f = open(directory + 'fgrtgdtegd', 'r')
        f.seek(0)
    # managing other files like txt, csv, html, json, etc.
    else:
        # Try if file can't be handled
        try:
            with open(listOfFiles[i], 'r') as tc:
                content = tc.read()
        except UnicodeDecodeError:
            print(color.YELLOW + '\nUnable to open ' + listOfFiles[i] + color.END)
            i += 1
            continue
        f = open(listOfFiles[i], 'r')
    language = ''
    line = f.readline()
    while line:   # reads the lines
        for word in line.split():
            checking = True  # used to check other wordlists if a word is not in the current wordlist
            while checking:
                if len(temp_seed) == 0:
                    # identify language
                    language = check_lang(word)
                    if language == 'none':
                        checking = False
                    else:
                        temp_seed.append(word)
                        checking = False
                else:
                    if check_word(word, language):
                        temp_seed.append(word)
                        checking = False
                    else:
                        temp_seed = []
                if (len(temp_seed) > 11) and (len(temp_seed) % 3 == 0):
                    temp_seed_str = ' '.join(temp_seed)
                    # adds only valid bip39 seeds to output
                    if is_mnemonic(temp_seed_str, language):
                        langprint = language.upper()
                        # adds language of the seed (uppercase and in brackets) to the output string
                        temp_seed_str += ' (' + langprint + ')'
                        seed_out.append(temp_seed_str)
                        seed2check.append(temp_seed_str)
                        temp_seed = []
                elif len(temp_seed) > 24:
                    temp_seed = []
        line = f.readline()
        
# Printing the output
    pr = 0
    if len(seed_out) > 0:
        print(color.DARKCYAN + f'\n=== Seeds found in {listOfFiles[i]} ===' + color.END)
        while pr < len(seed_out):
            pr += 1
            prpr = str(pr)
            print(prpr + ' ' + seed_out[pr - 1])
    seed_out = []
    f.close()
    i += 1
    
# delete temporary file
if os.path.isfile(directory + 'fgrtgdtegd'):
    os.remove(directory + 'fgrtgdtegd')
