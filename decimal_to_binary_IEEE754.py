# check to ensure correct decimal data is parsed
def check_validity(data):
    if '-' in data[1:]:
        return False
    split_data = list(data)
    valid_regex = list('0123456789.-')
    radix_pt_cnt = 0
    minus_cnt = 0
    for character in split_data:
        if character not in valid_regex:
            return False
        if character == '.':
            radix_pt_cnt += 1
        if character == '-':
            minus_cnt += 1
    if minus_cnt > 1 or radix_pt_cnt > 1:
        return False
    return True

# binary converter for characters before the radix point
def to_binary_before_radix(decimal):
    remainder_stream = []
    binary_string = ''
    while decimal != 0:
        remainder_stream.append(str(decimal % 2))
        decimal = int(decimal / 2)
    remainder_stream = remainder_stream[::-1]
    return binary_string.join(remainder_stream)

# binary converter for characters after the radix point
def to_binary_after_radix(data, repetition_limit):
    final_output = ''
    decimal = decimalize(data)
    while repetition_limit != 0:
        decimal *= 2
        if decimal == 1.0:
            final_output += '1'
            break
        elif decimal > 1.0:
            final_output += '1'
            decimal -= 1.0
        else:
            final_output += '0'
        repetition_limit -= 1
    return final_output

# returns the value as a 0.xxxx form decimal
def decimalize(data):
    return data / pow(10, len(str(data)))

def main():
    # valid floating point data types
    valid_options = {'float':(8,23), 'double':(11,52), 'long double': (15,112), 'custom': None}

    # keep reading input from user until they choose a valid option
    data_type = input('Enter floating point data type to convert from decimal to binary:\n').strip()

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
    
    # read input for decimal value
    raw_decimal = input(f'Enter your decimal string for {data_type}:\n').strip()
    valid = check_validity(raw_decimal)

    while not valid:
        print('That is an invalid decimal string')
        print(f'You entered {raw_decimal} which contains bits outside the range: [0, 9] or includes characters beside \'-\' and \'.\'')
        raw_decimal = input(f'Enter your binary string for {data_type}:\n').strip()
        valid = check_validity(raw_decimal)

    # extract pieces of information
    if raw_decimal[0] == '-':
        sign = '1'
        raw_decimal = raw_decimal[1:]
    else:
        sign = '0'
    pos_val = raw_decimal.split('.')
    before_radix = pos_val[0]
    after_radix = ''
    if len(pos_val) > 1:
        after_radix = pos_val[1]

    # convert to binary
    before_radix = to_binary_before_radix(int(before_radix))
    exponent_value = len(before_radix[1:])
    if len(pos_val) > 1:
        after_radix = to_binary_after_radix(int(after_radix), mantissa_size - exponent_value)

    # form mantissa
    final_mantissa = before_radix + after_radix
    final_mantissa = final_mantissa[1:]

    # form exponent with bias
    bias = pow(2, exponent_size - 1) - 1
    exp_with_bias = exponent_value + bias
    binary_exponent = to_binary_before_radix(exp_with_bias)
    
    # output final binary
    output = sign + binary_exponent + final_mantissa
    print(f'Your decimal string converts to {output} in binary form (base-2) in accordance with IEEE 754')

if __name__ == '__main__':
    main()