class Constraint:

    def is_satisfied(self, dataframe):
        return False


class HasAtLeastNumRecords(Constraint):
    def __init__(self, num_records):
        pass

    # TODO Implement


class NotNull(Constraint):
    def __init__(self, column):
        pass

    # TODO Implement


class HasNumDistinctValues(Constraint):
    def __init__(self, column, min_distinct_values, max_distinct_values):
        pass

    # TODO Implement


class IsInRange(Constraint):
    def __init__(self, column, min_value, max_value):
        pass

    # TODO Implement


class And(Constraint):
    def __init__(self, *constraints):
        pass

    # TODO Implement


class Or(Constraint):
    def __init__(self, *constraints):
        pass

    # TODO Implement
