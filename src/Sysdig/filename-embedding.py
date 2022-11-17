from gensim.models import FastText
from gensim.models.doc2vec import TaggedDocument
from argparse import ArgumentParser
import re
import pandas as pd
from nostril import nonsense
import string
from tools import sanitize_string


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--epoch",type = int,default=100)
    parser.add_argument("--e",type = int, default=256)
    parser.add_argument("--d",type = str, default='hw17')
    args = parser.parse_args()
    epoch = args.epoch
    dataset = args.d
    embedding_size = args.e
    input_file = dataset + '/filename.txt'
    pathname = []
    corpus = []
    f = open(input_file,'r')
    while True:
        line = f.readline()
        if not line:
            break
        if line == '\n' or line == 'None' or line == 'none':
            continue
    
        splitline = sanitize_string(line)
        print(splitline)

        corpus.append(splitline)
    # input_file = 'process-event-anomaly.txt'
    # f = open(input_file,'r')
    # while True:
    #     line = f.readline()
    #     if not line:
    #         break
    #     if line == '\n' or line == 'None' or line == 'none':
    #         continue
    #     line = line.strip().lower()
    #     if line.endswith('$$$true'):
    #         line = line.replace('$$$true','')
    #     elif line.endswith('$$$false'):
    #         line = line.replace('$$$false','')
    #     # print(line)
    #     splitline = sanitize_string(line)
    #     print(splitline)

    #     corpus.append(splitline)

    # print('finished path')


    model = FastText(min_count = 2, vector_size=embedding_size, workers= 30, alpha=0.01,window=3,negative=3)
    model.build_vocab(corpus)
    model.train(corpus,epochs=epoch,total_examples=model.corpus_count)
    model.save(dataset + '/filepath-embedding.model')
# model = word2vec.Word2Vec.load('line-embedding-cadets.model')

# print(model.wv['<unk>'])
# model = Doc2Vec.load('cmdline.model')

