import sys
import queue


class Influencer:
    def __init__(self, influencer_id: int, name: str, penetration: int, avoid: list[int]):
        self.id = influencer_id
        self.name = name
        self.penetration = penetration
        self.avoid = avoid


class State:
    def __init__(self, selected: list[Influencer]):
        self.value = get_total_value(selected)
        self.selected = selected
        self.cost = 0

    def __lt__(self, other):
        return self.cost >= other.cost


def get_total_value(selected: list[Influencer]):
    return sum(influencer.penetration for influencer in selected)


def cost_function(selected_influencers, new_influencer, total_influencers):
    return sum(influencer.penetration for influencer in selected_influencers) + new_influencer.penetration * (
            len(total_influencers) - len(selected_influencers))


def generate_next_states(available_states: queue.PriorityQueue, current_state: State, influencers: list[Influencer]):
    for influencer in influencers:
        if influencer not in current_state.selected:
            new_state = State(current_state.selected + [influencer])
            new_state.cost = cost_function(current_state.selected, influencer, influencers)

            available_states.put(new_state)


def limit_function(state: State):
    avoid = set()
    for influencer in state.selected:
        avoid.update(influencer.avoid)

    for influencer in state.selected:
        if influencer.id in avoid:
            return False
    return True


def parse_influencer(line: list[str]):
    return Influencer(int(line[0]), line[1], int(line[2]), [int(i) for i in line[3:]])


def read_influencers(file_name: str):
    influencers = []
    with open(file_name) as file:
        for line in file.readlines():
            influencers.append(parse_influencer(line.split(",")))
    return influencers


def print_result(best_solution: State):
    print("Valor conseguido:", best_solution.value)
    print()
    print(*(influencer.name for influencer in best_solution.selected), sep='\n')


def main(file_name: str):
    influencers = read_influencers(file_name)

    initial_state = State([])
    available_states = queue.PriorityQueue()
    available_states.put(initial_state)
    best_solution = initial_state

    while not available_states.empty():
        current_state = available_states.get()

        if limit_function(current_state):
            if current_state.value > best_solution.value:
                best_solution = current_state

        generate_next_states(available_states, current_state, influencers)

    print_result(best_solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python promocion.py [file]")
    else:
        main(sys.argv[1])
