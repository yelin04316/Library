# 거리 계산 같은 순수 로직

# 내 위치 <-> 도서관 거리 계산
import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # km
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)

    a = (
        math.sin(d_lat / 2) ** 2 +
        math.cos(math.radians(lat1)) *
        math.cos(math.radians(lat2)) *
        math.sin(d_lon / 2) ** 2
    )
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))
