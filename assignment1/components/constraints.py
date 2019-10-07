class Constraint:

    def is_satisfied(self, dataframe):
        return False


class HasAtLeastNumRecords(Constraint):
    def __init__(self, num_records):
        self.num_records = num_records

    def is_satisfied(self, dataframe):
        if len(dataframe) >= self.num_records:
            return True
        else:
            return False



class NotNull(Constraint):
    def __init__(self, column):
        self.column = column

    def is_satisfied(self, dataframe):
        answer = dataframe[self.column].isnull()
        for k in answer:
            if k is True:
                return False
        return True



class HasNumDistinctValues(Constraint):
    def __init__(self, column, min_distinct_values, max_distinct_values):
        self.column = column
        self.min_distinct_values = min_distinct_values
        self.max_distinct_values = max_distinct_values

    def is_satisfied(self, dataframe):
        data = dataframe[self.column].dropna()
        num = len(data.unique())
        if num >= self.min_distinct_values and num <= self.max_distinct_values:
            return True

        return False


class IsInRange(Constraint):
    def __init__(self, column, min_value, max_value):
        self.column = column
        self.min_value = min_value
        self.max_value = max_value

    def is_satisfied(self, dataframe):
        min_n = dataframe[self.column].min()
        max_n = dataframe[self.column].max()
        if min_n >= self.min_value and max_n <= self.max_value:
            return True
        return False




class And(Constraint):
    def __init__(self, *constraints):
        self.output = constraints



    def is_satisfied(self, dataframe):
        for obj in self.output:
            if not obj.is_satisfied(dataframe):
                return False
        return True


class Or(Constraint):
    def __init__(self, *constraints):
        self.output = constraints

    def is_satisfied(self, dataframe):

        for obj in self.output:
            if obj.is_satisfied(dataframe):
                return True
        return False
