def plot_pie_chart ():
    
    import matplotlib.pyplot as plt
    
    ##Data to plot (Office)
    labels = ['Cooling', 'Lighting', 'Ventilation', 'Lift and Escalator', 'Others']
    data = [60,15,10,10,5]
    colors = ['lightblue', 'lightcoral', 'yellowgreen', 'orchid', 'gold']
    explode = [0.1, 0, 0, 0, 0]
    
    plt.pie(data, explode=explode, colors=colors, autopct='%1.1f%%', shadow=False, startangle=240)
    
    plt.axis('equal')
    plt.legend(labels, loc='best')
    plt.title('Office')
    plt.savefig('C:\\Users\\zhonglin.chiam\\Desktop\\office_elect_cons.png', dpi = 1000)
    plt.close()
    
    ##Data to plot (Office)
    labels = ['Cooling', 'Refrigerator', 'Lighting', 'AV equipment', 'Water heater', 'Washing', 'Kitchen Appl', 'Fans', 'Others']
    data = [30,17,10,10,9,6,6,4,8]
    colors = ['lightblue', 'dodgerblue', 'lightcoral', 'yellowgreen', 'orchid', 'olive', 'grey', 'salmon', 'gold']
    explode = [0.1, 0, 0, 0, 0, 0, 0, 0, 0]
    
    plt.pie(data, explode=explode, colors=colors, autopct='%1.1f%%', shadow=False, startangle=240)
    
    plt.axis('equal')
    plt.legend(labels, loc='best')
    plt.title('Residential')
    plt.savefig('C:\\Users\\zhonglin.chiam\\Desktop\\home_elect_cons.png', dpi = 1000)
    return

############################################################################################################################################################

##Running the script
if __name__ == '__main__':
    plot_pie_chart ()