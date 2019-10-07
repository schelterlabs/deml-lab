from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

class LearnedImputer(BaseEstimator, TransformerMixin):

    def __init__(self, target_column):
        self.column = target_column
        self.category = None
        self.clf = None
        self.count_vect = None
        self.tfidf_transformer = None

    def fit(self, dataframe):
        # prepare targets for model

        target_col = dataframe[self.column]
        tem_cat = target_col.unique()
        self.category = {tem_cat[idx]: idx for idx, name in enumerate(tem_cat)}
        target = []
        for i in target_col:
            target += [self.category[i]]

        # prepare features for model (here we only use 'review'
        feature = dataframe['review']
        self.count_vect = CountVectorizer()
        X_train_counts = self.count_vect.fit_transform(feature)
        tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
        X_train_tf = tf_transformer.transform(X_train_counts)
        self.tfidf_transformer = TfidfTransformer()
        X_train_tfidf = self.tfidf_transformer.fit_transform(X_train_counts)

        # train model using naive bayes

        self.clf = MultinomialNB().fit(X_train_tfidf, target)

        return self

    def transform(self, dataframe):

        feature = dataframe['review']
        new_feature = self.count_vect.transform(feature)
        X_new_tfidf = self.tfidf_transformer.transform(new_feature)

        predicted = self.clf.predict(X_new_tfidf)
        real_predicted = []
        for outcome in predicted:
            for i, j in self.category.items():
                if j == outcome:
                    real_predicted += [i]
        dataframe[self.column] = real_predicted

        return dataframe


