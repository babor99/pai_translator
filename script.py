import sys, getopt, os, json

from helper import translateDataAndMakePDF


def main(argv):
    output_filename = ''
    json_dict = {}
    try:
        opts, args = getopt.getopt(argv,"hj:o:", ["json=","output="])
        print('opts: ', opts)
        print('args: ', args)
    except getopt.GetoptError:
        print(f'{os.path.basename(__file__)} --json <inputfile> --output <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--json"):
            try:
                with open(arg, 'r') as file:
                    json_dict = json.load(file)
                    print('lang: ', json_dict['languages'])
                    print('json_dict: ', json_dict)
                    print('json_dict len: ', len(json_dict))
            except FileNotFoundError as e:
                print(e)
        elif opt in ("-o", "--output"):
            output_filename = arg

    if len(json_dict) > 1:
        translateDataAndMakePDF(json_dict, output_filename)
    else:
        sys.exit('Your json file have not enough data or ')


if __name__ == "__main__":
   main(sys.argv[1:])