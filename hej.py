import numpy as np
def main():
    
    print(root(6))
    print(3/2)
    print(cumsum(root(8)))


def fibbonachi(number):
    if number <= 1:
        return number
    else:
        return fibbonachi(number - 1) + fibbonachi(number - 2)
    
    
def root(number):
    return number**0.5, number**0.25

    
    

def cumsum(iterable):
    result = []
    total = 0
    for value in iterable:
        total += value
        result.append(total)
    return result


if __name__ == '__main__':
    main()


