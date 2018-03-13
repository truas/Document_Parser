'''
Created on Mar 13, 2018

@author: Terry Ruas

Important:
1. 'files' folder for input/output should be placed in the same level as document_analysis

'''
import argparse
import sys
import os


#python module absolute path
pydir_name = os.path.dirname(os.path.abspath(__file__))

#python path definition
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

import document_analysis.read_write as rw

#input/output files/folder - If you need to set input, output folders
#in_foname = "C:/tmp_project/DocParser/input"
#ou_foname = "C:/tmp_project/DocParser/output"
#lis_fname = "input_list.txt"

if __name__ == '__main__':  
    
    #IF you want to use COMMAND LINE for folder path  
    parser = argparse.ArgumentParser(description="Document_Parser - combine and separate general text documents")
    parser.add_argument('--input', type=str, action='store', dest='in_f', metavar='<folder>', required=True, help='input folder to read document(s)')
    parser.add_argument('--output', type=str, action='store', dest='out_f', metavar='<folder>', required=True, help='outnput folder to write document(s)')
    parser.add_argument('--list', type=str, action='store', dest='lis_f', metavar='<file name>', required=False, help='file name for the input')
    args = parser.parse_args()
    
    #COMMAND LINE  folder paths
    input_folder = args.in_f
    output_folder = args.out_f
    lis_fname = args.lis_f
    
    #in/ou relative location
    in_fname = os.path.join(pydir_name,'../'+input_folder)
    ou_fname = os.path.join(pydir_name,'../'+output_folder)
    
    
    docs = rw.doc_list_multi(in_fname) #list of documents to parse
    #rw.print_doclist(docs, ou_fname, lis_fname) #list of files you read
    #rw.synsets_one_file(docs, ou_fname) #if you are parsing a doc-synset (output format from BSD_Extractor)
    rw.text_one_file(docs, ou_fname) #parsing multiple text in one single file
   
    
    
    print('Finished...')