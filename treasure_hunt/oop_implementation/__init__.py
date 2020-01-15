from .treasure_hunt import TreasureHunt


def find_treasure(treasure_map):
    """Forms treasure path from a treasure map.

    Args:
        treasure_map (:obj:`list` of :obj:`int`): Map to explore for a treasure.

    Returns:
        :obj:`str`: Treasure path.

    Raises:
        :class:`ValueError`: If treasure was not found.
    """

    return TreasureHunt(treasure_map).get_treasure_path()
