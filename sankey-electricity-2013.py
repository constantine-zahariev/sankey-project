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
                     title="Electricity Sources and End Use in the UK 2013")

# We need to use fractional values for the Sankey branch values

# Fractions from renewable sources - their total is then an output that
# goes into the next section
# Data source:
# https://www.gov.uk/government/statistics/digest-of-united-kingdom-energy-statistics-2014-internet-content-only
# Page 163, chart H.4: Electricity flow chart 2013 (TWh)
renewables_in = [-0.1185492, 0.034143, 0.008508, 0.075898]

# Fractions for electricity generation where renewables are bunched together
# First element in list represents the output of this section - all the energy
# produced then goes into the next section (consumption)
production = [-1.0, 0.1185492, 0.201052, 0.226464, 0.409381, 0.017016, 0.019590, 0.007612, 0.000336]

consumption = [1.0, -0.004254, -0.004590, -0.105452, -0.608306, -0.127057, -0.113848, -0.033024, -0.003470]

sankey = Sankey(ax=ax, unit=None, gap=0.4, scale=1.5, offset=0.3, shoulder=0.03, head_angle=130)

sankey.add(patchlabel="Renewables", flows=renewables_in,
           labels=["", "Wind, \nwave \n& solar \n30.5 TWh", "Hydro \n7.6 TWh", "Thermal \nrenewables \n67.8 TWh"],
           orientations=[0, -1, 1, 0],
           facecolor='#127475')

sankey.add(patchlabel="Total Production", flows=production,
           labels=["", "", "Nuclear \n179.6 TWh", "Natural Gas \n202.3 TWh", "Coal \n365.7 TWh",
                   "Other \nthermal \nsources \n15.2 TWh", "Imports \n17.5 TWh",
                   "Petroleum \n6.8 TWh", "Statistical \ndifferences \n0.3 TWh"],
           orientations=[0, 0, -1, 1, 1, 1, -1, -1, -1],
           facecolor='#F5DFBB',
           prior=0,
           connect=(0, 1))

sankey.add(flows=consumption,
           labels=["", "Iron \n& Steel \nProduction \n3.8 TWh", "Transport \n4.1 TWh",
                   "Other \nIndustry \n94.2 TWh", "Conversion, \nTransmission & \nDistribution \nLosses \n543.4 TWh",
                   "Domestic \n113.5 TWh", "Other \nConsumers \n101.7 TWh", "Energy \nIndustry \nUse \n29.5 TWh",
                   "Exports \n3.1 TWh"],
           orientations=[0, 1, 1, 1, 0, -1, 1, -1, -1],
           facecolor='#F2542D',
          prior=1,
          connect=(0, 0))

sankey.finish()
plt.axis('off')  # Turn off figure border
plt.savefig("electricity-sankey-2013.png", dpi=800, transparent=False)
plt.show()
