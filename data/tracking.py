class Tracking:
    def __init__(self):
        self.tracking = []  # wallets being copytraded - confirmed profitable
        self.watchlist = []  # wallets of interest, but not being copytraded

    def add_address(self, address: str) -> None:
        if address not in self.tracking:
            self.tracking.append(address)

    def remove_address(self, address: str) -> None:
        if address in self.tracking:
            self.tracking.remove(address)
