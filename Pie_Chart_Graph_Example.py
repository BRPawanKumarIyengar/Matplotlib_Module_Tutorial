#This sample plots a pie graph

#We create an array of the types of work perfomed by us
work = ['python','Java','C++','C','VB','PHP','Perl','Ruby']

#we create an array of amount of preference of each type of work
Amount =[120,60,40,40,30,30,20,20]

#We create an array of colors so that we can give each language a color of our choice
Pie_Colors = ['g','r','orange','violet','yellow','c','b' ,'brown']

#We import pyplot from matplotlib with alias my_plt
from matplotlib import pyplot as my_plt

#We now create a pie chart with all the information put in
my_plt.pie(Amount, labels = work,colors = Pie_Colors,startangle = 90,shadow = False,explode =(0.1,0,0,0,0,0,0,0),autopct='%1.1f%%')
#startangle = 90 means start the first slice at 90 and proceed counter clockwise
#shadow = False means we do not want the pie chart to display a shadow
#Explode options lets us pull out (and thus highlight) a part of chart; Here we are pulling out first slice (only that is 0.1)
#autopuct takes in a predefined input "%1.1f%%' and gives out the percentage of each slice (calculatd automatically)


#We give a titlde to the chart 
my_plt.title('This is the best Pie Chart on Earth')

#The created Pie Chart is displayed
my_plt.show()


  

