import pandas as pd
from components.constraints import NotNull, HasNumDistinctValues, IsInRange, And, Or, HasAtLeastNumRecords

# We load a pandas dataframe with missing values
data = pd.read_csv('adult-sample.csv', na_values='?')

# We evaluate constraints on the number of contained records
assert HasAtLeastNumRecords(500).is_satisfied(data)
assert not HasAtLeastNumRecords(501).is_satisfied(data)

# We evaluate constraints on the range of values in the 'age' column
assert IsInRange('age', 17, 90).is_satisfied(data)
assert IsInRange('age', 10, 100).is_satisfied(data)
assert not IsInRange('age', 50, 100).is_satisfied(data)

# We evaluate constraints on the completeness of the 'age' and 'workclass' column
assert NotNull('age').is_satisfied(data)
assert not NotNull('workclass').is_satisfied(data)

# We evaluate constraints on the completeness of the 'workclass' and 'education' column
assert HasNumDistinctValues('workclass', 8, 8).is_satisfied(data)
assert HasNumDistinctValues('workclass', 0, 10).is_satisfied(data)
assert not HasNumDistinctValues('workclass', 10, 20).is_satisfied(data)
assert HasNumDistinctValues('education', 16, 16).is_satisfied(data)

# We evaluate boolean expressions built from of constraints
assert And(HasAtLeastNumRecords(500), NotNull('age'), IsInRange('age', 17, 90)).is_satisfied(data)
assert And(HasAtLeastNumRecords(500), NotNull('age'), IsInRange('age', 17, 90)).is_satisfied(data)
assert Or(NotNull('age'), NotNull('workclass')).is_satisfied(data)

constraint = And(
    And(HasAtLeastNumRecords(500), NotNull('age'), IsInRange('age', 17, 90)),
    Or(NotNull('age'), NotNull('workclass')))

assert constraint.is_satisfied(data)

