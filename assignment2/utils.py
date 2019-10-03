
def to_partitions(X, y, num_partitions, num_records_per_partition):
    partitions = []

    for partition_index in range(0, num_partitions):
        partition = []
        for record_index in range(0, num_records_per_partition):
            i = partition_index * num_records_per_partition + record_index

            x_pi = X[i, :]
            y_pi = y[i]
            record = (i, (x_pi, y_pi))

            partition.append(record)

        partitions.append(partition)

    return partitions