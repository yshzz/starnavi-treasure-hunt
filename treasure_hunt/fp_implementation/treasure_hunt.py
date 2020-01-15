from .utils import list_output_to_str


@list_output_to_str
def find_treasure(treasure_map):
    """Forms treasure path from a treasure map.

    Args:
        treasure_map (:obj:`list` of :obj:`int`): Map to explore for a treasure.

    Returns:
        :obj:`str`: Treasure path.

    Raises:
        :class:`ValueError`: If treasure was not found.
    """

    def get_treasure_path(n=1, curr_row=1, curr_col=1):
        if n > len(treasure_map) ** 2:
            raise ValueError('Treasure not found')

        cell_val = treasure_map[curr_row - 1][curr_col - 1]
        cell_coordinates = curr_row * 10 + curr_col
        res = [cell_coordinates]

        if cell_val == cell_coordinates:
            return res

        n += 1
        next_row, next_col = divmod(cell_val, 10)
        return res + get_treasure_path(n=n, curr_row=next_row,
                                       curr_col=next_col)

    return get_treasure_path()
