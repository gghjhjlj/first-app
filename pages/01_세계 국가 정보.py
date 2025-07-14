import pandas as pd
import json

def load():
    try:
        df_c = pd.read_csv("countries.csv")
        df_cr = pd.read_csv("crime.csv")
        df_ex = pd.read_csv("currency.csv")
        with open("attractions.json", encoding="utf-8") as f:
            attractions = json.load(f)
    except FileNotFoundError:
        # 샘플 데이터 삽입
        df_c = pd.DataFrame({
            "country": ["South Korea", "Japan"],
            "capital": ["Seoul", "Tokyo"],
            "population": [51780000, 125800000],
            "area_km2": [100210, 377975]
        })
        df_cr = pd.DataFrame({
            "country": ["South Korea", "Japan"],
            "crime_index": [35.0, 20.0]
        })
        df_ex = pd.DataFrame({
            "country": ["South Korea", "Japan"],
            "exchange_rate_usd": ["1300 KRW", "155 JPY"]
        })
        attractions = {
            "South Korea": ["Gyeongbokgung", "Jeju Island"],
            "Japan": ["Mount Fuji", "Tokyo Disneyland"]
        }
    return df_c, df_cr, df_ex, attractions
