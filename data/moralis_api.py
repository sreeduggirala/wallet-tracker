from dotenv import load_dotenv
from moralis import evm_api
import os


class MoralisAPI:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("MORALIS_API_KEY")

    def get_pnl_breakdown(self, address: str, chain: str) -> dict:
        params = {
            "address": address,
            "chain": chain,
        }

        return evm_api.wallets.get_wallet_profitability(
            api_key=os.getenv("MORALIS_API_KEY"),
            params=params,
        )

    def get_net_worth(self, address: str) -> float:
        params = {
            "exclude_spam": True,
            "exclude_unverified_contracts": False,
            "address": address,
        }

        result = evm_api.wallets.get_wallet_net_worth(
            api_key=os.getenv("MORALIS_API_KEY"),
            params=params,
        )

        return float(result.total_networth_usd)

    def get_win_rate(self, address: str, chain: str) -> float:
        pnl_breakdown = self.get_pnl_breakdown(address, chain)
        # print(pnl_breakdown["result"][0])
        wins = 0
        i = 0
        while i < len(pnl_breakdown["result"]):
            if pnl_breakdown["result"][i]["realized_profit_percentage"] > 0:
                wins += 1
            i += 1

        return wins / len(pnl_breakdown["result"])

    def get_native_balance(self, address: str, chain: str) -> dict:
        params = {
            "address": address,
            "chain": chain,
        }

        result = evm_api.balance.get_native_balance(
            api_key=os.getenv("MORALIS_API_KEY"),
            params=params,
        )

        return result.balance

    def get_erc20_balances(self, address: str, chain: str) -> dict:
        params = {
            "address": address,
            "chain": chain,
        }

        return evm_api.token.get_wallet_token_balances(
            api_key=os.getenv("MORALIS_API_KEY"),
            params=params,
        )

    def get_erc20_transfers(self, address: str, chain: str) -> dict:
        params = {
            "address": address,
            "chain": chain,
        }

        return evm_api.token.get_wallet_token_transfers(
            api_key=os.getenv("MORALIS_API_KEY"),
            params=params,
        )

    def get_ens_by_address(self, address: str) -> str:

        params = {"address": address}

        result = evm_api.resolve.resolve_address(
            api_key=os.getenv("MORALIS_API_KEY"),
            params=params,
        )

        return result.name

    def get_address_by_ens(self, domain: str) -> str:
        params = {
            "domain": domain,
        }

        result = evm_api.resolve.resolve_e_n_s_domain(
            api_key=os.getenv("MORALIS_API_KEY"),
            params=params,
        )

        return result.address
