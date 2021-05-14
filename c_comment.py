#CS320 HW3 Question 1 // Shang Chun,Lin
#following the structure of the dfa2 provided in the lab
#The situation that the first '*/' followed by some digits are not allowed!!

def c_comment(str):
    dfa_state = 0
    if_end = 0

    for i in range(len(str)):
        digit = str[i]
         
        if dfa_state == 0:
            if digit == '/':
                dfa_state = 1
            else:
                break

        elif dfa_state == 1:
            if digit == '*':
                dfa_state = 2
            else:
                break

        elif dfa_state == 2:
            if digit == '*':
                dfa_state = 3
            else:
                dfa_state = 2

        elif dfa_state == 3:
            if digit == '/':
                dfa_state = 4
                if_end = 1
            elif digit == '*':
                dfa_state = 3
            else:
                dfa_state = 2

        elif dfa_state == 4:
            if_end = 0
    
    if dfa_state == 4 and if_end == 1:
        print(str,True)
    else:
        print(str,False)
                
if __name__ == "__main__":
    c_comment('/**/')
    c_comment('/***/')
    c_comment('/**/*/')
    c_comment('/*2348dfdg*/')
    c_comment('/*23/*48dfdg*/')
    c_comment('/*23*/48dfdg*/')
    c_comment('*/ccc*/ddd*/')
    c_comment('/*fdg*/*')
    c_comment('/*fdg/')
    c_comment('/*/*fdg*/*/')
    c_comment('//**/')
