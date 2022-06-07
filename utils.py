import json

from config import json_path


def load_candidates_from_json():
    """
    возвращает список всех кандидатов
    :return:dict
    """

    path = json_path
    with open(path, "r", encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_candidate(candidate_id):
    """
    возвращает одного кандидата по его id
    :param candidate_id:
    :return:dict
    """
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """
    возвращает кандидатов по имени
    :param candidate_name:
    :return:dict
    """
    candidates_names = []
    candidates = load_candidates_from_json()

    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            candidates_names.append(candidate)
    return candidates_names


def get_candidates_by_skill(skill_name):
    """
    возвращает кандидатов по навыку
    :param skill_name:
    :return:
    """
    skilled_candidates = []
    candidates = load_candidates_from_json()

    for candidate in candidates:
        skills = candidate["skills"].lower().strip().split(", ")
        if skill_name in skills:
            skilled_candidates.append(candidate)
    return skilled_candidates



