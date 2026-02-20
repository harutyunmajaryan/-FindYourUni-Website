import pandas as pd
from thefuzz import process
from thefuzz import fuzz
df = pd.read_csv("master_dataset_v1.3.csv")
df[['NSS_SAT', 'OVERALL_SUCCESS_RATE']] = df[['NSS_SAT', 'OVERALL_SUCCESS_RATE']].fillna(50)

def filter(user_input_country, user_input_course):
    # user_input_country = "England"                         #These are some test inputs that were used to check filtering based on countries
    # user_input_country = "Wales"
    # user_input_country = "Northern Ireland"
    # user_input_country = "Scotland"


    if user_input_country == "England":
        country_code = "XF"
    elif user_input_country == "Wales":
        country_code = "XI"
    elif user_input_country == "Northern Ireland":
        country_code = "XG"
    elif user_input_country == "Scotland":
        country_code = "XH"


    # user_input_course = "C"                                  #These are some test inputs that were used to check filtering based on courses
    # user_input_course = "CComp" 
    # user_input_course = "Computer Science"
    # user_input_course = "CS"
    # user_input_course = "Computation"
    # user_input_course = "Compatition" 
    # user_input_course = "AI"
    # user_input_course = "ML"   


    match_based_on_course = process.extractBests(user_input_course, df["COURSE_NAME"], scorer= fuzz.partial_token_set_ratio, score_cutoff=0)
    final_df = pd.DataFrame(columns=df.columns)

    match_names = [m[0] for m in match_based_on_course]
    final_df = df[(df["COURSE_NAME"].isin(match_names)) & (df["COUNTRY_CODE"] == country_code)]

    final_df = final_df.drop_duplicates()
    final_df.to_csv("filtered_temp.csv", index=False)
    return final_df

if __name__ == '__main__':    
    print(filter("England", "Art"))
