import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

def plot_weights(df):
    import numpy as np
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize =(2, 9))

    bottom = 0
    labels = []

    for i in range(0,len(df["sample_weight"]),1):
        plt.bar("weights", df["sample_weight"][i], bottom=bottom)
        bottom += df["sample_weight"][i]
        labels.append(df.index[i])

    ax.set_ylabel('Sample weights')
    ax.legend(labels=labels)

    font = {'family' : 'arial',
            'weight' : 'normal',
            'size'   : 20}

    plt.rc('font', **font)

    # define plot name
    # datetime object containing current date and time
    now = datetime.now()
    
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
    
    plt.savefig('.\plots\weights_' + dt_string + '.svg')
    plt.show()

def plot_alpha(alpha, error):
    alpha_list = []
    error_list = []

    for e in np.linspace(0, 1.0, num=100):
        alpha_n = 1/2 * np.log((1-e)/e)
        error_list.append(e)
        alpha_list.append(alpha_n)

    font = {'family' : 'arial',
            'weight' : 'normal',
            'size'   : 15}

    plt.rc('font', **font)

    plt.plot(error_list, alpha_list, color='black')
    plt.plot(np.linspace(error, error, num=100), alpha_list, color='red')
    plt.plot(np.linspace(0, 1.0, num=100), np.linspace(alpha, alpha, num=100), color='red')

    plt.ylabel('Alpha / Amount of say')
    plt.xlabel('Error')
    plt.title(f'Alpha(Error={error})={round(alpha,3)}')
    # define plot name
    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")

    plt.savefig(r'.\plots\alpha_' + dt_string + '.svg')
    plt.show()