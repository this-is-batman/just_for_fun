'''
vector_representations_of_words.py: Script containing the codes to understand anything and everything related to embeddings and vector representations in NLP
Author: Abhirup Gupta
'''

import numpy as np
from nltk.tokenize import word_tokenize
from collections import Counter
from typing import List

def compute_term_doc_mat(vocab: List[str], documents: List[List[str]]) -> np.array:
    """compute_term_doc_matrix: Function to create the term-document matrix
    This matrix contains as rows the terms or the words in the vocabulary and as columns the different documents

    Args:
        vocab (List[str]): These are the list of words in the vocabulary
        documents (List[List[str]]): These are the list of documents in the corpus

    Returns:
        np.array: Returns the term-document matrix
    """

    term_doc_mat = np.zeros((len(vocab), len(documents)))
    for idx,word in enumerate(vocab):
        for doc_idx, document in enumerate(documents):
            word_freq = Counter(document)
            if word in word_freq:
                term_doc_mat[idx,doc_idx] += word_freq[word]
    
    return term_doc_mat


if __name__ == '__main__':
    text = ['Topic sentences are similar to mini thesis statements.\
        Like a thesis statement, a topic sentence has a specific \
        main point. Whereas the thesis is the main point of the essay',\
        'the topic sentence is the main point of the paragraph.\
        Like the thesis statement, a topic sentence has a unifying function. \
        But a thesis statement or topic sentence alone doesn’t guarantee unity.', \
        'An essay is unified if all the paragraphs relate to the thesis,\
        whereas a paragraph is unified if all the sentences relate to the topic sentence.']


 
    documents = []
    vocab = []

    for sent in text:
        x = [i.lower() for i in word_tokenize(sent) if i.isalpha()]
        documents.append(x)
        for word in x:
            if word not in vocab:
                vocab.append(word)


    # computing the term document matrix
    term_doc_mat = compute_term_doc_mat(vocab, documents)
    print(vocab[0], term_doc_mat[0])   # get the counts of the word at idx 0 across the different documents
