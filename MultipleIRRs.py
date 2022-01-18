#importing libraries
import pandas as pd
import numpy as np
import numpy_financial as npf
from matplotlib import pyplot as plt

# Cashflows input
cf=[-10000,11000,12000,43000,-80000,15000,16000,17000,-88000,19000,40000]

# itterating npv calcualtion
d=[]
is_negative = False
lst_irr = []
for r in np.arange(-0.1, 1.1, 0.001):
    npv = npf.npv(r, cf)

    # Checking if the discount rate switches from pos to neg, indiciating IRR.
    if npv < 0 and not is_negative:
        # Positive -> Negative
        is_negative = True
        lst_irr.append(r)
    elif npv > 0 and is_negative:
        # Negative -> Positive
        lst_irr.append(r)
        is_negative = False
    d.append(
        {
            'rate': r,
            'npv': npv
        }
    )
print(f"All the IRRs have been found: {lst_irr}")
#setup dataframe
df=pd.DataFrame(d, columns=["rate","npv"])

#plot
plt.plot(df["rate"],df["npv"])
#Hline @NPV=0
plt.axline((-0.1,0), (1.0,0),linestyle="-",lw=2,color="black")
plt.vlines(lst_irr,max(df["npv"]),min(df["npv"]),linestyle="--",lw=0.5,color="black")
plt.title("Multiple IRR Calculator")
plt.xlabel("Discount Rate")
plt.ylabel("NPV")
plt.show()

