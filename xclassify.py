"""TODO"""
import pandas
import nltk
nltk.download('punkt') # skip if already downloaded
from sklearn.cross_validation import train_test_split
from textblob.classifiers import NaiveBayesClassifier
from arcode import anycode, clean_str

class XcLassify(object):
    """TODO"""
    def __init__(self):
        self.__cl = None
        self.__traindata = None
        self.__testdata = None

    def _fetch_clean(self, filepath):
        """TODO"""
        dframe = pandas.read_excel(filepath)
        dframe.iloc[:, 0] = dframe.iloc[:, 0].map(clean_str)
        dframe.iloc[:, 0] = dframe.iloc[:, 0].map(anycode)
        return dframe.iloc[:, 0:2].to_records(index=False).tolist()

    def _split_data(self, datalist, test_ratio):
        """TODO"""
        self.__traindata, self.__testdata = train_test_split(datalist, test_size=test_ratio)
        return self.__traindata, self.__testdata

    def data_from_excel(self, filepath, test_ratio=0.24):
        datalist = self._fetch_clean(filepath)
        return self._split_data(datalist, 0.2)

    def train(self, update=False, new_data=None):
        """TODO"""
        if update and new_data:
            self.__cl.update(new_data)
        else:
            self.__cl = NaiveBayesClassifier(self.__traindata)

    def classify(self, text):
        """TODO"""
        text = clean_str(text, post_func=anycode)
        return self.__cl.classify(text)

    def benchmark(self, show_best_features=False):
        """TODO"""
        print('\nAccuracy: %0.3f\n' % self.__cl.accuracy(self.__testdata))
        if show_best_features:
            self.__cl.show_informative_features()

# test area
if __name__ == '__main__':
    XCL = XcLassify()
    XCL.data_from_excel('data/data_sample.xlsx')
    XCL.train()
    print(XCL.classify("الباقة خلصت وسحب من الرصيد بدون اخطار قبلها!"))
    print(XCL.classify("ازاى اجدد باقة النت قبل ميعادها؟"))
    print(XCL.classify("لو سمحت عاوز اقدم شكوى فى الفرع"))
    XCL.benchmark(show_best_features=True)
else:
    pass
