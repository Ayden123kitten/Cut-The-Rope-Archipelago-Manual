from typing import Optional, Any
from BaseClasses import MultiWorld


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    from ..Helpers import get_option_value

    if category_name == "Box 1":
        return get_option_value(multiworld, player, "Boxes") >= 1
    if category_name == "Box 2":
        return get_option_value(multiworld, player, "Boxes") >= 2
    if category_name == "Box 3":
        return get_option_value(multiworld, player, "Boxes") >= 3
    if category_name == "Box 4":
        return get_option_value(multiworld, player, "Boxes") >= 4
    if category_name == "Box 5":
        return get_option_value(multiworld, player, "Boxes") >= 5
    if category_name == "Box 6":
        return get_option_value(multiworld, player, "Boxes") >= 6
    if category_name == "Box 7":
        return get_option_value(multiworld, player, "Boxes") >= 7
    if category_name == "Box 8":
        return get_option_value(multiworld, player, "Boxes") >= 8
    if category_name == "Box 9":
        return get_option_value(multiworld, player, "Boxes") >= 9
    if category_name == "Box 10":
        return get_option_value(multiworld, player, "Boxes") >= 10
    if category_name == "Box 11":
        return get_option_value(multiworld, player, "Boxes") >= 11
    if category_name == "Box 12":
        return get_option_value(multiworld, player, "Boxes") >= 12
    if category_name == "Box 13":
        return get_option_value(multiworld, player, "Boxes") >= 13
    if category_name == "Box 14":
        return get_option_value(multiworld, player, "Boxes") >= 14
    if category_name == "Box 15":
        return get_option_value(multiworld, player, "Boxes") >= 15
    if category_name == "Box 16":
        return get_option_value(multiworld, player, "Boxes") >= 16
    if category_name == "Box 17":
        return get_option_value(multiworld, player, "Boxes") >= 17

    if category_name == "Star Unlocks - Progressive Per Level":
        return get_option_value(multiworld, player, "Boxes") == 2

    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
