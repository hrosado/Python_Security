import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))

# The following example is from: docs.python on argparse.html
# parser = argparse.ArgumentParser(description="Process some integers.")
# parser.add_argument('integers', metavar='N',type=int,nargs='+',help='an integer accumulator')
# parser.add_argument('--sum',dest='accumulate', action='store_const',const=sum, default=max,help='sum the integers (default: find the max)')

# args = parser.parse_args()
# print(args.acculate(args.integers))


# parser = argparse.ArgumentParser(description='Testing parameters')

# parser.add_argument("-p1", dest="param1", help="parameter1")
# parser.add_argument("-p2", dest="param2", help="parameter2")

# params = parser.parse_args()

# print("Parameter 1", params.param1)
# # print("Parameter 2", params.param2)

