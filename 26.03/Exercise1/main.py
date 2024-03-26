## 1
# def aggregate_list_values(inputs):
#     dict = {}
#     for tup in inputs:
#         dict[tup[0]] = dict.setdefault(tup[0], 0) + tup[1]
#     print(dict)


# aggregate_list_values([("Apples", 1), ("Banana", 2), ("Apples", 3)])


##2
# def list_intersection(list_1, list_2):
#     return set(list_1).intersection(set(list_2))

# print(list_intersection([1, 2, 3], [2, 3, 4]))


##3
# def merge_dicts(dict_1: dict, dict_2: dict):
#     dict_1.update(dict_2)
#     return dict_1

# print(merge_dicts({"one": 1, "two": 2}, {"two": 3, "three": 3}))


##4
# def count_freq(input: list):
#     return {key: input.count(key) for key in set(input)}


# print(count_freq([1, 2, 3, 2, 1, 1, 1, 2]))


##5
# def nested_dicts(dict_top: dict):
#     for dict_inner in dict_top:
#         dict_top[dict_inner]["key"] = "value"
#     return dict_top


# print(nested_dicts({"dict1": {"one": 1}, "dict2": {"two": 2}}))


##6
# def sort_list_of_tuples(list: list):
#     list.sort(key=lambda person: person[1], reverse=True)
#     return list


# print(sort_list_of_tuples([("john", 22), ("amy", 30), ("adam", 16)]))


##7
# def filter_dict(dict_1: dict, prefix: str):
#     temp = filter(lambda item: item[0].startswith(prefix), dict_1.items())
#     return dict(temp)


# print(filter_dict({"one": 1, "two": 2, "three": 3}, "t"))


##8
# def list_with_condit(input: list):
#     return [v**2 for v in input if v % 2 == 0]


# print(list_with_condit([1, 2, 3, 4, 5, 6]))


##9
# def set_union(set_1: set, set_2: set):
#     return set_1.union(set_2)


# def set_intersection(set_1: set, set_2: set):
#     return set_1.intersection(set_2)


# def set_difference(set_1: set, set_2: set):
#     return set_1.difference(set_2)


# def set_symmetric_difference(set_1: set, set_2: set):
#     return set_1.symmetric_difference(set_2)


# set_1 = {1, 2, 3, 4}
# set_2 = {2, 3, 5, 6}
# print(set_union(set_1, set_2))
# print(set_intersection(set_1, set_2))
# print(set_difference(set_1, set_2))
# print(set_symmetric_difference(set_1, set_2))


##10
# def dict_key_tuples(input: list):
#     return {k: k[0] + k[1] for k in input}


# print(dict_key_tuples([(1, 2), (3, 4), (5, 6)]))


##11
# def dict_average_scores(input: list):
#     return {tup[0]: sum(tup[1:]) / (len(tup[1:])) for tup in input}


# print(dict_average_scores([("John", 2, 2, 2), ("Adam", 4, 6, 8)]))


##12
# def sort_dict(input: list):
#     temp = sorted(input, key=lambda item: item["score"], reverse=True)
#     return temp


# print(
#     sort_dict(
#         [
#             {"name": "John", "score": 10},
#             {"name": "Adam", "score": 12},
#             {"name": "Ben", "score": 16},
#         ]
#     )
# )


##13
# def combine_lists(list_1: list, list_2: list):
#     return dict(zip(list_1, list_2))


# print(combine_lists(["one", "two", "three"], [1, 2, 3]))


##14
# def longest_string(input: list):
#     return sorted(
#         [item for item in input if type(item) == str],
#         key=lambda item: len(item),
#         reverse=True,
#     )[0]


# print(longest_string([1, 2, 3, "one", "wfegfbg", "three"]))


##15
# def encode(input: str):
#     return "".join([item for item in list(input) for _ in range(2)])


# def decode(input: str):
#     return "".join([item for count, item in enumerate(list(input)) if count % 2 == 1])


# encoded = encode("hello")
# print(encoded)
# print(decode(encoded))
