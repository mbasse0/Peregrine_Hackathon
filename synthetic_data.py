import pandas as pd
import numpy as np

# I need synthetic data for the following:
# damage estimation (costs) by month, location, and damage type (4 damage types: wind, flood ,storm surge, erosion)

synthetic_damage_data_list = []

#location is to dimensionsal with x element of [1,100] and y element of [1,100]
# Generate synthetic data
for month in range(1, 25):
    for x in range(1, 11):
        for y in range(1, 11):
            location = (x, y)
            for damage_type in ['Wind', 'Flooding', 'Storm Surge', 'Erosion']:
                #50% chance of 0 damage
                #50% of uniform, 1000000 to 5000000
                if np.random.rand() < 0.5:
                    damage_cost = 0
                else:
                    damage_cost = np.random.randint(1000000, 5000000)
            synthetic_damage_data_list.append({'month': month, 'location': location, 'damage_type': damage_type, 'damage_cost': damage_cost})

synthetic_damage_data_df = pd.DataFrame(synthetic_damage_data_list)

capital_investments_df = pd.read_csv('hackathon_student/01_Data/02_For_students/02_future/capital_investments.csv')
#the protection type column has multiple types of damage types concatenated. We need to transform to a dataframe of ixm where i is the number of measures and m is the different types where each value is the % reduction in damage cost (Damage_Reduction_Pct)

cost_reduction_list = []

for index, row in capital_investments_df.iterrows():
    protection_type = row['Protection_Type']
    protection_types = protection_type.split(',')
    for protection_type in protection_types:
        #remove first space
        protection_type = protection_type.strip()
        #if "All Hazards" it should be the same pct for all damage types
        if protection_type == "All Hazards":
            for damage_type in ['Wind', 'Flooding', 'Storm Surge', 'Erosion']:
                cost_reduction_list.append({'damage_type': damage_type, 'damage_reduction_pct': row['Damage_Reduction_Pct']})
        else:
            cost_reduction_list.append({'damage_type': protection_type, 'damage_reduction_pct': row['Damage_Reduction_Pct']})

cost_reduction_df = pd.DataFrame(cost_reduction_list)

#no multiplying the cost reduction df by the synthetic data df given the damage_type = protection_type (for all t)

#merge the two dataframes on the protection_type column

print(cost_reduction_df.head())
print(synthetic_damage_data_df.head())
merged_df = pd.merge(synthetic_damage_data_df, cost_reduction_df, on='damage_type', how='outer')

print(merged_df.head())

merged_df['reduced_damage_cost'] = merged_df['damage_cost'] * (1 - merged_df['damage_reduction_pct']/100)

merged_df = merged_df.fillna(0)
print(merged_df.describe())

merged_df.to_csv('damage_cost_reduction.csv', index=False)


