import PySimpleGUI as sg
import random as rand
import matplotlib.pyplot as plt
import seaborn as sns

sg.theme("DarkGrey")

layout = [[sg.Text("Create Some Dot Paper Samples")],
	[sg.Text("How many Samples?")],
	[sg.Input(key = "Samples")],
	[sg.Text("How many Dots for those samples?")],
	[sg.Input(key = "Dots")],
	[sg.Text("")],
	[sg.Text("Save Location:")],
	[sg.FolderBrowse(key = 'folder'),sg.Input(key = "folderLoc",change_submits=True)],
	[sg.Button("Generate Samples", key = "Status")],
	[sg.Button("Quit",key = "Quit",)],
	[sg.Text("                                                        ",key= "Done")],]

window = sg.Window("Create Samples",layout)

'''
def makePlot(int number of samples, int number of dots,loc file location)
Makes a random plot of the sample space with no two squares touching eachother
'''
def makePlot(numOfSamples=1,numOfDots=1,fileLoc = ""):
	for i in range(numOfSamples):
		paper = [[0 for i in range(15)] for j in range(10)] 
		locRec = []
		used = 1
		paper[0][0] = 1
		while used <= numOfDots:
			loc = (rand.randint(0,8),rand.randint(0,13))
			print(loc)
			locRec.append(loc)
			x,y = loc
			if paper[x][y]!=1 and paper[x-1][y]!=1 and paper[x+1][y]!=1 and paper[x][y-1]!=1 and paper[x][y+1]!=1:
				paper[x][y]=1
			elif used == 75:
				print("Too many dots")
				break
			else:
				continue
			used = 1 + used
		paper[9][14] = 1
		for row in paper:
			print(row)
		sns.heatmap(paper,vmin = 0, vmax =1,cmap = "Greys",cbar =False,square =True,xticklabels="",yticklabels="")
		print(fileLoc)
		plt.savefig(fileLoc+"Sample"+str(i+1)+".png")


while True:
	event,values = window.Read()
	if event == sg.WINDOW_CLOSED or event == "Quit":
		break
	elif event == "Status":
		stat = "Generated"
		
		try:
			makePlot(int(values['Samples']),int(values['Dots']),str(values['folder'])+"/")
			window['Done'].update(stat)
			window.refresh()
		except Exception as e:
			stat = "Error saving or generating or invalid fields:" 
			window['Done'].update(stat)
			window.refresh()

window.close()
