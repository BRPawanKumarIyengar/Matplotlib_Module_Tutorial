#This is most basic and simplesr use of matplotlib

#W import matplotlib as my_plt for easy reference
from matplotlib import pyplot as my_plt


#To enhace the look of our graph we use style 
from matplotlib import style

#Here we are manually feeding data for x and Y and legend as " plot 1", width of line as 5 and color as red (shown by 'r')
my_plt.plot([1,2,3,4,5],[1,3,5,7,9],'r', label = 'plot 1',linewidth = 5)

#We can also pass in variables and items from dataframe into graph
X_Variable = [1,2,3,4,5]
Y_Variable = [9,7,5,3,1]

#We here plot another line 
my_plt.plot(X_Variable,Y_Variable,'c', label = 'plot 2',linewidth = 5)

#Here we add lables (that tell us what are values of X and Y ) to x and y axis
my_plt.xlabel('X - Axis')
my_plt.ylabel('Y - Axis')

#Here we add the title of the graph (Tells us what to do)
my_plt.title('Title of Graph')

#We put in a grid of green color
my_plt.grid(color = 'g')

#We input the legend to be shown
my_plt.legend()

my_plt.show()


  

