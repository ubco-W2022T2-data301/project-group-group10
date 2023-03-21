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
    
def load(url_or_path_to_csv_file):
    
    df_adol=(pd.read_csv(url_or_path_to_csv_file)
        .drop(columns='smoker')
        .rename(columns={'age':'Age','sex':'Sex','bmi':'BMI','children':'Children','region':'Region','charges':'Medical expenses'})
        .assign(Group_of_age=lambda x: x['Age'].apply(typeofage))
        .loc[lambda x:x['Group_of_age']=='adolescent']
        .loc[lambda x:x['Sex']=='female']
        .sort_values('Region',ascending=True)
        .sort_values('Age',ascending=True)
        .reset_index(drop=True)
    )
    df_young=(pd.read_csv(url_or_path_to_csv_file)
        .drop(columns='smoker')
        .rename(columns={'age':'Age','sex':'Sex','bmi':'BMI','children':'Children','region':'Region','charges':'Medical expenses'})
        .assign(Group_of_age=lambda x: x['Age'].apply(typeofage))
        .loc[lambda x:x['Group_of_age']=='young adult']
        .loc[lambda x:x['Sex']=='female']
        .sort_values('Region',ascending=True)
        .sort_values('Age',ascending=True)
        .reset_index(drop=True)
    )

    df_mid=(pd.read_csv(url_or_path_to_csv_file)
        .drop(columns='smoker')
        .rename(columns={'age':'Age','sex':'Sex','bmi':'BMI','children':'Children','region':'Region','charges':'Medical expenses'})
        .assign(Group_of_age=lambda x: x['Age'].apply(typeofage))
        .loc[lambda x:x['Group_of_age']=='middle-aged adult']
        .loc[lambda x:x['Sex']=='female']
        .sort_values('Region',ascending=True)
        .sort_values('Age',ascending=True)
        .reset_index(drop=True)
    )

    df_older=(pd.read_csv(url_or_path_to_csv_file)
        .drop(columns='smoker')
        .rename(columns={'age':'Age','sex':'Sex','bmi':'BMI','children':'Children','region':'Region','charges':'Medical expenses'})
        .assign(Group_of_age=lambda x: x['Age'].apply(typeofage))
        .loc[lambda x:x['Group_of_age']=='older adult']
        .loc[lambda x:x['Sex']=='female']
        .sort_values('Region',ascending=True)
        .sort_values('Age',ascending=True)
        .reset_index(drop=True)
    )
    
    df_el=(pd.read_csv(url_or_path_to_csv_file)
        .drop(columns='smoker')
        .rename(columns={'age':'Age','sex':'Sex','bmi':'BMI','children':'Children','region':'Region','charges':'Medical expenses'})
        .assign(Group_of_age=lambda x: x['Age'].apply(typeofage))
        .loc[lambda x:x['Group_of_age']=='elderly']
        .loc[lambda x:x['Sex']=='female']
        .sort_values('Region',ascending=True)
        .sort_values('Age',ascending=True)
        .reset_index(drop=True)
    )


    

    return df_adol,df_young,df_mid,df_older,df_el

load('../../data/raw/insurance.csv')