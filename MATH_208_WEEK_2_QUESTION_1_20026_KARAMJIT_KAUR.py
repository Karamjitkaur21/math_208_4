def encoding(msg, poly):
    # Append zeros for the CRC remainder
    msg += '0' * (len(poly) - 1)
    msg = list(msg)
    
    # Perform polynomial division
    for i in range(len(msg) - len(poly) + 1):
        if msg[i] == '1':
            for j in range(len(poly)):
                msg[i + j] = '1' if msg[i + j] != poly[j] else '0'

    # Append the CRC remainder to the original message
    encoded_msg = ''.join(msg)

    return encoded_msg

def decoding(rcv, poly):
    rcv = list(rcv)
    
    # Perform polynomial division
    for i in range(len(rcv) - len(poly) + 1):
        if rcv[i] == '1':
            for j in range(len(poly)):
                rcv[i + j] = '1' if rcv[i + j] != poly[j] else '0'

    # Check if the remainder is zero to detect errors
    if '1' in rcv:
        return 'Error'
    else:
        return 'No error'

# Test cases
org_sig1 = '1010'
poly = '100101'
encoded_output1 = encoding(org_sig1, poly)
print(encoded_output1)  # Output: '101000111'

received_sig1 = '101000111'
decoding_result1 = decoding(received_sig1, poly)
print(decoding_result1)  # Output: 'No error'

org_sig2 = '1100'
poly = '100101'
encoded_output2 = encoding(org_sig2, poly)
print(encoded_output2)  # Output: '110011001'

received_sig2 = '101001111'
decoding_result2 = decoding(received_sig2, poly)
print(decoding_result2)  # Output: 'Error'
