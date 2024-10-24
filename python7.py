# Quiz 1
import random
def generate_lotto_numbers():
    result = []
    while len(result) < 6:
        num = random.randint(1, 45)
        if num not in result:
            result.append(num)
    return result


print(generate_lotto_numbers())



# Quiz 2
class gugudan:
    def __init__(self, num):
        self.num = num
    def output(self):
        print(f"---{self.num}단---")
        for dan in range(1, 10):
            print(f"{self.num} x {dan} = {self.num * dan}")

user_input = int(input("구구단을 입력하세요:"))
Gugudan = gugudan(user_input)
Gugudan.output()




# Quiz 3

# 교통 시뮬레이션 및 경로 최적화 시스템을 구축하여 실시간으로 교통 상황을 분석.
# 가장 빠른 경로를 사용자에게 제공하는 프로그램

# Vehicle(차량) 클래스
class Vehicle:
    def __init__(self, vehicle_number, vehicle_type, current_location):
        self.vehicle_number = vehicle_number  # 차량 번호
        self.vehicle_type = vehicle_type  # 차량 종류 (승용차, 트럭 등)
        self.current_location = current_location  # 차량의 현재 위치

    # 차량의 위치 업데이트 메서드
    def update_location(self, new_location):
        """차량의 현재 위치를 업데이트합니다."""
        self.current_location = new_location
        print(f"{self.vehicle_number} 차량의 위치가 {self.current_location}로 업데이트되었습니다.")

    # 차량 정보 출력 메서드
    def vehicle_info(self):
        """차량 정보를 출력합니다."""
        return f"차량 번호: {self.vehicle_number}, 종류: {self.vehicle_type}, 현재 위치: {self.current_location}"


# Route(경로) 클래스
class Route:
    def __init__(self, start, end):
        self.start = start  # 출발지
        self.end = end  # 목적지
        self.stops = []  # 경유지 리스트
        self.distances = {}  # 경로의 거리 정보 저장

    # 경유지 추가 메서드
    def add_stop(self, stop, distance):
        """경로에 경유지를 추가하고 그에 따른 거리를 설정합니다."""
        self.stops.append(stop)
        self.distances[stop] = distance
        print(f"경유지 {stop}이(가) 추가되었습니다. 거리: {distance}km")

    # 경유지 제거 메서드
    def remove_stop(self, stop):
        """경유지를 제거합니다."""
        if stop in self.stops:
            self.stops.remove(stop)
            del self.distances[stop]
            print(f"경유지 {stop}이(가) 제거되었습니다.")
        else:
            print(f"경유지 {stop}이(가) 경로에 존재하지 않습니다.")

    # 최적 경로 계산 메서드 (교통 상황에 따른 가중치 반영)
    def calculate_optimal_route(self, traffic_conditions):
        """
        최적 경로를 계산합니다.
        각 구간별 거리를 고려하여 교통 상황에 따른 가중치를 적용합니다.
        """
        route = [self.start] + self.stops + [self.end]
        total_distance = 0

        print(f"경로: {route}")
        for i in range(len(route) - 1):
            segment = f"{route[i]}-{route[i + 1]}"
            distance = self.distances.get(route[i], 0)
            traffic_weight = traffic_conditions.get(segment, 1)  # 교통 상황 가중치 적용
            adjusted_distance = distance * traffic_weight
            total_distance += adjusted_distance
            print(f"{segment} 구간: {distance}km (가중치: {traffic_weight}) -> 조정 거리: {adjusted_distance}km")

        print(f"총 최적 경로의 거리: {total_distance}km")
        return total_distance


# TrafficCondition(교통 상황) 클래스
class TrafficCondition:
    def __init__(self):
        self.traffic_data = {}  # 경로별 교통 상황 저장

    # 교통 혼잡도 업데이트 메서드
    def update_traffic(self, route, condition):
        """
        경로의 교통 상황을 업데이트합니다.
        교통 상황은 혼잡도에 따라 1.0 (원활) ~ 3.0 (매우 혼잡)의 가중치를 가집니다.
        """
        self.traffic_data[route] = condition
        print(f"경로 {route}의 교통 상황이 {condition}으로 업데이트되었습니다.")

    # 교통 상황 분석 메서드
    def analyze_traffic(self, route):
        """특정 경로의 교통 상황을 반환합니다."""
        return self.traffic_data.get(route, 1.0)  # 기본적으로 원활(1.0)로 설정

    # 교통 상황에 따른 추천 경로 메서드
    def recommend_route(self, route):
        """교통 상황을 분석하고 경로를 추천합니다."""
        condition = self.analyze_traffic(route)
        if condition > 1.5:
            print(f"경로 {route}가 혼잡하므로 대체 경로를 탐색하는 것이 좋습니다.")
        else:
            print(f"경로 {route}가 원활하므로 이 경로로 진행하는 것이 좋습니다.")


# 시스템 실행 코드 예시

# 차량 생성
my_car = Vehicle("123가4567", "승용차", "서울")

# 차량 정보 출력
print(my_car.vehicle_info())

# 경로 생성
my_route = Route("서울", "부산")
my_route.add_stop("대전", 150)
my_route.add_stop("대구", 120)

# 교통 상황 생성 및 업데이트
traffic = TrafficCondition()
traffic.update_traffic("서울-대전", 1.2)  # 서울-대전 구간이 약간 혼잡
traffic.update_traffic("대전-대구", 1.5)  # 대전-대구 구간이 혼잡
traffic.update_traffic("대구-부산", 1.0)  # 대구-부산 구간이 원활

# 최적 경로 계산
optimal_distance = my_route.calculate_optimal_route(traffic.traffic_data)

# 추천 경로 출력
traffic.recommend_route("서울-대전")
traffic.recommend_route("대전-대구")
traffic.recommend_route("대구-부산")
