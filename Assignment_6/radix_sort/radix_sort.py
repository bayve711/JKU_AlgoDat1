class RadixSort:
    def __init__(self):
        self.base = 7
        self.bucket_list_history = []

    def get_bucket_list_history(self):
        return self.bucket_list_history

    def sort(self, input_array):
        """
        Sorts a given list using radix sort in descending order
        @param input_array to be sorted
        @returns a sorted list
        """
        self.bucket_list_history.clear()  # clear history list at beginning of sorting
        # TODO
        max_num = self.get_dig_num(input_array)
        bucket_list = []
        for i in range(self.base):
            bucket_list.append([])
        for i in range(max_num-1, -1, -1):
            for j in range(0, len(input_array)):
                bucket_list[self.get_digit(input_array[j], i)].append(input_array[j])
            input_array.clear()
            for j in range(0, self.base):
                for k in range(0, len(bucket_list[j])):
                    input_array.append(bucket_list[j][k])
                bucket_list[j].clear()
            self._add_bucket_list_to_history(bucket_list)
        for i in range(len(bucket_list)):
            for j in range(len(bucket_list[i]) - 1, -1, -1):
                input_array.append(bucket_list[i][j])
        return input_array[::-1]

        # TODO end


    # Helper functions
    def get_dig_num(self, input_array):
        max_val = max(input_array)
        return len(str(max_val))
    # returns the digit (base7) of val at position pos
    def get_digit(self, val, pos):
        return (val // (self.base ** pos)) % self.base

    # calculates buckets for position pos


    def _add_bucket_list_to_history(self, bucket_list):
        """
        This method creates a snapshot (clone) of the bucket list and adds it to the bucket list history.
        @param bucket_list is your current bucket list, after assigning all elements to be sorted to the buckets.
        """
        arr_clone = []
        for i in range(0, len(bucket_list)):
            arr_clone.append([])
            for j in bucket_list[i]:
                arr_clone[i].append(j)
        self.bucket_list_history.append(arr_clone)



