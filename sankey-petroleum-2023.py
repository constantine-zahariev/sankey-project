import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

# Set figure size and font
plt.rcParams["figure.figsize"] = (18, 10)
plt.rcParams["font.family"] = 'Jost'
plt.rcParams["font.size"] = '10'

fig = plt.figure()  # Create a figure object

# add_subplot is a method that acts on the fig object
# Call pattern: add_subplot(nrows, ncols, index, **kwargs)
# Subplots can include multiple rows and columns
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[], title="Petroleum Flows in the UK 2023")

# Create Sankey object
sankey = Sankey(ax=ax, unit=None, gap=0.45, scale=2, offset=0.3, shoulder=0.03, head_angle=130)
# offset = label separation from arrow
# gap = distance between arrow branches
# scale = overall thickness of diagram
# shoulder = length of arrow shoulder
# ax = specify axes on which the Sankey object is used

# Data source: https://www.gov.uk/government/statistics/digest-of-uk-energy-statistics-dukes-2024
# Chapter 3: Oil and Oil Products

oil_gas_production_flows = [0.304467, -0.231541, -0.072926]

# Oil & Gas Production, Direct Exports & Flow Into Refineries
sankey.add(flows=oil_gas_production_flows,
           labels=["Crude Oil \n & Gas \nProduction \n33.4 Mt",
                   "Crude Oil \n & Natural \nGas \nExports \n25.4 Mt",
                   "8.0 Mt"],
           orientations=[0, 1, 0],
           facecolor="#0F5257")


refineries_input_flows_old = [0.007293, -0.007293, 0.072926, 0.381951, 0.036463, -0.49134]
refineries_input_flows = [0.007293, -0.007293, 0.072926, 0.381951, 0.036463, 0.002735, -0.494075]
# I just had to split number 4 into two!
refineries_input_flows = [0.007293, -0.007293, 0.072926, 0.381951, 0.033728, 0.002735, -0.49134]
# Flows Into Refineries
sankey.add(flows=refineries_input_flows,
           labels=["", "", "",
                   "41.9 Mt", "Feedstock \n Imports \n3.7 Mt",
                   "Backflow \n0.3 Mt", " "],
           orientations=[1, 1, 0, -1, 1, -1, 0],
           facecolor="#FFA737", # #E5DDC8
           prior=0,
           connect=(2, 2))

# flows3 = [0.447584, 0.002735, 0.033728, 0.007293, -0.491340]

# Crude Oil Stocks Sankey loop
sankey.add(flows=[0.007293, -0.007293],
           orientations=[1, 1],
           # Orientation of 1 means sankey branch goes up relative to the main trunk
           prior=1,
           connect=(0, 1))

sankey.add(flows=[0.381951, -0.381951],
           labels=["Oil and \nNatural Gas \nImports \n41.9 Mt", " "],
           orientations=[0, 1],
           prior=1,
           connect=(3, 1),
           trunklength=1.5,
           facecolor="#50B2C0")

refineries_old = [0.00009115770, -0.00009115770, 0.49134, -0.015497, -0.475843]

refineries = [0.00009115770, -0.00009115770, 0.49134, -0.015497, -0.475843]

sankey.add(flows=refineries,
           patchlabel="Refineries",
           labels=[" ", " ", " ", "Losses \n1.7 Mt", " "],
           orientations=[-1, -1, 0, 1, 0],
           facecolor="#DB1F48",
           prior=1,
           connect=(6, 2),
           trunklength=1)

sankey.add(flows=[0.00009115770, -0.00009115770],
           prior=4,
           orientations=[-1, -1],
           connect=(0, 1),
           trunklength=1)

# Flows for Refineries' Outputs
refineries_output_flows = [0.475843, -0.017320, -0.030994, -0.172288, -0.020055, -0.235187]

sankey.add(flows=refineries_output_flows,
           labels=[" ", "Marine \nBunkers \n1.9 Mt",
                   "Energy \nIndustry \n Use \n3.4 Mt",
                   "Exports \n18.9 Mt",
                   "Feedstock \nExports \n2.2 Mt ",
                   ""],
           orientations=[0, 1, 1, 0, 1, -1],
           pathlengths=0.2,
           facecolor="#004369",
           prior=4,
           connect=(4, 0))

# Flows for the Inland Deliveries section
inland_delivery_flows = [0.235187, 0.277119, -0.004558, -0.403829, -0.002735, -0.018232, -0.045579, -0.037375]

# Sankey for Inland Delivery Use
sankey.add(flows=inland_delivery_flows,
           labels=[" ", "Petroleum \nImports \n30.4 Mt", "Losses \n0.5 Mt", "Transport \n44.3 Mt",
                   "Backflow to \nRefinery \n0.3 Mt", "Industry \n2.0 Mt",
                   "Domestic \nand \nOther \n5.0 Mt", "Non-energy \nuse \n4.1 Mt"],
           orientations=[1, 0, 1, 0, 1, -1, -1, -1],
           trunklength=1,
           facecolor="#E5DDC8", # #E5DDC8
           prior=6,
           connect=(5, 0))

ax.text(2.7, .55, "Crude Oil Stocks \n 0.8 Mt", fontfamily="Jost",
        horizontalalignment="center")
ax.text(3.74, -1.85, "Petroleum Stocks \n 0.01 Mt", fontfamily="Jost",
        horizontalalignment="center")
ax.text(5.1, -1.75, "Inland \nDelivery \n25.8 Mt", fontfamily="Jost",
        horizontalalignment="center")

sankey.finish()
# Turn off figure border
plt.axis('off')

plt.savefig("sankey-petroleum-2023.png", dpi=800, transparent=False)
plt.show()
