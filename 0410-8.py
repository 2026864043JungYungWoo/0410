def input_c() :
    c = float(input("섭씨 온도를 입력하시오: "))
    return c
def main() :
    while True:
        index = menu()
        if index == 1 :
            t = input_c()
            t2 = ctof(t)
            print("화씨 온도 = ", t2, "\n")
        elif index == 2 :
            t = input_f()
            t2 = ftoc(t)
            print("섭씨 온도 = ", t2, "\n")
        else :
            break
main()