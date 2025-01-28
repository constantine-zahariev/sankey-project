import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

# Set plot size and font
plt.rcParams["figure.figsize"] = (15, 7)
plt.rcParams["font.family"] = 'Jost'
plt.rcParams["font.size"] = '10.5'

fig = plt.figure()  # Create a figure object

# add_subplot is a method that acts on the fig object
# Call pattern: add_subplot(nrows, ncols, index, **kwargs)
# Subplots can include multiple rows and columns
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                     title="Natural Gas Flows in the UK 2023 (TWh)")

# Create Sankey object
# It needs the 'ax' argument to work, which is why we need the add_subplot method
sankey = Sankey(ax=ax, unit=None, gap=0.45, scale=1.2, offset=0.3, shoulder=0.03, head_angle=130)
# offset = label separation from arrow
# gap = distance between arrow branches
# scale = overall thickness of diagram
# shoulder = length of arrow shoulder
# ax = specify axes on which the Sankey object is used

# Data source: https://www.gov.uk/government/statistics/digest-of-uk-energy-statistics-dukes-2024
# Chapter 4: Natural Gas

# Input flows
input_flows = [0.007570, -0.007570, 0.432381, 0.559146, 0.008474, -0.531804, -0.232403, -0.029827, -0.198396]

# Sankey for input Production and Import flows
sankey.add(flows=input_flows,
           labels=[" ", " ", "Production \n382.7 TWh", "Imports \n494.9 TWh", "Biomethane\nInjection\n7.5 TWh",
                   " ", "Power \nStations \n205.7 TWh", "Other \nTransformations \n26.4 TWh",
                   "Exports \n175.6 TWh"],
           orientations=[1, 1, 1, 0, -1, 0, 1, -1, -1],
           facecolor="#669BBC", # 29335C
           trunklength=1.5)

# Natural Gas Stock flows
nat_gas_stock_flows = [0.007570, -0.007570]

# Sankey for Natural Gas Stocks
sankey.add(flows=nat_gas_stock_flows,
           orientations=[1, 1],
           prior=0,
           connect=(0, 1),
           facecolor="orange",
           trunklength=1.5)

# Flows for end use branches
end_use_flows = [0.531804, -0.005875, -0.092758, -0.100554, -0.001130, -0.267879, -0.000339, -0.063270]

# Sankey for final use categories
sankey.add(flows=end_use_flows,
           labels=[" ", "Iron & \nSteel \n5.2 TWh", "Other \nIndustry \n82.1 TWh",
                   "Other \nFinal \nCustomers \n89.0 TWh", "Transport \n1.0 TWh",
                   "Domestic \n237.1", "Synthetic\ncoke oven\nfuel\n0.3 TWh",
                   "Losses & \nother use \n56 TWh"],
           orientations=[0, 1, 1, 1, -1, 0, -1, -1],
           prior=0,
           connect=(5, 0),
           facecolor="#A8C686", # F3A712
           trunklength=1.5)

ax.text(-0.01, 1.20, "Natural Gas Stock 6.7 TWh", fontfamily="Jost",
        horizontalalignment="center")

sankey.finish()
plt.axis('off') # Turn off figure border
plt.savefig("natural-gas-sankey-2023.png", dpi=800, transparent=False)
plt.show()
