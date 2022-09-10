
def convert_number():
    file = open("numeros.txt")
    data = file.readlines()
    file.close()
    numbers=[]
    for line in data:
        numbers.append(int(line.replace("\\n","")))
    return numbers

def sum(*args):
    s = 0
    for n in args: s += n
    s = int(str(s)[0:10])
    return s


print(sum(*convert_number()))
