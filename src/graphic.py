import matplotlib.pyplot as plt

def bar(x:list[str] = [1,2,3], y:list[int]= [3,2,1]):
    fig, ax = plt.subplots()
    ax.bar(x, y)
    plt.show()
