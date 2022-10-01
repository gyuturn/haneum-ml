# static에 고정적으로 들어가야할 사진 등이 들어간다
# templates 등에 html이 들어가는 구조이다.

from flask import Flask, request, jsonify
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

# 만들어온 모델은 다음과 같이 불러온다.
# 즉, 이미 저장되어 있어야한다.!
model = joblib.load('./regression_model.pkl')
scaler = joblib.load('./regression-scaler.pkl')


# 다음과 같이 Flask Module이 시작된다.
app = Flask(__name__)



# # 기본주소에서 일어나는 일
# @app.route('/')
# def main():
# 	# home.html을 띄워준다.
#     return render_template('home.html')

# predict 페이지에서는 POST라는 method가 사용될 것이다.
@app.route('/regression', methods=['POST'])
def home():
    jsonData = request.json
  
    temporal_data={'kda': jsonData['kda'], 'cs_per_minute':jsonData['cs_per_minute'], 'play_time': jsonData['play_time'], 'hit_damage': jsonData['hit_damage']}
    UNKNOWN_USER = np.array([temporal_data['kda'], temporal_data['cs_per_minute'], temporal_data['play_time'], temporal_data['hit_damage']])
    UNKNOWN_USER = np.array([UNKNOWN_USER])
    UNKNOWN_USER = scaler.transform(UNKNOWN_USER)
    is_troll = model.predict(UNKNOWN_USER)
    troll_possibility = model.predict_proba(UNKNOWN_USER)
    
    
    
#     arr = np.array([[data1, data2, data3, data4]])
#     is_troll = model.predict(arr)
#     troll_possibility = model.predict_proba(arr)
    print(f'트롤확률: {troll_possibility[0][0]*100}%')
    # 보여줄 페이지 그리고 어떤 데이터를 넘길지에 대해서 확인한다....
    # 모델이 예측한 결과를 넘겨서 그 값에 따라 if문을 작성하게 한다.
    return jsonify({"troll_possibility":troll_possibility[0][0]*100}) 



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='8080')