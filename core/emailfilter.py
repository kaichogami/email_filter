"""
   Implements Bayes theorem to calculate the probabilty that a given sentence
   is spam or not spam. This is terribly inaccurate if it has a low training data.
   Therefore it is necessary to train it with large amount of data.
"""

class NaiveBayes:

    def __init__(self):
        self.trivial = ['the', 'of', 'a', 'an', '.', ',']
        self.category = {'spam' : 0.0, 'ham' : 0.0}
        self.words = {}
        self.sents = 0.0

    def train(self, text, category):
        #work with text
        text = text.lower()
        words = text.split(' ')
        for word in words:

            if word in self.trivial:
                continue

            try:
                self.words[word]["count"] += 1
            except:
                self.words[word] = {'count' : 0.0, 'spam' : 0.0, 'ham' : 0.0}
                self.words[word]['count'] = 1.0

            #category here means the total number of times
            #word comes in particular category
            #P(word/category) = self.words[word]['count'] / self.words[word][category]
            
            self.words[word][category] += 1

        self.category[category] += 1
        self.sents += 1


    def classify(self, text):
        text = text.lower()
        words = text.split(' ')

        #prior information
        pspam = self.category['spam'] / self.sents
        pham = self.category['ham'] / self.sents
        print(pspam, pham)
        
        #calculate probabilty of text being spam or ham
        default = 'undefine'

        for word in words:
            #division of p(wordi) is not needed as it is a constant and equal for both
            if not word in self.words:
                continue

            print(self.words[word])
            if self.words[word]['spam'] == 0 and self.words[word]['ham'] != 0:
                pham = pham * (self.words[word]['ham'] / self.words[word]['count'])

            elif self.words[word]['ham'] == 0 and self.words[word]['spam'] != 0:
                pspam = pspam * (self.words[word]['spam'] / self.words[word]['count'])

            else:
                pspam = pspam * (self.words[word]['spam'] / self.words[word]['count'])
                pham = pham * (self.words[word]['ham'] / self.words[word]['count'])


        print(pspam, pham)
        if pspam >= pham:
            return "spam"
        elif pspam < pham:
            return 'ham'
        else:
            return default

if __name__ == '__main__':
    n = NaiveBayes()
    n.train('get viagra for just rupess 10', 'spam')
    n.train('Use viagra if you need medical attention', 'ham')
    n.train('a strong penis needs a strong viagra', 'spam')
    n.train('No use of getting yourself into trouble with your wife for a small matter as penis', 'spam')
    n.train('Meet me tomorrow at India', 'ham')
    n.train('we meet today near India now', 'ham')
    n.train('meeting now is not required', 'ham')
    print(n.classify('meet me now with viagra and your penis'))
