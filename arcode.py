"""TODO"""
import sys
import re
import pandas

def anycode(obj, file=sys.stdout):
    """TODO"""
    if not pandas.isnull(obj):
        enc = file.encoding
        return obj if enc == 'UTF-8' \
        else str(obj).encode(enc, errors='backslashreplace').decode(enc)

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    """TODO"""
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        refine = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(refine, objects), sep=sep, end=end, file=file)

def clean_str(string, pre_func=None, post_func=None):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    *Note: Modified by @MekkyUA for Arabic language support
    """
    if not pandas.isnull(string):
        if pre_func:
            string = pre_func(string)
        string = re.sub(r"[^ا-يA-Za-z0-9(),؟!?\'\`]", " ", string)
        string = re.sub(r"\'s", " \'s", string)
        string = re.sub(r"\'ve", " \'ve", string)
        string = re.sub(r"n\'t", " n\'t", string)
        string = re.sub(r"\'re", " \'re", string)
        string = re.sub(r"\'d", " \'d", string)
        string = re.sub(r"\'ll", " \'ll", string)
        string = re.sub(r",", " , ", string)
        string = re.sub(r"؟", " ؟ ", string)
        string = re.sub(r"!", " ! ", string)
        string = re.sub(r"\(", " ( ", string)
        string = re.sub(r"\)", " ) ", string)
        string = re.sub(r"\?", " ? ", string)
        string = re.sub(r"\s{2,}", " ", string)
        string = string.strip().lower()
        return post_func(string) if post_func else string
