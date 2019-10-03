
class MapReduceEngine:

    def __init__(self, f_m, f_r, num_reducers):
        self.f_m = f_m
        self.f_r = f_r
        self.num_reducers = num_reducers

    def execute(self, partitions):
        # Run the map-phase: for each partition, transform each input record with f_r
        map_outputs = []
        for partition in partitions:
            map_output_for_partition = self.map_partition(partition)
            map_outputs.extend(flatten(map_output_for_partition))

        # Run the shuffle-phase: create as many output partitions as we have reducers, all records with the same
        # key must land in the same group in the same partition
        shuffle_outputs = self.shuffle(map_outputs)

        # Run the reduce phase: apply f_r to every group in every partition
        reduce_outputs = {}
        for partition in shuffle_outputs:
            reduce_output_for_partition = self.reduce_partition(partition)
            reduce_outputs.update(reduce_output_for_partition)

        return reduce_outputs

    def map_partition(self, partition):
        # TODO implement
        pass


    def shuffle(self, map_outputs):
        # TODO implement
        pass

    def reduce_partition(self, partition):
        # TODO implement
        pass


def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]