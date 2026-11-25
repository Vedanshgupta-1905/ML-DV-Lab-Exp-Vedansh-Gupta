import matplotlib.pyplot as plt
import numpy as np
cols=["Quantity","UnitPrice","Sales","Profit"]
corr=dataset[cols].corr()
fig,ax=plt.subplots()
im=ax.imshow(corr,vmin=-1,vmax=1,cmap="coolwarm")
ax.set_xticks(range(len(cols)),cols,rotation=45)
ax.set_yticks(range(len(cols)),cols)
for i in range(len(cols)):
    for j in range(len(cols)):
        ax.text(j,i,f"{corr.iloc[i,j]:.2f}",ha="center",va="center")
fig.colorbar(im)
plt.tight_layout()
plt.show()
