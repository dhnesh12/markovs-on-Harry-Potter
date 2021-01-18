import re,sys,glob,argparse
import random
from preprocess import Textprocess
import markovify

def parse_args():
    argument_parse = argparse.ArgumentParser(description = "MarkovChain for Large Corpus.")
    argument_parse.add_argument("-i", dest = "input",  default = "data/*.txt", help = "Input txt file/s for Markov model")
    argument_parse.add_argument("-c", dest = "characters", default = 4500, help = "Length of characters ")
    argument_parse.add_argument("-o",  dest = "output", default = "output/fin.txt", help = "Output File for All Meger Files")
    results = argument_parse.parse_args()
    input = results.input
    character = results.characters
    output = results.output
    return input, character, output


def read_files(input_path,outputfile):

    # read all  txt files and merge in one,
    files = glob.glob(input_path)
    files.sort()


    with open(outputfile, 'w'): pass

    with open(outputfile, 'w') as buffile:
        for fname in files:
            with open(fname) as infile:
                for line in infile:
                    buffile.write(line)
    return outputfile

def Preprocess(outputfile):

    # escape_numbers,removing unwanted tags from the text
    open_file = open(outputfile, "r")
    content=(open_file.read())
    textprocess=Textprocess()
    content=textprocess.preprocess(content)
    return content

def Markov(content,characters):
    # State size is a number of words the probability of a next word depends on.

    final_markov = markovify.Text(content,state_size=3)


    # randomly-generated sentences
    output=(final_markov.make_sentence())
    return output




if __name__ == "__main__":

    input, num_characters, outputfile = parse_args()

    # read and merge txt files into one file
    corpus=read_files(input,outputfile)
    clean_data=Preprocess(corpus)
    output=Markov(clean_data,num_characters)
    print(output)
