# Import Libraries
import pandas as pd
import numpy


## FILL IN HERE ##
filepath = '' 
filename = ''
##################


cy = pd.read_csv(filepath + '\\data\\data\\yield_df.csv') 
cy = cy.drop(['Unnamed: 0'], axis=1)
def addstuff(df,filename, fill = False):
    stuff = pd.read_csv(filename) 
    stuff = stuff.drop(['Country Code', 'Indicator Code'], axis=1)
    if fill:
        stuff = stuff.fillna(0)
    stuff = stuff.melt(id_vars=['Country Name',"Indicator Name"]) 
    stuff['variable'] = pd.to_numeric(stuff['variable'])
    # GDP = GDP.rename(index={"value": GDP['Indicator Name'].iloc[0]}) 
    added = pd.merge(df, stuff,  how='left', left_on=['Area','Year'], right_on = ['Country Name','variable'])
    added = added.rename(columns={"value": added['Indicator Name'].iloc[0]})
    added = added.drop(['Country Name', 'variable','Indicator Name'], axis=1)
    return added
cy = addstuff(cy,filepath + '\\data\\Trade percentage of GDP.csv')
cy = addstuff(cy,filepath + '\\data\\Patent Applications.csv', True)
cy = addstuff(cy,filepath + '\\data\\Birth rate per 1k.csv')
cy = addstuff(cy,filepath + '\\data\\Arable Land.csv')
cy = addstuff(cy,filepath + '\\data\\Fixed Telephone Subscriptions.csv')
cy = addstuff(cy,filepath + '\\data\\Food imports.csv')
cy = addstuff(cy,filepath + '\\data\\GNI in US$.csv')
cy = addstuff(cy,filepath + '\\data\\Gender Ratio.csv')
cy = addstuff(cy,filepath + '\\data\\Land area.csv')
cy = addstuff(cy,filepath + '\\data\\Military Expenditure percent of gdp.csv')
cy = addstuff(cy,filepath + '\\data\\Net Migration.csv')
cy = addstuff(cy,filepath + '\\data\\Population ages 15-64 (% of total population).csv')
cy = addstuff(cy,filepath + '\\data\\agricultural_irrigated_land.csv')
cy = addstuff(cy,filepath + '\\data\\agricultural_land_sq_km.csv')
cy = addstuff(cy,filepath + '\\data\\agricultural_machinery_tractors.csv')
cy = addstuff(cy,filepath + '\\data\\droughts_floods_ex_temp.csv')
cy = addstuff(cy,filepath + '\\data\\employment_in_agriculture.csv')
cy.to_csv(filename+ ".csv")

