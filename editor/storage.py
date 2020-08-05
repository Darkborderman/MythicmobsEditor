"""Mythicmobs yml data in-memory storage"""
from components.utils import load_folder_yml, load_skills
from config import Config

# Use category and item name as a pair to search currently editing item
FOCUSED_CATEGORY = ""
FOCUSED_NAME = ""
STORAGE = {
    "DropTables": dict(),
    "Enchantments": dict(),
    "Items": dict(),
    "Mobs": dict(),
    "RandomSpawns": dict(),
    "Skills": list(),
    "Miscs": dict(),
}


def init_storage():
    """Initialize in-memory storage"""
    # STORAGE["DropTables"].update(
    #     load_folder_yml(f"{Config.MYTHICMOBS_FOLDER}/DropTables")
    # )
    # STORAGE["Enchantments"].update(
    #     load_folder_yml(f"{Config.MYTHICMOBS_FOLDER}/Enchantments")
    # )
    # STORAGE["Items"].update(load_folder_yml(f"{Config.MYTHICMOBS_FOLDER}/Items"))
    # STORAGE["Mobs"].update(load_folder_yml(f"{Config.MYTHICMOBS_FOLDER}/Mobs"))
    # STORAGE["RandomSpawns"].update(
    #     load_folder_yml(f"{Config.MYTHICMOBS_FOLDER}/RandomSpawns")
    # )
    # STORAGE["Mobs"] = load_mobs()
    STORAGE["Skills"] = load_skills()
    # STORAGE['Mobs'].update(load_folder_yml('./Mobs'))


def get_focused_item() -> dict:
    """Retrieve currently editing object"""
    try:
        for item in STORAGE[FOCUSED_CATEGORY]:
            if item.unique_id == FOCUSED_NAME:
                return item
    except Exception as error:
        print(error)
        return {"warning": "No item selected"}


def get_focused_name() -> str:
    """Retrieve currently editing item name"""
    return FOCUSED_NAME


def set_focused_item(category: str, name: str) -> None:
    """Set item that is currently editing by updateing category and item name pair

    Args:
        category (str): item category(ex: `enchantment`)
        name (str): item name(ex: `KNOCKBACK`)
    """
    globals().__setitem__("FOCUSED_CATEGORY", category)
    globals().__setitem__("FOCUSED_NAME", name)
