import pandas as pd

df = pd.read_csv("violations_merged.csv", low_memory=False)

clean_violation = pd.DataFrame(columns=['Violation Code'])

for row in range(len(df['Violation Code'])):
    code = str(df['Violation Code'][row])
    if 'M' in code:
        clean_code = code[1:]
        clean_code = clean_code.lstrip('0')
        clean_violation.loc[row] = clean_code

    else:
        clean_violation.loc[row] = code

df['Violation Code'] = clean_violation['Violation Code']
df.to_csv("violations_merged.csv", index=False)