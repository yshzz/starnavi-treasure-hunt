class TreasureHunt:
    """Treasure Hunt class.

    Args:
        treasure_map (:obj:`list` of :obj:`int`): Map to explore for a treasure.
        start_row_col (:obj:`tuple` of :obj:`int`): Starting point in the search.
    """

    def __init__(self, treasure_map, start_row_col=(1, 1)):
        self.treasure_map = treasure_map
        self._curr_row, self._curr_col = start_row_col

    @property
    def _cell_val(self):
        return self.treasure_map[self._curr_row - 1][self._curr_col - 1]

    @property
    def _cell_coordinates(self):
        return self._curr_row * 10 + self._curr_col

    @staticmethod
    def list_to_str(data):
        return ' '.join(map(str, data))

    def _get_next_row_col(self):
        return divmod(self._cell_val, 10)

    def get_treasure_path(self):
        """Forms treasure path from a treasure map.

        Returns:
            :obj:`str`: Treasure path.

        Raises:
            :class:`ValueError`: If treasure was not found.
        """

        res = list()

        for _ in range(len(self.treasure_map) ** 2):
            res.append(self._cell_coordinates)

            if self._cell_val == self._cell_coordinates:
                return self.list_to_str(res)

            self._curr_row, self._curr_col = self._get_next_row_col()

        raise ValueError('Treasure not found')
