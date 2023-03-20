{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "306fa2f1-983a-416f-bd4d-d66348d36ac2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "7254958d-2d93-4c2b-b827-785b3e26cee0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age_group</th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>children</th>\n",
       "      <th>has_children</th>\n",
       "      <th>smoker</th>\n",
       "      <th>region</th>\n",
       "      <th>bmi</th>\n",
       "      <th>BMI_Category</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>40s</td>\n",
       "      <td>46</td>\n",
       "      <td>female</td>\n",
       "      <td>2</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>northwest</td>\n",
       "      <td>19.950</td>\n",
       "      <td>Normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>60s</td>\n",
       "      <td>19</td>\n",
       "      <td>female</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>northwest</td>\n",
       "      <td>22.515</td>\n",
       "      <td>Normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>teen</td>\n",
       "      <td>18</td>\n",
       "      <td>female</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>northeast</td>\n",
       "      <td>21.660</td>\n",
       "      <td>Normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>50s</td>\n",
       "      <td>55</td>\n",
       "      <td>male</td>\n",
       "      <td>1</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>southwest</td>\n",
       "      <td>21.500</td>\n",
       "      <td>Normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>40s</td>\n",
       "      <td>43</td>\n",
       "      <td>female</td>\n",
       "      <td>2</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>northeast</td>\n",
       "      <td>20.045</td>\n",
       "      <td>Normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1313</th>\n",
       "      <td>20s</td>\n",
       "      <td>21</td>\n",
       "      <td>male</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>northeast</td>\n",
       "      <td>27.360</td>\n",
       "      <td>Overweight</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1314</th>\n",
       "      <td>30s</td>\n",
       "      <td>34</td>\n",
       "      <td>female</td>\n",
       "      <td>1</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>northwest</td>\n",
       "      <td>26.410</td>\n",
       "      <td>Overweight</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1315</th>\n",
       "      <td>40s</td>\n",
       "      <td>47</td>\n",
       "      <td>female</td>\n",
       "      <td>1</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>northwest</td>\n",
       "      <td>29.545</td>\n",
       "      <td>Overweight</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1316</th>\n",
       "      <td>30s</td>\n",
       "      <td>36</td>\n",
       "      <td>male</td>\n",
       "      <td>3</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>northeast</td>\n",
       "      <td>28.880</td>\n",
       "      <td>Overweight</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1317</th>\n",
       "      <td>60s</td>\n",
       "      <td>61</td>\n",
       "      <td>female</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>northwest</td>\n",
       "      <td>29.070</td>\n",
       "      <td>Overweight</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1318 rows × 9 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     age_group  age  gender  children has_children smoker     region     bmi  \\\n",
       "0          40s   46  female         2          yes     no  northwest  19.950   \n",
       "1          60s   19  female         0           no     no  northwest  22.515   \n",
       "2         teen   18  female         0           no    yes  northeast  21.660   \n",
       "3          50s   55    male         1          yes     no  southwest  21.500   \n",
       "4          40s   43  female         2          yes    yes  northeast  20.045   \n",
       "...        ...  ...     ...       ...          ...    ...        ...     ...   \n",
       "1313       20s   21    male         0           no     no  northeast  27.360   \n",
       "1314       30s   34  female         1          yes     no  northwest  26.410   \n",
       "1315       40s   47  female         1          yes     no  northwest  29.545   \n",
       "1316       30s   36    male         3          yes     no  northeast  28.880   \n",
       "1317       60s   61  female         0           no    yes  northwest  29.070   \n",
       "\n",
       "     BMI_Category  \n",
       "0          Normal  \n",
       "1          Normal  \n",
       "2          Normal  \n",
       "3          Normal  \n",
       "4          Normal  \n",
       "...           ...  \n",
       "1313   Overweight  \n",
       "1314   Overweight  \n",
       "1315   Overweight  \n",
       "1316   Overweight  \n",
       "1317   Overweight  \n",
       "\n",
       "[1318 rows x 9 columns]"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "def load_and_process(url_or_path_to_csv_file):\n",
    "   \n",
    "    def bmi_category(bmi):\n",
    "        if bmi < 16:\n",
    "            return 'Underweight'\n",
    "        elif 16 <= bmi <= 18.4:\n",
    "            return 'Underweight'\n",
    "        elif 18.5 <= bmi <= 24.9:\n",
    "            return 'Normal'\n",
    "        elif 25 <= bmi <= 29.9:\n",
    "            return 'Overweight'\n",
    "        else:\n",
    "            return 'Obese'\n",
    "\n",
    "    \n",
    "    def age_category(age):\n",
    "        if age < 19:\n",
    "            return 'teen'\n",
    "        elif 20 <= age <= 29:\n",
    "            return '20s'\n",
    "        elif 30 <= age <= 39:\n",
    "            return '30s'\n",
    "        elif 40 <= age <= 49:\n",
    "            return '40s'\n",
    "        elif 50 <= age <= 59:\n",
    "            return '50s'  \n",
    "        else:\n",
    "            return '60s'\n",
    "\n",
    "    new_order = ['age_group', 'age', 'sex', 'children', 'has_children', 'smoker', 'region', 'bmi', 'BMI_Category']\n",
    "    \n",
    "    df1 = (\n",
    "        pd.read_csv(url_or_path_to_csv_file)\n",
    "        .drop(columns=['charges'])\n",
    "        .assign(has_children=lambda x: x['children'].apply(lambda c: 'yes' if c > 0 else 'no'))\n",
    "        .assign(BMI_Category=lambda x: x['bmi'].apply(bmi_category))\n",
    "        .loc[lambda x: x['bmi'] >= 18.5]\n",
    "    )\n",
    "    \n",
    "    df2 = (\n",
    "        df1\n",
    "        .assign(age_group=lambda x: x['age'].apply(age_category))\n",
    "        .pipe(lambda x: x.reindex(columns=new_order))\n",
    "        .rename(columns={\"sex\": \"gender\"})\n",
    "        .sort_values('BMI_Category', ascending=True)\n",
    "        .reset_index(drop=True)\n",
    "    )\n",
    "\n",
    "    return df2\n",
    "\n",
    "\n",
    "data = load_and_process(\"../data/raw/insurance.csv\")\n",
    "data\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0acb23e9-ff64-4929-b061-fcc86d7e8d6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "    \n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
