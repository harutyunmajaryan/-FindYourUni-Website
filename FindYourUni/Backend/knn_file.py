import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors



def csv_scores_processor():
    """If need be, will make every score in csv file from 1-100"""
    pass

def ratings_processor(raw_ratings):
    user_ratings = {'NSS_SAT': raw_ratings[0], 'OVERALL_SUCCESS_RATE': raw_ratings[1]}
    return user_ratings

def course_ranker(user_importance, csv_path='filtered_temp.csv'): #assuming this csv file has already had filters applied
    df = pd.read_csv(csv_path)
    factors = list(user_importance.keys())                      #creates list of factors that the KNN algo cares about
    stretcher = np.sqrt([user_importance[f] for f in factors])  #creates list of numbers to stretch each axis/factor by, based on square root of user importance rating
    stretched_data = df[factors].values * stretcher             #creates 2d numpy array of each course's factors multiplied by that factor's 'stretcher'
    target_pin = np.array([100 for f in factors])               #creating an array that corresponds to the perfect score in every factor
    stretched_pin = target_pin * stretcher                      #creating an array that corresponds to the perfect score in every factor
    knn = NearestNeighbors(n_neighbors=10, metric='euclidean', algorithm='brute')   #I care about top 10 courses
    knn.fit(stretched_data)                                     #indexing the array in memory
    distances, indices = knn.kneighbors([stretched_pin])        #runs knn algorithm, finds row indices in csv file and puts it into a list ordered by euclidian distance of the corresponding course's plot form the stretched pin
    top_10_ids = df.iloc[indices[0]][['UNIVERSITY_NAME', 'COURSE_NAME', 'COURSE_URL']].to_dict(orient='records')    #gets list of course ids ordered by closest fit
    return top_10_ids

if __name__ == '__main__':
    raw_user_ratings = [8, 1]
    ratings = ratings_processor(raw_user_ratings)
    top_courses = course_ranker(ratings)
    print(top_courses)
