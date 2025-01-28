import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

# Set figure size and font
plt.rcParams["figure.figsize"] = (15, 7)
plt.rcParams['font.family'] = 'Jost'
plt.rcParams['font.size'] = '10.5'

fig = plt.figure()  # Create a figure object

# add_subplot is a method that acts on the fig object
# Call pattern: add_subplot(nrows, ncols, index, **kwargs)
# Subplots can include multiple rows and columns
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                     title="Electricity Sources and End Use in the UK 2023")

# We need to use fractional values for the Sankey branch values
# Data source:
# https://www.gov.uk/government/statistics/digest-of-uk-energy-statistics-dukes-2024
# Chapter 5: Electricity
renewables_in = [-0.343681, 0.163189, 0.014249, 0.166243]

# Fractions for electricity generation where renewables are bunched together
# First element in list represents the output of this section - all the energy
# produced then goes into the next section (consumption)
production = [-1.0, 0.343681, 0.173367,
              0.353520, 0.017812, 0.046819,
              0.056489, 0.007973, 0.000339]

production_all = [0.163189, 0.014249, 0.166243, 0.173367, 0.353520,
                  0.017812, 0.046819, 0.056489, 0.007973, 0.000339]

consumption = [1.0, -0.003562, -0.018490,
               -0.142663, -0.495674, -0.157082,
               -0.134690, -0.031722, -0.016115]

sankey = Sankey(ax=ax, unit=None, gap=0.4, scale=1.5, offset=0.3, shoulder=0.03, head_angle=130)

sankey.add(patchlabel="Renewables", flows=renewables_in,
           labels=["", "Wind, \nwave \n& solar \n96.2 TWh", "Hydro \n8.4 TWh", "Thermal \nrenewables \n98.0 TWh"],
           orientations=[0, -1, 1, 0],
           facecolor='#127475')

sankey.add(patchlabel="Total Production",
           flows=production,
           labels=["", "", "Nuclear \n102.2 TWh", "Natural Gas \n208.4 TWh", "Coal \n10.5 TWh",
                   "Other \nthermal \nsources \n27.6 TWh", "Imports \n33.3 TWh",
                   "Petroleum \n4.7 TWh", "Statistical \ndifferences \n0.2 TWh"],
           orientations=[0, 0, -1, 1, 1, 1, -1, -1, -1],
           facecolor='#F5DFBB',
           prior=0,
           connect=(0, 1))

sankey.add(flows=consumption,
           labels=["", "Iron \n& Steel \nProduction \n2.1 TWh", "Transport \n10.9 TWh",
                   "Other \nIndustry \n84.1 TWh", "Conversion, \nTransmission & \nDistribution \nLosses \n292.2 TWh",
                   "Domestic \n92.6 TWh", "Other \nConsumers \n79.4 TWh", "Energy \nIndustry \nUse \n18.7 TWh",
                   "Exports \n9.5 TWh"],
           orientations=[0, 1, 1, 1, 0, -1, 1, -1, -1],
           facecolor='#F2542D',
           prior=1,
           connect=(0, 0))

sankey.finish()
plt.axis('off')  # Turn off figure border
plt.savefig("electricity-sankey-2023.png", dpi=800, transparent=False)
plt.show()
