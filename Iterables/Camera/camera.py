import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--cameras", type=str, dest='camera_file', required=True, help="A properly formatted file containing the locations of cameras\n")
parser.add_argument("--cameras-in-city", dest='city', help="Queries input files for all cameras in a city")
parser.add_argument("--cameras-on-road", dest='road', help="Queries input files for all cameras on a certain road")

def parse(cams):

    iterator = iter(cams)
    next(iterator)
    next(iterator)

    cameras = []

    for line in iterator:
        var = line.split(',')
        var[-1] = var[-1].rstrip('\n')
        cameras.append(tuple(var))

    #delete last 9 lines from the file
    del(cameras[-9:])

    return tuple(cameras)


def print_cams(cams):
    for cam in cams:
        print("Camera on %s at km %s %s in %s (%s)" %
              (cam[2], cam[3], cam[4], cam[1], cam[0]))
    print("")


args = parser.parse_args()

#actual program
with open(args.camera_file) as inputfile:
    cameras = parse(inputfile)

if args.city:
    cams = filter(lambda x: args.city == x[1], cameras)
    print("Cameras in {}".format(args.city))
    print_cams(cams)

if args.road:
    cams = filter(lambda x: args.road == x[2], cameras)
    print("Cameras on {}">format(args.road))
    print_cams(cams)
