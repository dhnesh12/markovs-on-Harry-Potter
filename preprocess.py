import re,nltk,sys
from string import punctuation
from nltk.corpus import stopwords
stopwords.words('english')


class Textprocess:
    def __int__(self):
        pass

    def correctspell(self,text):
        """
        to correct the spelling of any word.
        """
        doc = nlp(text)
        output = (doc._.outcome_spellCheck)

        return str(output)


    def escape_numbers(self,text):
        """
        take input as string and output number free texts
        """
        result = ''.join(data for data in text if not data.isdigit())
        return result

    def remove_punct(self,text):
        """
        take input as string and clean string without punctuations.
        use regex to remove the punctuations.
        """
        return ''.join(c for c in text if c not in punctuation)

    def sentence_tokenize(self,text):
        """
        take string input and return list of sentences.
        use nltk.sent_tokenize() to split the sentences.
        """
        output = []
        for data in nltk.sent_tokenize(text):
            output.append(data)
        return output

    def remove_Tags(self,text):
        """
        take string input and clean string without tags.
        use regex to remove the html tags.
        """
        cleaned_text = re.sub('<[^<]+?>', '', text)
        return cleaned_text

    def sentence_tokenize(self,text):
        """
        take string input and return list of sentences.
        use nltk.sent_tokenize() to split the sentences.
        """
        sent_list = []
        for w in nltk.sent_tokenize(text):
            sent_list.append(w)
        return sent_list

    def word_tokenize(self,text):
        """
        :param text:
        :return: list of words
        """
        return [data for sent in nltk.sent_tokenize(text) for data in nltk.word_tokenize(sent)]


    def preprocess(self,text):
        sentence_tokens = self.sentence_tokenize(text)
        word_list = []
        for each_sent in sentence_tokens:

            clean_text = self.escape_numbers(each_sent)
            # clean_text = self.remove_punct(clean_text)
            clean_text = self.remove_Tags(clean_text)


            word_list.append(clean_text)


        return ' '.join(c for c in word_list)
