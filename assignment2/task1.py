from components.schema_validation import infer_schema_from_csv, has_anomalies, adjust_product_schema, adjust_rating_schema

# We infer the schema from the first data file
product_schema = infer_schema_from_csv('data/products-data-0.tsv', column_names=['id', 'category', 'description'])

# We adjust the schema with some constraint that the automatic inference might not have captured
adjust_product_schema(product_schema)

# We use the schema to check for anomalies in subsequent data files
assert not has_anomalies('data/products-data-0.tsv', product_schema)
assert not has_anomalies('data/products-data-1.tsv', product_schema)
assert not has_anomalies('data/products-data-2.tsv', product_schema)
assert has_anomalies('data/products-data-3.tsv', product_schema)

# We infer the schema from the first data file
rating_schema = infer_schema_from_csv('data/ratings-0.tsv', column_names=['id', 'rating'])

# We adjust the schema with some constraint that the automatic inference might not have captured
adjust_rating_schema(rating_schema)

# We use the schema to check for anomalies in subsequent data files
assert not has_anomalies('data/ratings-0.tsv', rating_schema)
assert not has_anomalies('data/ratings-1.tsv', rating_schema)
assert has_anomalies('data/ratings-2.tsv', rating_schema)
assert has_anomalies('data/ratings-3.tsv', rating_schema)