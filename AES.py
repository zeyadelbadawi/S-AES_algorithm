import tkinter as tk
from tkinter import messagebox



def Encryption():
    plain_str = plaintext_entry.get()
    key_str = key_entry.get()

    if len(key_str) != 16:
        messagebox.showerror(
            "Error", "Key or plaintext must contain exactly 16 digits.")
        return

        
    key_is_binary = all(bit in "01" for bit in key_str)
    plain_is_binary = all(bit in "01" for bit in plain_str)

    
    if key_is_binary:
        print("Key is binary.")
        
    else:
        messagebox.showerror(
        "Error", "Key must be binary")
        

    if plain_is_binary:
        print("plain is binary.")
        
    else:
        messagebox.showerror(
        "Error", "plaintext must be binary")
        
        


    w2_helper = "10000000"
    w4_helper = "00110000"

    matrix = [
        ["0000", "1001"],
        ["0001", "0100"],
        ["0010", "1010"],
        ["0011", "1011"],
        ["0100", "1101"],
        ["0101", "0001"],
        ["0110", "1000"],
        ["0111", "0101"],
        ["1000", "0110"],
        ["1001", "0010"],
        ["1010", "0000"],
        ["1011", "0011"],
        ["1100", "1100"],
        ["1101", "1110"],
        ["1110", "1111"],
        ["1111", "0111"],
    ]
    Multi = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [2, 4, 6, 8, 10, 12, 14, 3, 1, 7, 5, 11, 9, 15, 13],
        [3, 6, 5, 12, 15, 10, 9, 11, 8, 13, 14, 7, 4, 1, 2],
        [4, 8, 12, 3, 7, 11, 15, 6, 2, 14, 10, 5, 1, 13, 9],
        [5, 10, 15, 7, 2, 13, 8, 14, 11, 4, 1, 9, 12, 3, 6],
        [6, 12, 10, 11, 13, 7, 1, 5, 3, 9, 15, 14, 8, 2, 4],
        [7, 14, 9, 15, 8, 1, 6, 13, 10, 3, 4, 2, 5, 12, 11],
        [8, 3, 11, 6, 14, 5, 13, 12, 4, 15, 7, 10, 2, 9, 1],
        [9, 1, 8, 2, 11, 3, 10, 4, 13, 5, 12, 6, 15, 7, 14],
        [10, 7, 13, 14, 4, 9, 3, 15, 5, 8, 2, 1, 11, 6, 12],
        [11, 5, 14, 10, 1, 15, 4, 7, 12, 2, 9, 13, 6, 8, 3],
        [12, 11, 7, 5, 9, 14, 2, 10, 6, 1, 13, 15, 3, 4, 8],
        [13, 9, 4, 1, 12, 8, 5, 2, 15, 11, 6, 3, 14, 10, 7],
        [14, 15, 1, 13, 3, 2, 12, 9, 7, 6, 8, 4, 10, 11, 5],
        [15, 13, 2, 9, 6, 4, 11, 1, 14, 12, 3, 8, 7, 5, 10],
    ]
    Add = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],
        [2, 3, 0, 1, 6, 7, 4, 5, 10, 11, 8, 9, 14, 15, 12, 13],
        [3, 2, 1, 0, 7, 6, 5, 4, 11, 10, 9, 8, 15, 14, 13, 12],
        [4, 5, 6, 7, 0, 1, 2, 3, 12, 13, 14, 15, 8, 9, 10, 11],
        [5, 4, 7, 6, 1, 0, 3, 2, 13, 12, 15, 14, 9, 8, 11, 10],
        [6, 7, 4, 5, 2, 3, 0, 1, 14, 15, 12, 13, 10, 11, 8, 9],
        [7, 6, 5, 4, 3, 2, 1, 0, 15, 14, 13, 12, 11, 10, 9, 8],
        [8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7],
        [9, 8, 11, 10, 13, 12, 15, 14, 1, 0, 3, 2, 5, 4, 7, 6],
        [10, 11, 8, 9, 14, 15, 12, 13, 2, 3, 0, 1, 6, 7, 4, 5],
        [11, 10, 9, 8, 15, 14, 13, 12, 3, 2, 1, 0, 7, 6, 5, 4],
        [12, 13, 14, 15, 8, 9, 10, 11, 4, 5, 6, 7, 0, 1, 2, 3],
        [13, 12, 15, 14, 9, 8, 11, 10, 5, 4, 7, 6, 1, 0, 3, 2],
        [14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3, 0, 1],
        [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    ]

    hexx = [
        ["0000", "0"],
        ["0001", "1"],
        ["0010", "2"],
        ["0011", "3"],
        ["0100", "4"],
        ["0101", "5"],
        ["0110", "6"],
        ["0111", "7"],
        ["1000", "8"],
        ["1001", "9"],
        ["1010", "10"],
        ["1011", "11"],
        ["1100", "12"],
        ["1101", "13"],
        ["1110", "14"],
        ["1111", "15"],
    ]


    helper_matrix = [
        ["1", "4"],
        ["4", "1"],
    ]
    helper_matrix2 = [
        ["9", "2"],
        ["2", "9"],
    ]    

    # calculate w0,w1
    w0 = key_str[:8]
    w1 = key_str[8:]

    # calculate rotnib w1
    w1_left = w1[:4]
    w1_right = w1[4:]
    RotNib = w1_right + w1_left

    # calculate subnib
    RotNib_left = RotNib[:4]
    RotNib_right = RotNib[4:]
    rib_left_value = None
    rib_right_value = None
    for row in matrix:
        if row[0] == RotNib_left:
            rib_left_value = row[1]
        if row[0] == RotNib_right:
            rib_right_value = row[1]
    SubNib = rib_left_value + rib_right_value

    # calculate w2,w3
    help_w2 = bin(int(w0, 2) ^ int(w2_helper, 2))[2:].zfill(8)
    w2 = bin(int(help_w2, 2) ^ int(SubNib, 2))[2:].zfill(8)
    w3 = bin(int(w2, 2) ^ int(w1, 2))[2:].zfill(8)

    # calculate rotnib w3
    w3_left = w3[:4]
    w3_right = w3[4:]
    RotNib2 = w3_right + w3_left

    # calculate subnib2
    RotNib2_left = RotNib2[:4]
    RotNib2_right = RotNib2[4:]
    rib2_left_value = None
    rib2_right_value = None

    for row in matrix:
        if row[0] == RotNib2_left:
            rib2_left_value = row[1]
        if row[0] == RotNib2_right:
            rib2_right_value = row[1]
    SubNib2 = rib2_left_value + rib2_right_value

    # calculate w4,w5
    help_w4 = bin(int(w2, 2) ^ int(w4_helper, 2))[2:].zfill(8)
    w4 = bin(int(help_w4, 2) ^ int(SubNib2, 2))[2:].zfill(8)
    w5 = bin(int(w4, 2) ^ int(w3, 2))[2:].zfill(8)

    # calculate sub-keys
    key0 = w0 + w1
    key1 = w2 + w3
    key2 = w4 + w5


########################################### STEP2###############################################################
########################################### STEP2###############################################################
########################################### STEP2###############################################################

    # calculate Add_Round_Key1
    Add_Round_Key1 = bin(int(plain_str, 2) ^ int(key0, 2))[2:].zfill(16)
   ## print('Add_Round_Key1: '+str(Add_Round_Key1))
    # calculate shift_left1
    part1 = Add_Round_Key1[:4]
    part2 = Add_Round_Key1[4:8]
    part3 = Add_Round_Key1[8:12]
    part4 = Add_Round_Key1[12:]

    S00 = None
    S11 = None
    S01 = None
    S10 = None

    for row in matrix:
        if row[0] == part1:
            S00 = row[1]
        if row[0] == part2:
            S11 = row[1]
        if row[0] == part3:
            S01 = row[1]
        if row[0] == part4:
            S10 = row[1]

    shift_left1 = S00 + S10 + S01 + S11
    shift_matrix = [
        [S00, S01],
        [S10, S11],
    ]

    hex_value = None
    for row in hexx:
        if row[0] == shift_matrix[0][1]:
            hex_value = row[1]
          ###  print('hex_value: '+str(hex_value))
            break

    hex_value2 = None
    for row in hexx:
        if row[0] == shift_matrix[0][0]:
            hex_value2 = row[1]
          ##  print('hex_value2: '+str(hex_value2))

            break

    hex_value3 = None
    for row in hexx:
        if row[0] == shift_matrix[1][0]:
            hex_value3 = row[1]
         ##   print('hex_value3: '+str(hex_value3))
            break

    hex_value4 = None
    for row in hexx:
        if row[0] == shift_matrix[1][1]:
            hex_value4 = row[1]
          ##  print('hex_value4: '+str(hex_value4))
            break

    xs = 4
 ##   print('xs: '+str(xs))
#######################S00#############################
    r = None
    for row_idx, row in enumerate(Multi):
        if row[0] == int(hex_value3):
            r = row_idx
       ##     print('R: '+str(r))
            break

    c = None
    for col_idx, row in enumerate(Multi):
        if row[0] == 4:
            c = col_idx
         ##   print('C:', c)
            break

    if r is not None and c is not None:
        xb = Multi[r][c]
       ## print('xb '+str(xb))

    r2 = None
    for row2_idx, row in enumerate(Add):
        if row[0] == int(hex_value2):
            r2 = row2_idx
          ##  print('r2:', r2)

            break

    c2 = None
    for col2_idx, row in enumerate(Add):
        if row[0] == xb:
            c2 = col2_idx
          ##  print('c2:', c2)

            break

    if r2 is not None and c2 is not None:
        xxx= None
        xxx = Add[r2][c2]
       ## print('xxx:', xxx)

    S00_ = None
    for row in hexx:
        if row[1] == str(xxx):
            S00_ = row[0]
         ##   print('S00:', str(S00_))
            break


########################################S10################################################


    r3 = None
    for row_idx, row in enumerate(Multi):
        if row[0] == int(hex_value2):
            r3 = row_idx
           ## print('R3: '+str(r3))
            break

    c3 = None
    for col_idx, row in enumerate(Multi):
        if row[0] == 4:
            c3 = col_idx
     ##       print('C3:', c3)
            break

    if r3 is not None and c3 is not None:
        xb2 = Multi[r3][c3]
       ## print('xb2 '+str(xb2))

    r4 = None
    for row2_idx, row in enumerate(Add):
        if row[0] == int(hex_value3):
            r4 = row2_idx
      ##      print('r4:', r4)

            break

    c4 = None
    for col2_idx, row in enumerate(Add):
        if row[0] == xb2:
            c4 = col2_idx
       ##     print('c4:', c4)
            break

    if r4 is not None and c4 is not None:
        xxxxx = None
        xxxxx = Add[r4][c4]
       # print('xxxxx:', xxxxx)
    
    S10_ = None
    for row in hexx:
        if row[1] == str(xxxxx):
            S10_ = row[0]
       #     print('S10:', S10_)
            break

################################S01###########################################

    r = None
    for row_idx, row in enumerate(Multi):
        if row[0] == int(hex_value4):
            r = row_idx
       #     print('R: '+str(r))
            break

    c = None
    for col_idx, row in enumerate(Multi):
        if row[0] == 4:
            c = col_idx
          #  print('C:', c)
            break

    if r is not None and c is not None:
        xb = None

        xb = Multi[r][c]
      #  print('xb '+str(xb))

    r2 = None
    for row2_idx, row in enumerate(Add):
        if row[0] == int(hex_value):
            r2 = row2_idx
       #     print('r2:', r2)

            break

    c2 = None
    for col2_idx, row in enumerate(Add):
        if row[0] == xb:
            c2 = col2_idx
       #     print('c2:', c2)

            break

    if r2 is not None and c2 is not None:
        s01__ = None

        s01__ = Add[r2][c2]
      #  print('s01__:', s01__)

    S01_ = None
    for row in hexx:
        if row[1] == str(s01__):
            S01_ = row[0]
        #    print('S01:', S01_)
            break


########################S11#################################


    r3 = None
    for row_idx, row in enumerate(Multi):
        if row[0] == int(hex_value):
            r3 = row_idx
         #   print('R3: '+str(r3))
            break

    c3 = None
    for col_idx, row in enumerate(Multi):
        if row[0] == 4:
            c3 = col_idx
         #   print('C3:', c3)
            break

    if r3 is not None and c3 is not None:
        xb2 = None
        xb2 = Multi[r3][c3]
     #   print('xb2 '+str(xb2))

    r4 = None
    for row2_idx, row in enumerate(Add):
        if row[0] == int(hex_value4):
            r4 = row2_idx
        #    print('r4:', r4)

            break

    c4 = None
    for col2_idx, row in enumerate(Add):
        if row[0] == xb2:
            c4 = col2_idx
         #   print('c4:', c4)
            break

    if r4 is not None and c4 is not None:
        s11__ = Add[r4][c4]
      #  print('s11__', s11__)

    S11_ = None
    for row in hexx:
        if row[1] == str(s11__):
            S11_ = row[0]
          #  print('S11:', S11_)
            break


# Add Round Key 1
    Mix_coloumn = str(S00_) + str(S10_) + str(S01_) + str(S11_)
#    print('Mix_coloumn:', Mix_coloumn)
    Add_Round_Key1 = None
    Add_Round_Key1 = bin(int(Mix_coloumn, 2) ^ int(key1, 2))[2:].zfill(16)
  #  print('add key:', Add_Round_Key1)
    
    
########################################### STEP3 ##############################################################
########################################### STEP3 ##############################################################
########################################### STEP3 ##############################################################

    part1xx = Add_Round_Key1[:4]
    part2xx = Add_Round_Key1[4:8]
    part3xx = Add_Round_Key1[8:12]
    part4xx = Add_Round_Key1[12:]



    for row in matrix:
        if row[0] == part1xx:
            part1x = row[1]
        if row[0] == part2xx:
            part2x = row[1]
        if row[0] == part3xx:
            part3x = row[1]
        if row[0] == part4xx:
            part4x = row[1]

    shift_left2 = str(part1x) + str(part4x) + str(part3x) + str(part2x)
   # print('shiftleft2:', shift_left2)

    Ciphertext = None
    Ciphertext = bin(int(shift_left2, 2) ^ int(key2, 2))[2:].zfill(16)
    # print('Ciphertext:', Ciphertext)
  

    w0_label.config(text="w0: " + w0)
    w1_label.config(text="w1: " + w1)
    w2_label.config(text="w2: " + w2)
    w3_label.config(text="w3: " + w3)
    w4_label.config(text="w4: " + w4)
    w5_label.config(text="w5: " + w5)
    add_round_key_label.config(text="Add_Round_Key1: " + Add_Round_Key1)
    shift_left1_label.config(text="shift_left1: " + shift_left1)
    Mix_coloumn_label.config(text="Mix_coloumn: " + Mix_coloumn)
    shift_left2_label.config(text="shift_left2: " + shift_left2)
    Ciphertext_label.config(text="Ciphertext: " + Ciphertext)

##############################decryption##########################################################################
##############################decryption##########################################################################
##############################decryption##########################################################################
##############################decryption##########################################################################
##############################decryption##########################################################################
def decryption():

    Ciphertext = Ciphertext_entry.get()
    key_str = key_entry.get()

    if len(key_str) != 16:
        messagebox.showerror(
            "Error", "Key & plaintext must contain exactly 16 digits.")
        return

    key_is_binary = all(bit in "01" for bit in key_str)
    cipher_is_binary = all(bit in "01" for bit in Ciphertext)

    
    if key_is_binary:
        print("Key is binary.")
        
    else:
        messagebox.showerror(
        "Error", "Key must be binary")
     
    if cipher_is_binary:
            print("cipher text is binary.")
        
    else:
        messagebox.showerror(
        "Error", "cipher text  must be binary")
        
    matrix = [
        ["0000", "1001"],
        ["0001", "0100"],
        ["0010", "1010"],
        ["0011", "1011"],
        ["0100", "1101"],
        ["0101", "0001"],
        ["0110", "1000"],
        ["0111", "0101"],
        ["1000", "0110"],
        ["1001", "0010"],
        ["1010", "0000"],
        ["1011", "0011"],
        ["1100", "1100"],
        ["1101", "1110"],
        ["1110", "1111"],
        ["1111", "0111"],
    ]
    Multi = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [2, 4, 6, 8, 10, 12, 14, 3, 1, 7, 5, 11, 9, 15, 13],
        [3, 6, 5, 12, 15, 10, 9, 11, 8, 13, 14, 7, 4, 1, 2],
        [4, 8, 12, 3, 7, 11, 15, 6, 2, 14, 10, 5, 1, 13, 9],
        [5, 10, 15, 7, 2, 13, 8, 14, 11, 4, 1, 9, 12, 3, 6],
        [6, 12, 10, 11, 13, 7, 1, 5, 3, 9, 15, 14, 8, 2, 4],
        [7, 14, 9, 15, 8, 1, 6, 13, 10, 3, 4, 2, 5, 12, 11],
        [8, 3, 11, 6, 14, 5, 13, 12, 4, 15, 7, 10, 2, 9, 1],
        [9, 1, 8, 2, 11, 3, 10, 4, 13, 5, 12, 6, 15, 7, 14],
        [10, 7, 13, 14, 4, 9, 3, 15, 5, 8, 2, 1, 11, 6, 12],
        [11, 5, 14, 10, 1, 15, 4, 7, 12, 2, 9, 13, 6, 8, 3],
        [12, 11, 7, 5, 9, 14, 2, 10, 6, 1, 13, 15, 3, 4, 8],
        [13, 9, 4, 1, 12, 8, 5, 2, 15, 11, 6, 3, 14, 10, 7],
        [14, 15, 1, 13, 3, 2, 12, 9, 7, 6, 8, 4, 10, 11, 5],
        [15, 13, 2, 9, 6, 4, 11, 1, 14, 12, 3, 8, 7, 5, 10],
    ]
    Add = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],
        [2, 3, 0, 1, 6, 7, 4, 5, 10, 11, 8, 9, 14, 15, 12, 13],
        [3, 2, 1, 0, 7, 6, 5, 4, 11, 10, 9, 8, 15, 14, 13, 12],
        [4, 5, 6, 7, 0, 1, 2, 3, 12, 13, 14, 15, 8, 9, 10, 11],
        [5, 4, 7, 6, 1, 0, 3, 2, 13, 12, 15, 14, 9, 8, 11, 10],
        [6, 7, 4, 5, 2, 3, 0, 1, 14, 15, 12, 13, 10, 11, 8, 9],
        [7, 6, 5, 4, 3, 2, 1, 0, 15, 14, 13, 12, 11, 10, 9, 8],
        [8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7],
        [9, 8, 11, 10, 13, 12, 15, 14, 1, 0, 3, 2, 5, 4, 7, 6],
        [10, 11, 8, 9, 14, 15, 12, 13, 2, 3, 0, 1, 6, 7, 4, 5],
        [11, 10, 9, 8, 15, 14, 13, 12, 3, 2, 1, 0, 7, 6, 5, 4],
        [12, 13, 14, 15, 8, 9, 10, 11, 4, 5, 6, 7, 0, 1, 2, 3],
        [13, 12, 15, 14, 9, 8, 11, 10, 5, 4, 7, 6, 1, 0, 3, 2],
        [14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3, 0, 1],
        [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    ]

    hexx = [
        ["0000", "0"],
        ["0001", "1"],
        ["0010", "2"],
        ["0011", "3"],
        ["0100", "4"],
        ["0101", "5"],
        ["0110", "6"],
        ["0111", "7"],
        ["1000", "8"],
        ["1001", "9"],
        ["1010", "10"],
        ["1011", "11"],
        ["1100", "12"],
        ["1101", "13"],
        ["1110", "14"],
        ["1111", "15"],
    ]


    helper_matrix = [
        ["1", "4"],
        ["4", "1"],
    ]
    helper_matrix2 = [
        ["9", "2"],
        ["2", "9"],
    ]    

    w2_helper = "10000000"
    w4_helper = "00110000"
    # calculate w0,w1
    w0 = key_str[:8]
    w1 = key_str[8:]

    # calculate rotnib w1
    w1_left = w1[:4]
    w1_right = w1[4:]
    RotNib = w1_right + w1_left

    # calculate subnib
    RotNib_left = RotNib[:4]
    RotNib_right = RotNib[4:]
    rib_left_value = None
    rib_right_value = None
    for row in matrix:
        if row[0] == RotNib_left:
            rib_left_value = row[1]
        if row[0] == RotNib_right:
            rib_right_value = row[1]
    SubNib = rib_left_value + rib_right_value

    # calculate w2,w3
    help_w2 = bin(int(w0, 2) ^ int(w2_helper, 2))[2:].zfill(8)
    w2 = bin(int(help_w2, 2) ^ int(SubNib, 2))[2:].zfill(8)
    w3 = bin(int(w2, 2) ^ int(w1, 2))[2:].zfill(8)

    # calculate rotnib w3
    w3_left = w3[:4]
    w3_right = w3[4:]
    RotNib2 = w3_right + w3_left

    # calculate subnib2
    RotNib2_left = RotNib2[:4]
    RotNib2_right = RotNib2[4:]
    rib2_left_value = None
    rib2_right_value = None

    for row in matrix:
        if row[0] == RotNib2_left:
            rib2_left_value = row[1]
        if row[0] == RotNib2_right:
            rib2_right_value = row[1]
    SubNib2 = rib2_left_value + rib2_right_value

    # calculate w4,w5
    help_w4 = bin(int(w2, 2) ^ int(w4_helper, 2))[2:].zfill(8)
    w4 = bin(int(help_w4, 2) ^ int(SubNib2, 2))[2:].zfill(8)
    w5 = bin(int(w4, 2) ^ int(w3, 2))[2:].zfill(8)

    # calculate sub-keys
    key0 = w0 + w1
    key1 = w2 + w3
    key2 = w4 + w5

    
    Add_Round_2 = bin(int(Ciphertext, 2) ^ int(key2, 2))[2:].zfill(16)
   # print('Add_Round_2:', Add_Round_2)
    
   
    part1xxx = Add_Round_2[:4]
    part2xxx = Add_Round_2[4:8]
    part3xxx = Add_Round_2[8:12]
    part4xxx = Add_Round_2[12:]

    shift_inverse = str(part1xxx) + str(part4xxx) + str(part3xxx) + str(part2xxx)
   # print('shift_inverse:', shift_inverse)   


    for row in matrix:
        if row[1] == part1xxx:
            part1xr = row[0]
        if row[1] == part2xxx:
            part2xr = row[0]
        if row[1] == part3xxx:
            part3xr = row[0]
        if row[1] == part4xxx:
            part4xr = row[0] 

 
    Inverse_Nibble = str(part1xr) + str(part4xr) + str(part3xr) + str(part2xr)
   # print('Inverse_Nibble:', Inverse_Nibble)   
    
    Add_Round_1_decryption = bin(int(Inverse_Nibble, 2) ^ int(key1, 2))[2:].zfill(16)
   # print('Add_Round_1_decryption:', Add_Round_1_decryption)   

    S00_inv = None
    S11_inv = None
    S01_inv = None
    S10_inv = None
    
    part1xyx = Add_Round_1_decryption[:4]
    part2xyx = Add_Round_1_decryption[4:8]
    part3xyx = Add_Round_1_decryption[8:12]
    part4xyx = Add_Round_1_decryption[12:]

    
    shift_matrixx = [
        [part1xyx, part3xyx],
        [part2xyx, part4xyx],
    ]


    hex_value_enc = None
    for row in hexx:
        if row[0] == shift_matrixx[0][0]:
            hex_value_enc = row[1]
        #    print('hex_value_enc: '+str(hex_value_enc))
            break

    hex_value2_enc = None
    for row in hexx:
        if row[0] == shift_matrixx[0][1]:
            hex_value2_enc = row[1]
         #   print('hex_value2_enc: '+str(hex_value2_enc))

            break

    hex_value3_enc = None
    for row in hexx:
        if row[0] == shift_matrixx[1][0]:
            hex_value3_enc = row[1]
        #    print('hex_value3_enc: '+str(hex_value3_enc))
            break

    hex_value4_enc = None
    for row in hexx:
        if row[0] == shift_matrixx[1][1]:
            hex_value4_enc = row[1]
        #    print('hex_value4_enc: '+str(hex_value4_enc))
            break
    r = None
    for row_idx, row in enumerate(Multi):
        if row[0] == int(hex_value_enc):
            r = row_idx
     #       print('R: '+str(r))
            break

    c = None
    for col_idx, row in enumerate(Multi):
        if row[0] == 9:
            c = col_idx
      #      print('C:', c)
            break

    if r is not None and c is not None:
        xb_enc = None

        xb_enc = Multi[r][c]
      #  print('xb_encr '+str(xb_enc))

    rr = None
    for row_idx, row in enumerate(Multi):
        if row[0] == int(hex_value3_enc):
            rr = row_idx
     #       print('RR: '+str(rr))
            break

    cc = None
    for col_idx, row in enumerate(Multi):
        if row[0] == 2:
            cc = col_idx
      #      print('CC:', cc)
            break

    if rr is not None and cc is not None:
        xb_encc = None
        xb_encc = Multi[rr][cc]
    #    print('xb_encc '+str(xb_encc))


    r2 = None
    for row2_idx, row in enumerate(Add):
        if row[0] == xb_enc:
            r2 = row2_idx
    #        print('r2:', r2)

            break

    c2 = None
    for col2_idx, row in enumerate(Add):
        if row[0] == xb_encc:
            c2 = col2_idx
    #        print('c2:', c2)
#
            break

    if r2 is not None and c2 is not None:
        xxx= None
        xxx = Add[r2][c2]
    #    print('xxx:', xxx)

    S00_inv = None
    for row in hexx:
        if row[1] == str(xxx):
            S00_inv = row[0]
     #       print('S00_inv:', str(S00_inv))
            break




    r = None
    for row_idx, row in enumerate(Multi):
        if row[0] == int(hex_value_enc):
            r = row_idx
     #       print('R: '+str(r))
            break

    c = None
    for col_idx, row in enumerate(Multi):
        if row[0] == 2:
            c = col_idx
     #       print('C:', c)
            break

    if r is not None and c is not None:
        xb_enc = None

        xb_enc = Multi[r][c]
   #     print('xb_encr '+str(xb_enc))

    rr = None
    for row_idx, row in enumerate(Multi):
        if row[0] == int(hex_value3_enc):
            rr = row_idx
     #       print('RR: '+str(rr))
            break

    cc = None
    for col_idx, row in enumerate(Multi):
        if row[0] == 9:
            cc = col_idx
     #       print('CC:', cc)
            break

    if rr is not None and cc is not None:
        xb_encc = None
        xb_encc = Multi[rr][cc]
       # print('xb_encc '+str(xb_encc))


    r2 = None
    for row2_idx, row in enumerate(Add):
        if row[0] == xb_enc:
            r2 = row2_idx
           # print('r2:', r2)

            break

    c2 = None
    for col2_idx, row in enumerate(Add):
        if row[0] == xb_encc:
            c2 = col2_idx
          #  print('c2:', c2)

            break

    if r2 is not None and c2 is not None:
        xxx= None
        xxx = Add[r2][c2]
     #   print('xxx:', xxx)

    S10_inv = None
    for row in hexx:
        if row[1] == str(xxx):
            S10_inv = row[0]
         #   print('S10_inv:', str(S10_inv))
            break


    r = None
    for row_idx, row in enumerate(Multi):
        if row[0] == int(hex_value2_enc):
            r = row_idx
        #    print('R: '+str(r))
            break

    c = None
    for col_idx, row in enumerate(Multi):
        if row[0] == 9:
            c = col_idx
          #  print('C:', c)
            break

    if r is not None and c is not None:
        xb_enc = None

        xb_enc = Multi[r][c]
       # print('xb_encr '+str(xb_enc))

    rr = None
    for row_idx, row in enumerate(Multi):
        if row[0] == int(hex_value4_enc):
            rr = row_idx
        #    print('RR: '+str(rr))
            break

    cc = None
    for col_idx, row in enumerate(Multi):
        if row[0] == 2:
            cc = col_idx
        #    print('CC:', cc)
            break

    if rr is not None and cc is not None:
        xb_encc = None
        xb_encc = Multi[rr][cc]
      #  print('xb_encc '+str(xb_encc))


    r2 = None
    for row2_idx, row in enumerate(Add):
        if row[0] == xb_enc:
            r2 = row2_idx
        #    print('r2:', r2)

            break

    c2 = None
    for col2_idx, row in enumerate(Add):
        if row[0] == xb_encc:
            c2 = col2_idx
          #  print('c2:', c2)

            break

    if r2 is not None and c2 is not None:
        xxx= None
        xxx = Add[r2][c2]
       # print('xxx:', xxx)

    S01_inv = None
    for row in hexx:
        if row[1] == str(xxx):
            S01_inv = row[0]
       #     print('S01_inv:', str(S01_inv))
            break




    r = None
    for row_idx, row in enumerate(Multi):
        if row[0] == int(hex_value2_enc):
            r = row_idx
       #     print('R: '+str(r))
            break

    c = None
    for col_idx, row in enumerate(Multi):
        if row[0] == 2:
            c = col_idx
        #    print('C:', c)
            break

    if r is not None and c is not None:
        xb_enc = None

        xb_enc = Multi[r][c]
     #   print('xb_encr '+str(xb_enc))

    rr = None
    for row_idx, row in enumerate(Multi):
        if row[0] == int(hex_value4_enc):
            rr = row_idx
      #      print('RR: '+str(rr))
            break

    cc = None
    for col_idx, row in enumerate(Multi):
        if row[0] == 9:
            cc = col_idx
        #    print('CC:', cc)
            break

    if rr is not None and cc is not None:
        xb_encc = None
        xb_encc = Multi[rr][cc]
     #   print('xb_encc '+str(xb_encc))


    r2 = None
    for row2_idx, row in enumerate(Add):
        if row[0] == xb_enc:
            r2 = row2_idx
      #      print('r2:', r2)

            break

    c2 = None
    for col2_idx, row in enumerate(Add):
        if row[0] == xb_encc:
            c2 = col2_idx
       #     print('c2:', c2)

            break

    if r2 is not None and c2 is not None:
        xxx= None
        xxx = Add[r2][c2]
      #  print('xxx:', xxx)

    S11_inv = None
    for row in hexx:
        if row[1] == str(xxx):
            S11_inv = row[0]
        #    print('S11_inv:', str(S11_inv))
            break

    mix_coloumn_enc = str(S00_inv) + str(S10_inv) + str(S01_inv) + str(S11_inv)
   # print('mix_coloumn_enc:', str(mix_coloumn_enc))
    shift_enc = str(S00_inv) + str(S11_inv) + str(S01_inv) + str(S10_inv)
  #  print('shift_enc:', str(shift_enc))

    A =None
    B =None
    C =None
    D =None
    for row in matrix:
        if row[1] == S00_inv:
            A = row[0]
        if row[1] == S11_inv:
            B = row[0]
        if row[1] == S01_inv:
            C = row[0]
        if row[1] == S10_inv:
            D = row[0]

    Inverse_NIBBLE_ENC = str(A) + str(B) + str(C) + str(D)
   # print('Inverse_NIBBLE_ENC:', str(Inverse_NIBBLE_ENC))
    
    
    plaintext_enc = bin(int(Inverse_NIBBLE_ENC, 2) ^ int(key0, 2))[2:].zfill(16)
    #print('plaintext_enc:', str(plaintext_enc))
    
    Add_Round_2_label.config(text="Add_Round_2: " + Add_Round_2)
    shift_inverse_label.config(text="shift_inverse: " + shift_inverse)
    Inverse_Nibble_label.config(text="Inverse_Nibble: " + Inverse_Nibble)
    Add_Round_1_decryption_label.config(text="Add_Round_1_decryption: " + Add_Round_1_decryption)
    mix_coloumn_enc_label.config(text="mix_coloumn_enc: " + mix_coloumn_enc)
    shift_enc_label.config(text="shift_enc: " + shift_enc)
    Inverse_NIBBLE_ENC_label.config(text=":Inverse_NIBBLE_ENC " + Inverse_NIBBLE_ENC)
    plaintext_enc_label.config(text="plaintext: " + plaintext_enc)

################################# GUI############################################
################################# GUI############################################
################################# GUI############################################
################################# GUI############################################



root = tk.Tk()
root.title("AES Encryption & decryption Calculator")

plaintext_label = tk.Label(root, text="Enter the plaintext (16 digits):")
plaintext_entry = tk.Entry(root)
key_label = tk.Label(root, text="Enter the key (16 digits):")
key_entry = tk.Entry(root)
Ciphertext_label2 = tk.Label(root, text="Enter the cipher (16 digits):")
Ciphertext_entry = tk.Entry(root)

calculate_button = tk.Button(root, text="Encryption", command=Encryption)
calculate_button2 = tk.Button(root, text="decryption", command=decryption)


w0_label = tk.Label(root, text="w0:")
w1_label = tk.Label(root, text="w1:")
w2_label = tk.Label(root, text="w2:")
w3_label = tk.Label(root, text="w3:")
w4_label = tk.Label(root, text="w4:")
w5_label = tk.Label(root, text="w5:")
add_round_key_label = tk.Label(root, text="Add_Round_Key1:")
shift_left1_label = tk.Label(root, text="shift_left1:")
Mix_coloumn_label = tk.Label(root, text="Mix_coloumn:")
add_round_key_label2 = tk.Label(root, text="Add_Round_Key2:")
shift_left2_label = tk.Label(root, text="shift_left2:")
Ciphertext_label = tk.Label(root, text="Ciphertext:")
Ciphertext_label = tk.Label(root, text="Ciphertext:")
Add_Round_2_label = tk.Label(root, text="Add_Round_2:")
shift_inverse_label = tk.Label(root, text="shift_inverse:")
Inverse_Nibble_label = tk.Label(root, text="Inverse_Nibble:")
Add_Round_1_decryption_label = tk.Label(root, text="Add_Round_1_decryption:")
mix_coloumn_enc_label = tk.Label(root, text="mix_coloumn_enc:")
shift_enc_label = tk.Label(root, text="shift_enc:")
Inverse_NIBBLE_ENC_label = tk.Label(root, text="Inverse_NIBBLE_ENC:")
plaintext_enc_label = tk.Label(root, text="plaintext_enc:")

plaintext_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
plaintext_entry.grid(row=0, column=1, padx=20, pady=5)
key_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
key_entry.grid(row=1, column=1, padx=20, pady=5)
Ciphertext_label2.grid(row=2, column=0, padx=10, pady=5, sticky="w")
Ciphertext_entry.grid(row=2, column=1, padx=20, pady=5)
calculate_button.grid(row=15, columnspan=2, padx=10, pady=10)
calculate_button2.grid(row=16, columnspan=5, padx=10, pady=10)

w0_label.grid(row=3, columnspan=2, padx=10, pady=5, sticky="w")
w1_label.grid(row=4, columnspan=2, padx=10, pady=5, sticky="w")
w2_label.grid(row=5, columnspan=2, padx=10, pady=5, sticky="w")
w3_label.grid(row=6, columnspan=2, padx=10, pady=5, sticky="w")
w4_label.grid(row=7, columnspan=2, padx=10, pady=5, sticky="w")
w5_label.grid(row=8, columnspan=2, padx=10, pady=5, sticky="w")
shift_left1_label.grid(row=10, columnspan=2, padx=10, pady=5, sticky="w")
Mix_coloumn_label.grid(row=11, columnspan=2, padx=10, pady=5, sticky="w")
shift_left2_label.grid(row=13, columnspan=2, padx=10, pady=5, sticky="w")
Ciphertext_label.grid(row=14, columnspan=2, padx=10, pady=5, sticky="w")
Add_Round_2_label.grid(row=3, columnspan=2, padx=250, pady=5, sticky="w")
shift_inverse_label.grid(row=4, columnspan=2, padx=250, pady=5, sticky="w")
mix_coloumn_enc_label.grid(row=5, columnspan=2, padx=250, pady=5, sticky="w")
shift_enc_label.grid(row=6, columnspan=2, padx=250, pady=5, sticky="w")
Inverse_NIBBLE_ENC_label.grid(row=7, columnspan=2, padx=250, pady=5, sticky="w")
plaintext_enc_label.grid(row=8, columnspan=2, padx=250, pady=5, sticky="w")

root.mainloop()
