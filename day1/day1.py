import pandas as pd

def location_ID_diff(df: pd.DataFrame):
    c1 = df['c1']
    c2 = df['c2']

    c1 = c1.sort_values().reset_index(drop=True)
    c2 = c2.sort_values().reset_index(drop=True)

    df = pd.concat([c1,c2],axis=1)
    df['diff'] = abs(df['c1'] - df['c2'])

    total_diff = df['diff'].sum()
    
    print(total_diff)
    
    return total_diff

example_df = pd.read_csv('day1_example.csv', delimiter = "   ",engine = 'python')
df = pd.read_csv('day1_input.csv', delimiter = "   ",engine = 'python')

location_ID_diff(df)


def similarity_score(df: pd.DataFrame):
    c2 = df['c2']
    
    c2_value_counts = c2.value_counts()
    
    similarity_df = pd.merge(df['c1'],c2_value_counts,left_on='c1',right_index=True)

    similarity_value = (similarity_df['c1'] * similarity_df['count']).sum()
    
    print(similarity_value)
    
    return similarity_value


similarity_score(df)