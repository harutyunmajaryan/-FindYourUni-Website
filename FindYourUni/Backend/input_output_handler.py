from flask import Flask, request, jsonify
from flask_cors import CORS
from knn_file import ratings_processor, course_ranker
from filtering import filter

app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'])
def data_handler():
    user_data = request.json
    
    filter(user_data['country'], user_data['course'])
    
    sat_rating = int(user_data['student_satisfaction'])
    success_rating = int(user_data['successrate'])
    

    user_prefs = ratings_processor([sat_rating, success_rating])
    
    top_10_list = course_ranker(user_prefs)
    

    return jsonify(top_10_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
