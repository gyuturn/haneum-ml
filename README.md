# FlaskApi 서버 
![image](https://user-images.githubusercontent.com/87477702/197347107-ac9becac-2e43-4d67-b353-9fb9d0d69aa2.png)
- http://52.79.58.170:5000/
- JAVA에서 파이선 머신러닝을 이용하기 위한  API Server

## 기능
- LinearRegression을 이용한 유저의 트롤확률 분석
- KMeans클러스터링을 이용하여 트롤확률을 기반으로 듀오 추천

## API 명세
## regression(회기분석) Api -POST
- http://52.79.58.170:5000/regression

- request
  - json
{
 "kda": float,
 "cs_per_minute": float,
  "play_time": float,
   "hit_damage": float
}

-  response
   - json
{
    "troll_possibility":"xxx%"
}

## KMeans Api -POST
- http://52.79.58.170:5000/kmeans

- request
   - json
{
  "troll_possibility":"xxx%"
  "tier": "STRING"
}

- response
  - json
{
    "cluster": INTEGER
}
