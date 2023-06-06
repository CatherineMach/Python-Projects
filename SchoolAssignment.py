
import os




def writeData():
    data = '\nHi there!'
    with open('Text.txt','a') as f:
        f.write(data)
        f.close()


def openFile():
    with open('Text.txt','r') as f:
        data = f.read()
        print(data)
        f.close()
    




if __name__ == "__main__":
    writeData()
    openFile()
