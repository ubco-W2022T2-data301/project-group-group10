import pandas as pd

def load_and_process(url_or_path_to_csv_file):
   
    def bmi_category(bmi):
        if bmi < 16:
            return 'underweight'
        elif 16 <= bmi <= 18.4:
            return 'underweight'
        elif 18.5 <= bmi <= 24.9:
            return 'normal'
        elif 25 <= bmi <= 29.9:
            return 'overweight'
        else:
            return 'obese'

    
    def age_category(age):
        if age < 19:
            return 'teen'
        elif 20 <= age <= 29:
            return '20s'
        elif 30 <= age <= 39:
            return '30s'
        elif 40 <= age <= 49:
            return '40s'
        elif 50 <= age <= 59:
            return '50s'  
        else:
            return '60s'

    new_order = ['age_group', 'age', 'sex', 'children', 'has_children', 'smoker', 'region', 'bmi', 'BMI_Category']
    
    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .drop(columns=['charges'])
        .assign(has_children=lambda x: x['children'].apply(lambda c: 'yes' if c > 0 else 'no'))
        .assign(BMI_Category=lambda x: x['bmi'].apply(bmi_category))
        .loc[lambda x: x['bmi'] >= 18.5]
    )
    
    df2 = (
        df1
        .assign(age_group=lambda x: x['age'].apply(age_category))
        .pipe(lambda x: x.reindex(columns=new_order))
        .rename(columns={'age_group':'Age Group', 'age':'Age','sex':'Gender','bmi':'BMI','children':'Children','region':'Region', 'smoker':'Smoker', 'has_children':'Has Children', 'BMI_Category':'BMI Category'})
        .sort_values('BMI Category', ascending=True)
        .reset_index(drop=True)
    )

    return df2


data = load_and_process("../data/raw/insurance.csv")
data
