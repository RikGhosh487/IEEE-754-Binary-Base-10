# check to ensure only binary data is parsed
def check_validity(data):
    split_data = list(data)
    for bit in split_data:
        if bit != '0' and bit != '1':
            return False
    return True

# padding function to adjust for missing data
def pad(data, padding_length):
    if len(data) == padding_length:
        return data
    pad_amt = padding_length - len(data) + 1
    while pad_amt != 0:
        data += '0'
        pad_amt -= 1
    return data

# decimal converter for bits before the radix point
def to_decimal_before_radix(binary):
    final_output = 0
    split_binary = list(binary)
    i = 0
    for bit in reversed(split_binary):
        if bit == '1':
            final_output += pow(2, i)
        i += 1
    return final_output

# decimal converter for bits after the radix point
def to_decimal_after_radix(binary):
    final_output = 0
    split_binary = list(binary)
    i = 1
    for bit in split_binary:
        if bit == '1':
            final_output += pow(2, -1 * i)
        i += 1
    return final_output

def main():
    # valid floating point data types
    valid_options = {'float':(8,23), 'double':(11,52), 'long double': (15,112), 'custom': None}

    # keep reading input from user until they choose a valid option
    data_type = input('Enter floating point data type to convert from binary to decimal:\n').strip()

    while data_type not in valid_options.keys():
        print('That is an invalid floating point data type')
        print(f'You entered {data_type}, but valid choices include:\n{list(valid_options.keys())}')
        data_type = input('Please pick one of the data types listed above:\n').strip()

    if data_type != 'custom':
        exponent_size = valid_options[data_type][0]
        mantissa_size = valid_options[data_type][1]
    else:
        mantissa_size = int(input('Please enter a p-value (for mantissa):\n').strip()) - 1
        exponent_size = int(input('Please enter a q-value (for exponent):\n').strip())

    # read input for the binary
    raw_binary = input(f'Enter your binary string for {data_type}:\n').strip()
    valid = check_validity(raw_binary)

    while not valid:
        print('That is an invalid binary string')
        print(f'You entered {raw_binary} which contains bits outside the range: [0, 1]')
        raw_binary = input(f'Enter your binary string for {data_type}:\n').strip()
        valid = check_validity(raw_binary)
    
    if len(raw_binary) > exponent_size + mantissa_size + 1:
        raw_binary = raw_binary[:exponent_size + mantissa_size + 2] # 1 for signed bit and 1 for exclusion point
    else:
        raw_binary = pad(raw_binary,exponent_size + mantissa_size + 1)
    
    # obtain values from bit string
    sign = raw_binary[0]
    biased_exponent = raw_binary[1:exponent_size + 1]
    mantissa = raw_binary[exponent_size + 1:]
    
    # adjust for bias amount
    bias = pow(2, exponent_size - 1) - 1
    exponent = to_decimal_before_radix(biased_exponent) - bias

    # get pre-radix and post-radix values
    pre_radix = to_decimal_before_radix('1' + mantissa[:exponent])
    post_radix = to_decimal_after_radix(mantissa[exponent:])

    # compute value
    output = pre_radix + post_radix
    if sign == '1':
        output *= -1

    print(f'Your binary string converts to {output} in decimal form (base-10)')

if __name__ == '__main__':
    main()
