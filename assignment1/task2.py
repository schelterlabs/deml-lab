import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from components.learned_imputer import LearnedImputer

# We load product data for evaluation
all_products = pd.read_csv('products.csv', sep='\t')

# We run several experiments with different random seeds
for seed in [42, 129, 788, 555, 123456]:
    data_for_run = all_products.copy(deep=True)

    # We define the names of the column to impute
    column_to_impute = 'category'

    # In some tests, we will change the column names, the imputer should be general enough to handle that
    if seed % 2 == 1:
        column_to_impute = 'Kategorie'
        data_for_run = data_for_run.rename(columns={"category": "Kategorie", "title": "Titel"})

    # We split the data into train and test set
    train_data, test_data = train_test_split(data_for_run, test_size=0.2, random_state=seed)

    # We fit the imputer on the training data, it should learn its internal imputation model now
    imputer = LearnedImputer(column_to_impute)

    imputer.fit(train_data)

    # We create a copy with of the test data and remove the column values to impute
    to_impute = test_data.copy(deep=True)
    to_impute.category = np.nan

    # We have the imputer fill in the missing values
    imputed = imputer.transform(test_data)

    # We compute the accuracy of the imputer by comparing the filled in values to the correct ones
    imputed['correct__'] = test_data[column_to_impute]
    correctly_imputed = imputed[(imputed['correct__'] == imputed[column_to_impute])]

    accuracy = float(len(correctly_imputed)) / len(imputed)

    print("Accuracy:", accuracy)
    assert accuracy >= 0.75
