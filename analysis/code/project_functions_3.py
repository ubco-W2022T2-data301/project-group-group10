import pandas as pd

def typeofage(age):
    if age <= 19:
        return 'adolescent'
    elif 20 <= age <= 35:
        return 'young adult'
    elif 36 <= age <= 50:
        return 'middle-aged adult'
    elif 51 <= age <= 65:
        return 'older adult'  
    else:
        return 'elderly'
    
def load_and_process(url_or_path_to_csv_file):

    df_young=(pd.read_csv(url_or_path_to_csv_file)
        .drop(columns='smoker')
        .rename(columns={'age':'Age','sex':'Sex','bmi':'BMI','children':'Children','region':'Region','charges':'Medical expenses'})
        .assign(Group_of_age=lambda x: x['Age'].apply(typeofage))
        .loc[lambda x:x['Age']<=35]
        .loc[lambda x:x['Age']>=20]
        .loc[lambda x:x['Sex']=='female']
        .loc[lambda x:x['BMI']>=30]
        .loc[lambda x:x['Children']!=0]
        .sort_values('Region',ascending=True)
        .sort_values('Age',ascending=True)
        .reset_index(drop=True)
    )

    

    df_mid=(pd.read_csv(url_or_path_to_csv_file)
        .drop(columns='smoker')
        .rename(columns={'age':'Age','sex':'Sex','bmi':'BMI','children':'Children','region':'Region','charges':'Medical expenses'})
        .assign(Group_of_age=lambda x: x['Age'].apply(typeofage))
        .loc[lambda x:x['Age']<=50]
        .loc[lambda x:x['Age']>=36]
        .loc[lambda x:x['Sex']=='female']
        .loc[lambda x:x['BMI']>=30]
        .loc[lambda x:x['Children']!=0]
        .sort_values('Region',ascending=True)
        .sort_values('Age',ascending=True)
        .reset_index(drop=True)
    )

    

    return df_young , df_mid

load_and_process('../data/raw/insurance.csv')
                 