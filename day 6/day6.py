from collections import Counter
with open("day6.in", 'r') as file:
    data = file.read()

def packetCheck(arr):
    counter = 0
    for i in data:
        firstindex = data[counter]
        checkstring = firstindex+data[counter+1]+data[counter+2]+data[counter+3]+data[counter+4]+data[counter+5]+data[counter+6]+data[counter+7]+data[counter+8]+data[counter+9]+data[counter+10]+data[counter+11]+data[counter+12]+data[counter+13]
        if Unique(checkstring):
            break
        counter += 1
    print(counter+14)

def Unique(string):
    freq = Counter(string)
    if(len(freq) == len(string)):
        return True
    else:
        return False

if __name__ == "__main__":
    packetCheck(data)
