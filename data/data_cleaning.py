import pandas as pd

sheet1 = pd.read_excel('../data/Online_Retail_II.xlsx', sheet_name='Year 2009-2010')
sheet2 = pd.read_excel('../data/Online_Retail_II.xlsx', sheet_name='Year 2010-2011')

df_combined = pd.concat([sheet1, sheet2], ignore_index=True)

df_combined.to_csv('../data/online_retail_combined.csv', index=False)

print(f"Combined Shape: {df_combined.shape}")
