def HamEncoding(msg):
    m = len(msg) 
    k = 1
    while 2**k < m + k + 1:
        k += 1

    # Initialize the encoded message with zeros
    encoded_msg = ['0'] * (m + k)

    j = 0  # Index for the original message
    for i in range(1, m + k + 1):
        if i & (i - 1) == 0:
            # This is a parity bit position
            encoded_msg[i - 1] = '0'  # Initialize parity bit to 0
        else:
            # This is a data bit position
            encoded_msg[i - 1] = msg[j]
            j += 1

    # Calculate parity bits
    for i in range(k):
        parity_position = 2**i
        parity_value = 0
        for j in range(parity_position - 1, len(encoded_msg), 2 * parity_position):
            parity_value ^= int(encoded_msg[j])
        encoded_msg[parity_position - 1] = str(parity_value)

    return ''.join(encoded_msg)

# Test cases
org_sig1 = '1101'
encoded_output1 = HamEncoding(org_sig1)
print(encoded_output1) 

org_sig2 = '1001011'
encoded_output2 = HamEncoding(org_sig2)
print(encoded_output2)
