def minha_lista(input_list):
    if len(input_list) == 0:
        return []
    else:
        return [input_list[-1]] + minha_lista(input_list[:-1])


print(minha_lista([1, 2, 3, 4, 5]))
