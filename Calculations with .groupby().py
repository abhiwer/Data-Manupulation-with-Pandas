'''
Calculations with .groupby()
The .groupby() method makes life much easier. In this exercise, you'll perform the same calculations as last time, except you'll use the .groupby() method. You'll also perform calculations on data grouped by two variables to see if sales differs by store type depending on if it's a holiday week or not.

sales is available and pandas is loaded as pd.

Instructions 1/2
35 XP
Group sales by "type", take the sum of "weekly_sales", and store as sales_by_type.
Calculate the proportion of sales at each store type by dividing by the sum of sales_by_type. Assign to sales_propn_by_type.

'''
# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type / sales_by_type.sum()
print(sales_propn_by_type)