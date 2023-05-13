input_str = input("文字列を入力してください：")

def loop(str):
    if (str):
        i = 1
        while(True):
            print(i)
            i = i + i
    else:
        return

loop(input_str)