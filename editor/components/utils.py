import os

import yaml

from config import Config
from classes.skill import MythicSkill


def load_folder_yml(path: str) -> dict:
    """
        Load yml under the specific folders, and search recursively
        return dictionary of parsed item
    """
    result = {}
    for root, _, files in os.walk(path):
        for file in files:
            filename, filetype = file.split(".")
            if filetype == "yml":
                with open(f"{root}/{filename}.{filetype}") as infile:
                    result.update(yaml.safe_load(infile.read()))
        return result

def load_skills():
    skills = []
    key: str
    value: dict
    for key, value in load_folder_yml(f"{Config.MYTHICMOBS_FOLDER}/Skills").items():
        data_dict = {
            'unique_id': key,
            'cooldown': value['Cooldown'] if 'Cooldown' in value else '',
            'skills': value['Skills'] if 'Skills' in value else ''
        }
        skills.append(MythicSkill(**data_dict))
    return skills

# def load_mobs():
#     mobs = []
#     key: str
#     value: dict
#     for key, value in load_folder_yml(f"{Config.MYTHICMOBS_FOLDER}/Mobs").items():
#         mob_data = {
#             'unique_id': key,
#             'mob_type': value['Type'] if 'Type' in value else '',
#             'display': value['Display'] if 'Display' in  value else '',
#         }
#         mobs.append(MythicMob(**mob_data))
#     return mobs
