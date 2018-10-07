#This is most basic and simplesr ,use of matplotlib

#W import matplotlib as my_plt for easy reference
from matplotlib import pyplot as my_plt

#Here we are manually feeding data for x and Y a
#my_plt.plot([1,2,3,4,5],[1,3,5,7,9],)


#Here we add lables (that tell us what are values of X and Y ) to x and y axis
my_plt.xlabel('X - Axis')
my_plt.ylabel('Y - Axis')

#Here we add the title of the graph (Tells us what to do)
my_plt.title('Title of Graph')

#Here we plot a scatterplot graph
my_plt.scatter([1,2,3,4,5,6,7,8,9],[1,3,5,7,9,7,5,3,1])

my_plt.show()


  

