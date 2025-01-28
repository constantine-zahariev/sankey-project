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
                     title="Electricity Sources and End Use in the UK 2022")

# We need to use fractional values for the Sankey branch values

# Fractions from renewable sources - their total is then an output that
# goes into the next section
# https://www.gov.uk/government/statistics/digest-of-uk-energy-statistics-dukes-2023
# Chapter 5: Electricity
renewables_in = [-0.314818, 0.144022, 0.011694, 0.159101]

# Fractions for electricity generation where renewables are bunched together
# First element in list represents the output of this section - all the energy
# produced then goes into the next section (consumption)
production = [-1.0, 0.314818, 0.185413, 0.396676, 0.024927, 0.043237, 0.023850, 0.010002, 0.001077]

production_all = [0.144022, 0.011694, 0.159101, 0.185413, 0.396676, 0.024927,
                  0.043237, 0.023850, 0.010002, 0.001077]

consumption = [1.0, -0.003385, -0.012925, -0.127558, -0.514079, -0.148023, -0.130020, -0.032005, -0.032005]


sankey = Sankey(ax=ax, unit=None, gap=0.4, scale=1.5, offset=0.3, shoulder=0.03, head_angle=130)

sankey.add(patchlabel="Renewables", flows=renewables_in,
           labels=["", "Wind, \nwave \n& solar \n93.6 TWh", "Hydro \n7.6 TWh", "Thermal \nrenewables \n103.4 TWh"],
           orientations=[0, -1, 1, 0],
           facecolor='#127475')

sankey.add(patchlabel="Total Production", flows=production,
           labels=["", "", "Nuclear \n120.5 TWh", "Natural Gas \n257.8 TWh", "Coal \n16.2 TWh",
                   "Other \nthermal \nsources \n28.1 TWh", "Imports \n15.5 TWh",
                   "Petroleum \n6.5 TWh", "Statistical \ndifferences \n0.7 TWh"],
           orientations=[0, 0, -1, 1, 1, 1, -1, -1, -1],
           facecolor='#F5DFBB',
           prior=0,
           connect=(0, 1))

sankey.add(flows=consumption,
           labels=["", "Iron \n& Steel \nProduction \n2.2 TWh", "Transport \n8.4 TWh",
                   "Other \nIndustry \n82.9 TWh", "Conversion, \nTransmission & \nDistribution \nLosses \n334.1 TWh",
                   "Domestic \n96.2 TWh", "Other \nConsumers \n84.5 TWh", "Energy \nIndustry \nUse \n20.8 TWh",
                   "Exports \n20.8 TWh"],
           orientations=[0, 1, 1, -1, 0, 1, 1, -1, -1],
           facecolor='#F2542D',
           prior=1,
           connect=(0, 0))

sankey.finish()
plt.axis('off')  # Turn off figure border
plt.savefig("electricity-sankey-2022.png", dpi=800, transparent=False)
plt.show()
