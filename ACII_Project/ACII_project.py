import binascii


def convert_string_to_list(string):
    list1=[]
    list1[:0]=string
    return list1

def take_firsttwo_makeone_inlist(list):
    #Takes first two elements in list and makes them into one element and then it returns
    #that into a new list
    new_list = []
    for i in range(8):
        new_list.append(''.join(list[:2]))
        list = list[2:]
    return new_list

def undo_tfmi(list):
    new_list =[]
    for i in list:
        string = i[:8]
        string2 = i[8:]
        new_list.append(string)
        new_list.append(string2)
    return new_list

def print_pretty(list):
    #Makes the steps easier to read
    list = take_firsttwo_makeone_inlist(list)
    for i in list:
        print(i)
    print("\n")

def get_input():
    #This function gets the inputs we need and returns them into a list
    line = ""
    for i in range(8):
       line += input()
    hex_list = [line[i:i+2] for i in range(0, len(line), 2)]
    return hex_list

def convert_hex_bin(hexdata):
    #This takes in the hex code and says the scale needs to be 16 then it fills the 0 for
    #the number of bits which is 8
    return bin(int(hexdata, 16))[2:].zfill(8)

def copy_paste(list):
    list = take_firsttwo_makeone_inlist(list)
    new_list = []
    for i in list:
        string = convert_string_to_list(i)
        char = string.pop(0)
        string.insert(8, char)
        string = ''.join(string)
        new_list.append(string)
    
    new_list = undo_tfmi(new_list)
    return new_list

def addition_subtraction(list):
    even = [0, 2, 4, 6]
    odd = [1, 3, 5, 7]
    count = 0
    new_list = []
    for i in range(8):
        if count in even:
            for i in list[:2]:
                #plus binary
                string = bin(int(i, 2) + count)
                new_list.append(string)
            count += 1
            del list[:2]
        elif count in odd:
            for i in list[:2]:
                #subtract binary
                string = bin(int(i,2) - count)
                new_list.append(string)
            count += 1
            del list[:2]
    return new_list
    
def convert_bin_acii(list):
    new_list = []
    for i in list:
        binary_int = int(i, 2)
        byte_number = binary_int.bit_length() + 7 // 8

        binary_array = binary_int.to_bytes(byte_number, "big")
        ascii_text = binary_array.decode(encoding='windows-1252')
        new_list.append(ascii_text)
    return new_list


list = get_input()
print("STEP 1: Take in the inputs")
print(list)
print_pretty(list)

list = [convert_hex_bin(i) for i in list]
print("STEP 2: Make them into binary")
print(list)
print_pretty(list)

list = copy_paste(list)
print("STEP 3: Do the copy paste thingy majiggy")
print(list)
print_pretty(list)

list = addition_subtraction(list)
print("Step 4: addition subtracti")
print(list)
print_pretty(list)

list = convert_bin_acii(list)
print(''.join(list))
