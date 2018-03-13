'''
Created on Mar 13, 2018

@author: Terry Ruas

'''
#imports
import os
import nltk
import re

#from-imports
from datetime import timedelta
from stop_words import get_stop_words

#loads
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')

document_list = 'document_list.txt'
corpus = 'corpus.txt'

def doc_list_single(folder_name):
    #read all files in a  folder with .txt format and makes a list of them
    input_file_list = [folder_name+'/'+name for name in os.listdir(folder_name) if name.endswith('txt')]
    doc_data_list = open(document_list, 'w+')
    
    #saving document list
    for file in input_file_list:
        doc_data_list.write(file +'\n')
    doc_data_list.close() #raw-input list with absolute path
    
    #show the number of files in the directory
    print ('Found %s documents under the dir %s .....'%(len(input_file_list), folder_name))
    return (input_file_list)
#creates list of documents in a single folder

def doc_list_multi(folder_name):
    input_file_list = []
    for roots, dir, files in os.walk(folder_name):
        for file in files:
            file_uri = os.path.join(roots, file)
            #file_uri = file_uri.replace("\\","/") #if running on windows           
            if file_uri.endswith('txt'): input_file_list.append(file_uri)
    return input_file_list
#creates list of documents in many folders

def print_doclist(doclist, output_folder, listname):
    outp = open(output_folder+'/'+listname, 'w+', encoding='utf-8')
    for doc in doclist:
        outp.write(doc +'\n')
    outp.close()
#writes a list of documents to read

def text_one_file(files, output_folder):
    big_document = open(output_folder+'/'+corpus, 'w+', encoding='utf-8')    
    for file in files:
        print('Processing %s' %file)
        with open(file, 'r', encoding='utf-8') as fin:
            contents = fin.read()
            # clean and tokenize document string
            raw = str(contents.lower())
            tokens = tokenizer.tokenize(raw)
            #remove stop words from tokens
            stopped_tokens = [i for i in tokens[:] if not i in en_stop] #[1:] get rid of the 'b'byte if using 'rb'
            # remove numbers
            number_tokens = [re.sub(r'[\d]', ' ', i) for i in stopped_tokens]
            number_tokens = ' '.join(number_tokens).split()
            #removing noise single chars
            no_one_char_tokens = [i for i in number_tokens if not len(i) == 1]
            #big_document.write(str(tokens).strip("'"))
            words = concat_string(no_one_char_tokens)
            big_document.write(words+'\n')
    big_document.close()   
#creates one file with each line being a document in the files list

def concat_string(token_doc):
    words = ""
    for word in token_doc:
        words+=word + " "
    return (words)    
#concatenates a list of strings in one string for writing into a file

def synsets_one_file(files, output_folder):
    big_document = open(output_folder+'/'+corpus, 'w+', encoding='utf-8')    
    for file in files:
        print('Processing %s' %file)
        with open(file, 'r', encoding='utf-8') as fin:
            for line in fin:
                block = line.split('\t')
                #block[0]:word; block[1]:synset; block[2]:offset; block[3]:pos - this has \n at the end
                big_document.write(block[0] +'-'+ block[2] +'-'+ block[3].strip('\n') + '\t')
        big_document.write('\n')
    big_document.close()   
#creates one file with each line being a document in the files list