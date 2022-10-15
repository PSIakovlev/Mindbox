def count_buyers(n_customers: int) -> dict:
    result = {}
    for id in range(n_customers):
        number_group = sum(map(int, str(id)))
        if number_group not in result:
            result[number_group] = 0
        result[number_group] += 1
    return result


def count_buyers_in_range(first_id: int, n_customers: int) -> dict:
    result = {}
    for id in range(first_id, first_id + n_customers):
        number_group = sum(map(int, str(id)))
        if number_group not in result:
            result[number_group] = 0
        result[number_group] += 1
    return result

