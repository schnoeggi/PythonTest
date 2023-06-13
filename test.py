globalValue = "Hello World"

def getHello():
    b = "Hello"
    return b

def main():
    print(getHello())
    
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()
