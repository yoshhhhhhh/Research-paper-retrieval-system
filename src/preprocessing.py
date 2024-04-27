import os
import sys
import pdftotext
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords, wordnet as wn, wordnet
from nltk.stem import WordNetLemmatizer

SRC_FOLDER = './data/pdf_downloads/'
DST_FOLDER = './data/txt/'
FILES = os.listdir(SRC_FOLDER)

def preprocessor(files, src_folder, dst_folder):
    if not files:
        sys.exit("\'data/pdf_downloads\' directory is empty, cannot work")

    stops = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()

    for f_name in files:
        raw_f_path = os.path.join(src_folder, f_name)
        print("Starting pre-processing file: " + f_name)
        try:
            with open(raw_f_path, "rb") as f:
                pdf = pdftotext.PDF(f)
        except FileNotFoundError:
            print('File \'{0}\' does not exit.'.format(f_name))
            continue
        except IOError:
            print('File \'{0}\' has input/output exception.'.format(f_name))
            continue

        txt = "\n\n".join(pdf)
        tokens = word_tokenize(txt)
        filt_words = [lemmatizer.lemmatize(token.lower()) for token in tokens if token.isalpha() and token.lower() not in stops]

       

        output_file_path = os.path.join(dst_folder, f_name[:-4] + "_tokens.txt")
     
        with open(output_file_path, 'w', encoding="utf-8") as output_file:

            output_file.write(" ".join(filt_words))
        print(f"Writed tokens of : {f_name}")


if __name__ == '__main__':
    preprocessor(FILES, SRC_FOLDER, DST_FOLDER)

