import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from components.learned_imputer import LearnedImputer

all_products = pd.read_csv('products.csv', sep='\t')

for seed in [42, 129, 788, 555, 123456]:
    data_for_run = all_products.copy(deep=True)

    column_to_impute = 'category'

    if seed % 2 == 1:
        column_to_impute = 'Kategorie'
        data_for_run = data_for_run.rename(columns={"category": "Kategorie", "title": "Titel"})

    train_data, test_data = train_test_split(data_for_run, test_size=0.2, random_state=seed)

    imputer = LearnedImputer(column_to_impute)

    imputer.fit(train_data)

    to_impute = test_data.copy(deep=True)
    to_impute.category = np.nan

    imputed = imputer.transform(test_data)

    imputed['correct__'] = test_data[column_to_impute]

    correctly_imputed = imputed[(imputed['correct__'] == imputed[column_to_impute])]

    accuracy = float(len(correctly_imputed)) / len(imputed)

    print("Accuracy:", accuracy)
    assert accuracy >= 0.75
