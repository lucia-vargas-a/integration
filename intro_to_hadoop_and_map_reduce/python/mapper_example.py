import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 6:
            date, time, store, item, cost, payment = data
            print ("{0}\t{1}".format(store, cost))
        else:
            print("line withouth the expected format")

#def main():
if __name__ == '__main__':
    import io
    test_text = """2013-10-09\t13:22\tMiami\tBoots\t99.95\tVisa
    2013-10-09\t13:22\tNew York\tDVD\t9.50\tMasterCard
    2013-10-09 13:22:59 I/O Error
    ^d8x28orz28zoijzu1z1zp1OHH3du3ixwcz114<f
    1\t2\t3"""
    sys.stdin = io.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__