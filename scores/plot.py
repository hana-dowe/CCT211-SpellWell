import src.constants as const
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class Plot():
    def __init__(self):
        self.plots = plots
         
    def listDictScores(whichDict):
        whichDict_score_name = []
        whichDict_score_value = []
        with open('past_scores.csv', 'r', newline='') as file:
            score_list = list(csv.reader(file))
            for row in score_list:
                if row[0] == whichDict:
                    whichDict_score_name.append(row[0])
                    whichDict_score_value.append(row[1])
        return whichDict_score_name, whichDict_score_value

    def plotScores(dictName):
        obj = Plot.listDictScores(dictName)
        pltname = obj[0]
        pltvalue = obj[1]
        pltvalue = [int(i) for i in pltvalue]
        pltvalue.reverse()
        
        plt.plot(range(1, (len(pltname) + 1)), pltvalue, 'm*-.')
        plt.axis([1, 10, 0, 800])
        for i, txt in enumerate(pltvalue):
                plt.annotate(txt, ((range(1, (len(pltname) + 1)))[i], pltvalue[i]))  
        plt.ylabel('Score')
        plt.xlabel('Past Games')
        plt.savefig('\\Users\\aotis\\Desktop\\newnew\\CCT211-SpellWell-main\\scores\\graphs\\{}.png'.format(dictName))       

    def savePresetPlots():
        dictNames = const.Db.getDictNames(True)
        for name in dictNames:
            Plot.plotScores(name)
        
    def saveCustomPlots():
        dictNames = const.Db.getDictNames(False)
        for name in dictNames:
            Plot.plotScores(name)
        
Plot.savePresetPlots()
Plot.saveCustomPlots()