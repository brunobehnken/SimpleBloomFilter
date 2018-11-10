from random import randint


class BloomFilter:

    def __init__(self, size=1000, gran=1):
        self.bfilter = [False] * size  # The filter itself
        self.gran = gran

    def addElement(self, elem):
        # TODO magic hashing
        pass

    def checkElement(self, elem):
        # TODO magic hashing
        pass


def main():
    false_positives, true_positives, negatives = 0, 0, 0
    control_group = set()
    b_filter = BloomFilter()

    for i in range(0, 400):
        elem = randint(0, 1000)
        b_filter.addElement(elem)
        control_group.add(elem)

    for i in range(0, 400):
        elem = randint(0, 1000)
        if b_filter.checkElement(elem):
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
