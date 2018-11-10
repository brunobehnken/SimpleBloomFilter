from random import randint


class BloomFilter:

    def __init__(self, size=1000, gran=1):
        self.bfilter = [False] * size  # The filter itself
        self.size = size  # size of the filter
        self.gran = gran  # Granularity of the filter

    def __get_pos(self, elem, i):
        hashcode = hash((elem, i))
        while hashcode >= self.size:
            resto = hashcode % self.size
            hashcode = hashcode // self.size
            hashcode += resto
        return hashcode

    def add_element(self, elem):
        for i in range(0, self.gran):
            pos = self.__get_pos(elem, i)
            if not self.bfilter[pos]:
                self.bfilter[pos] = True

    def check_element(self, elem):
        for i in range(0, self.gran):
            pos = self.__get_pos(elem, i)
            if not self.bfilter[pos]:
                return False
        return True


def main():
    false_positives, true_positives, negatives = 0, 0, 0
    control_group = set()
    b_filter = BloomFilter()

    for i in range(0, 400):
        elem = randint(0, 1000)
        b_filter.add_element(elem)
        control_group.add(elem)

    for i in range(0, 400):
        elem = randint(0, 1000)
        if b_filter.check_element(elem):
            if elem in control_group:
                true_positives += 1
            else:
                false_positives += 1
        else:
            negatives += 1

    print(f"false positives {false_positives}\n"
          f"true positives {true_positives}\n"
          f"negatives {negatives}")


main()
