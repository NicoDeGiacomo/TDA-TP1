class Influencer:
    def __init__(self, id, name, penetration, avoid):
        self.id = id
        self.name = name
        self.penetration = penetration
        self.avoid = avoid


class State:
    def __init__(self, selected):
        self.value = get_total_value(selected)
        self.selected = selected
        self.cost = 0


def main():
    influencers = []
    with open('influencers.txt') as file:
        for line in file.readlines():
            influencers.append(parse_influencer(line.split(",")))

    initial_state = State([])
    available_states = [initial_state]

    best_solution = initial_state
    while available_states:
        available_states.sort(key=lambda x: x.cost)
        current_state = available_states.pop()

        if limit_function(current_state):
            if current_state.value > best_solution.value:
                best_solution = current_state

        available_states.extend(get_next_states(current_state, influencers))

    print(best_solution.value, [influencer.id for influencer in best_solution.selected])


def is_valid(influencer, selected):
    for code in selected:
        if code in influencer.avoid:
            return False
    return True


def parse_influencer(line):
    return Influencer(int(line[0]), line[1], int(line[2]), [int(i) for i in line[3:]])


def cost_function(selected, new_influencer, total_influencers):
    max_influencers = len(total_influencers)
    return sum([influencer.penetration for influencer in selected]) + new_influencer.penetration * (
            max_influencers - len(selected))


def get_total_value(state):
    return sum([influencer.penetration for influencer in state])


def limit_function(state):
    for influencer1 in state.selected:
        for influencer2 in state.selected:
            if influencer1.id in influencer2.avoid:
                return False
    return True


def get_next_states(state, influencers):
    next_states = []
    for influencer in influencers:
        if influencer not in state.selected:
            new_state = State(state.selected + [influencer])
            new_state.cost = cost_function(state.selected, influencer, influencers)
            next_states.append(new_state)
    return next_states


if __name__ == '__main__':
    main()

# TODO: Imprimir bien el resultado
# TODO: Calcular complejidad temporal y espacial
# TODO: Dejar el codigo mas limpio
# Algoritmo: Best-first search
# Function costo (aproximacion): Suma de penetraciones de los influencers seleccionados + penetracion del influencer a agregar * (cantidad de influencers - cantidad de influencers seleccionados)
# Funcion limite: No hay dos influencers que no puedan trabajar juntos
