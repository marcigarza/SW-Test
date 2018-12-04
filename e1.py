import sys
#Since we only considerate 3 cases (1 or even length or odd length), is more efficient to avoid conditionals inside the while
#loop, so we to treat each case differently

def valencia(x):
    odd = 0
    even = 0
    res = len(str(x)) 
    if not res%2:
        while x != 0:
            even += x%10
            x /= 10
            odd += x%10
            x /= 10
    elif res is 1:
        return x
    else:
        i = 0
        while i < res - 1:
            even += x%10
            x /= 10
            odd += x%10
            x /= 10
            i += 1
        even += x%10
    return odd - even

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Insert at least one integer as a parameter")
        sys.exit(-1)
    
    max_val = valencia(int(sys.argv[1]))
    if max_val == 0:
        print sys.argv[1]
        exit(0)
    size = len(sys.argv)
    i = 2
    while i < size:
        res =  valencia(int(sys.argv[i])) 
        if res  == 0:
            print sys.argv[i]
            sys.exit(0)
        elif res > max_val:
            max_val = res
        i += 1  
    print max_val
    sys.exit(0)

