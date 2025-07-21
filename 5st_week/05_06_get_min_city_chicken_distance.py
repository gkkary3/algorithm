import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]

# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시키려 한다. 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 반환하시오.
# 여러 개 중 M 개를 골라야 한다 ->
# 그 치킨 거리가 가장 적게 되는 경우 -< 모든 경우의 수를 다 봐야 한다.

def get_min_city_chicken_distance(n, m, city_map):
    chicken_location_list = []
    home_location_list = []

    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                home_location_list.append([i,j])
            elif city_map[i][j] == 2:
                chicken_location_list.append([i, j])
    print('home_location_list',home_location_list, 'chicken_location_list ', chicken_location_list)
    chicken_location_m_combinations = list(itertools.combinations(chicken_location_list, m))
    # print("chicken_location_m_combinations ", list(chicken_location_m_combinations))
    min_distance_of_m_combinations = sys.maxsize
    for chicken_location_m_combination in chicken_location_m_combinations:
        chicken_location_m_combination_total_chicken_distance = 0
        print("chicken_location_m_combination is ", chicken_location_m_combination)
        for home_r, home_c in home_location_list:
            min_home_chicken_distance = sys.maxsize
            print("home_r, home_c is ", home_r, home_c)

            # 각 집의 관점에서 발생할 수 있는 치킨 거리
            for chicken_location in chicken_location_m_combination:
                min_home_chicken_distance =   min (
                    min_home_chicken_distance,
                    abs(home_r - chicken_location[0]) + abs(home_c - chicken_location[1]))

                print("min_home_chicken_distance is ", min_home_chicken_distance, "combination is", chicken_location )
            chicken_location_m_combination_total_chicken_distance += min_home_chicken_distance

        min_distance_of_m_combinations = min(
            min_distance_of_m_combinations, chicken_location_m_combination_total_chicken_distance)
    return min_distance_of_m_combinations


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!


city_map = [
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0]
]
print("정답 = 11 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,1,city_map))


city_map = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2]
]
print("정답 = 10 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,2,city_map))