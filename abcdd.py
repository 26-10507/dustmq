import streamlit as st
import requests

# --- 설정 ---
API_KEY = "여기에_본인의_API_키를_넣으세요"  # OpenWeatherMap에서 받은 키 입력
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

st.set_page_config(page_title="오늘 뭐 입지?", page_icon="👕")

# --- 앱 화면 구성 ---
st.title("☀️ 오늘 뭐 입지? 날씨별 옷차림 추천")
city = st.text_input("날씨를 확인할 도시 이름을 영어로 입력하세요 (예: Seoul, Busan)", "Seoul")

if st.button("날씨 확인 및 추천받기"):
    # 날씨 데이터 가져오기 (단위는 섭씨 Celsius)
    params = {"q": city, "appid": API_KEY, "units": "metric", "lang": "kr"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        
        # 날씨 정보 출력
        st.subheader(f"📍 {city}의 현재 날씨")
        col1, col2, col3 = st.columns(3)
        col1.metric("온도", f"{temp}°C")
        col2.metric("습도", f"{humidity}%")
        col3.write(f"상태: {description}")

        # --- 옷차림 추천 로직 ---
        st.divider()
        st.subheader("👕 추천 옷차림")
        
        if temp >= 28:
            st.info("민소매, 반바지, 원피스 등 시원한 옷차림을 추천해요.")
        elif 23 <= temp < 28:
            st.info("반팔, 얇은 셔츠, 반바지나 면바지가 적당해요.")
        elif 20 <= temp < 23:
            st.info("긴팔 티셔츠, 가디건, 청바지나 슬랙스를 입으세요.")
        elif 17 <= temp < 20:
            st.info("니트, 맨투맨, 가디건, 청바지를 추천합니다.")
        elif 12 <= temp < 17:
            st.info("자켓, 셔츠, 가디건, 간절기용 코트를 챙기세요.")
        elif 9 <= temp < 12:
            st.info("트렌치코트, 야상, 여러 겹 껴입는 것을 추천해요.")
        elif 5 <= temp < 9:
            st.info("코트, 가죽 자켓, 히트텍 등 방한에 신경 쓰세요.")
        else:
            st.info("패딩, 두꺼운 코트, 목도리와 장갑이 필수예요!")
            
    else:
        st.error("도시 이름을 찾을 수 없습니다. 철자를 확인해 주세요!")
