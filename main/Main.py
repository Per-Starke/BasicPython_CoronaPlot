"""Run this little main to see some badass plots!"""
from visualization.plot import *

question = """What plot do you want to see? Type in the corresponding number and hit return, then wait
until the plot shows up!
'1' for 'Total incidence',
'2' for 'Incidence per age group',
'3' for 'Incidence per sex',
'4' for 'Incidence per state'\n"""


val = input(question)

repeat = True

while repeat:
    if val == "1":
        plot_incidence_total()
        repeat = False
    elif val == "2":
        plot_incidence_var_age()
        repeat = False
    elif val == "3":
        plot_incidence_var_sex()
        repeat = False
    elif val == "4":
        plot_incidence_var_state()
        repeat = False
    else:
        print("No valid input! ")
        val = input(question)

plt.show()







