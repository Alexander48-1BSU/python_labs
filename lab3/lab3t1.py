import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    dataset = sm.datasets.anes96.load_pandas()
    df = dataset.data
    colors= ["#33539E", "#A5678E"]
    sns.set_palette(sns.color_palette(colors))


    xaxis='TVnews' #same as factor
    yaxis='age'
    target_class='vote'
    
    #print(df)
    unique_classes=sorted(df['vote'].unique())
    plt.figure(figsize=(6, 5))
    for i in unique_classes:
        part=df[df[target_class]==i]
        plt.scatter(
            x=part[xaxis], 
            y=part[yaxis],
            s=25,
            label=f'{i}'
        )
    
    plt.title('anes96 "TVnews vs Age" scatter plot', fontsize=20)
    plt.xlabel(xaxis, fontsize=15)
    plt.ylabel(yaxis, fontsize=15)
    
    plt.legend(title='Vote value', bbox_to_anchor=(0.26, 0.8))
    plt.grid(True, linestyle='-', alpha=0.5)

    
    plt.show()

main()
    
