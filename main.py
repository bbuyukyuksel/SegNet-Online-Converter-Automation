from getSegnetDemo import getSegnetDemo
import os

sourcesPATH = "sources/"
resultsPATH = 'results/'

if __name__ == '__main__':

    listdir = []
    try:
        listdir = os.listdir(sourcesPATH)
    except:
        os.mkdir(sourcesPATH)
    finally:
        listdir = os.listdir(sourcesPATH)

    for file in listdir:
        mySegnet = getSegnetDemo(filename=sourcesPATH + file, url='URL ile Besle', log=True)
        mySegnet.start()
        mySegnet.getBase64Image()
        mySegnet.saveBase64Image(resultsPATH)
        print('\n')
        del mySegnet











