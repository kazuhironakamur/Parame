def lets_take_tea_break(m, e, n, c):
    if pow(m, e) % n == c: return str(m)
    return ""

if __name__ == "__main__":
    import sys
    
    # for x in range(1, 90000):
    #    if(lets_take_tea_break(*[int(i) for i in (x, 17, 3569, 915)]) != ""):
    #        print(x)

    print("http://cp1.nintendo.co.jp/" +
       lets_take_tea_break(*[int(i) for i in (sys.argv[1], 17, 3569, 915)]))