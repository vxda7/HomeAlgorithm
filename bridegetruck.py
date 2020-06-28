def solution(bridge_length, weight, truck_weights):
    arrive_truck = []
    on_bridge = []
    num_of_trucks = len(truck_weights)
    time = 0
    while len(arrive_truck) != num_of_trucks:
        time += 1
        bridge_weights = sum(on_bridge)
        if bridge_weights + truck_weights[0] < weight:
            on_bridge.append(truck_weights.pop(0))
    return time


print(solution(2,	10,	[7, 4, 5, 6],	8))
