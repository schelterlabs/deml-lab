from components.beam_job import create_and_run_beam_job
from os import path

# Invoke a beam job to join products and ratings, filter them according to the instructions,
# and count the number of entries per category
create_and_run_beam_job(path_to_products_file='data/products-data-0.tsv', path_to_ratings_file='data/ratings-0.tsv')


# Validate the outputs
assert path.exists('category_counts.tsv-00000-of-00001')

counts = {}
with open('category_counts.tsv-00000-of-00001') as results_file:
    for line in results_file:
        category, count = line.strip().split('\t')
        counts[category] = int(count)

assert 'Kitchen' in counts
assert counts['Kitchen'] == 217

assert 'Jewelry' in counts
assert counts['Jewelry'] == 148