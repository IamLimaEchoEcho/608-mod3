#Lee Jones 
import sys

def maximum(value1 = 12, value2 = 27, value3 = 36): 
    """Return the maximum of three values."""
    max_value = value1
    if value2 > max_value: 
        max_value = value2
    if value3 > max_value: 
        max_value = value3
    return max_value

def minimum(value1, value2, value3, value4): 
    """Return the minimum of three values."""
    min_value = value1
    if value2 < min_value: 
        min_value = value2
    if value3 < min_value: 
        min_value = value3
    if value4 < min_value: 
        min_value = value4
    return min_value    

#max and min from command line with arguments
if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    d = int(sys.argv[4])
    print("BIF max = ", max(a, b, c, d))
    print("BIF min = ", min(a, b, c, d))

#print(f'Input numbers: {value1}, {value2}, and {value3}')
print("The maximum value is", maximum(12, 27, 36))
print("The minimum value is", minimum(15, 9, 27, 14))

print("Lee Jones")
