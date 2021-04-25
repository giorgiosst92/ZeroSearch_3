from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

# read the base params from the config file
input = int(config.get('processing', 'input'))


def zeroes(input):
    # convert number into it's binary
    input = bin(input)

    # remove first two characters of output string
    input = input[2:]

    print("Binary conversion: " + input)

    zeroesList = list(map(len, input.split('1')))

    if zeroesList[-1] == 0:
        return max(zeroesList)
    if zeroesList[-1] != 0:
        zeroesList.pop(-1)
        return max(zeroesList)


# Driver program
if __name__ == '__main__':
    print("The largest number of consecutive 0s surrounded by 1s: ",str(zeroes(input)))
