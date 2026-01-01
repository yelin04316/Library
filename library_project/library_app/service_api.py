# 외부 API 처리 (도서관 정보나루)
# DB 저장 담당
import requests
from library_app.models import LibraryMap

API_URL = "http://data4library.kr/api/libSrch"
AUTH_KEY = "13761d3b3d5d8014011a5f344db9843993b339d4f78719186211ea97e1761e71"

def load_libraries():
    page = 1
    page_size = 200

    while True:
        params = {
            "authKey": AUTH_KEY,
            "pageNo": page,
            "pageSize": page_size,
            "format": "json",
        }

        res = requests.get(API_URL, params=params)
        data = res.json()

        libs = data["response"]["libs"]

        if not libs:
            break  # 더 이상 데이터 없음

        for item in libs:
            lib = item["lib"]

            lat = lib.get("latitude")
            lng = lib.get("longitude")

            if not lat or not lng:
                continue

            LibraryMap.objects.update_or_create(
                lib_code=lib["libCode"],
                defaults={
                    "name": lib["libName"],
                    "latitude": float(lat),
                    "longitude": float(lng),
                }
            )

        print(f"{page} 페이지 저장 완료")
        page += 1