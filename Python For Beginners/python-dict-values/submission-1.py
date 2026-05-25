from typing import Dict, List

# def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
#     return list(age_dict.values())

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    values = age_dict.values()
    return list(values)

# do not modify below this line
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))
