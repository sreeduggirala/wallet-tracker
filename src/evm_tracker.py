from dotenv import load_dotenv
from moralis import evm_api
import os

load_dotenv()
# api_key = os.getenv("MORALIS_API_KEY")


def get_pnl_breakdown(address: str, chain: str) -> dict:
    params = {
        "address": address,
        "chain": chain,
    }

    return evm_api.wallets.get_wallet_profitability(
        api_key=os.getenv("MORALIS_API_KEY"),
        params=params,
    )


def get_net_worth(address: str) -> dict:
    params = {
        "exclude_spam": True,
        "exclude_unverified_contracts": False,
        "address": address,
    }

    result = evm_api.wallets.get_wallet_net_worth(
        api_key=os.getenv("MORALIS_API_KEY"),
        params=params,
    )

    return result.total_networth_usd


def get_win_rate(address: str, chain: str) -> dict:
    # pnl_breakdown = get_pnl_breakdown(address, chain)
    # logic to calculate win rate
    pass


def get_native_balance(address: str, chain: str) -> dict:
    params = {
        "address": address,
        "chain": chain,
    }

    result = evm_api.balance.get_native_balance(
        api_key=os.getenv("MORALIS_API_KEY"),
        params=params,
    )

    return result.balance


def get_erc20_balances(address: str, chain: str) -> dict:
    params = {
        "address": address,
        "chain": chain,
    }

    return evm_api.token.get_wallet_token_balances(
        api_key=os.getenv("MORALIS_API_KEY"),
        params=params,
    )


def get_erc20_transfers(address: str, chain: str) -> dict:
    params = {
        "address": address,
        "chain": chain,
    }

    return evm_api.token.get_wallet_token_transfers(
        api_key=os.getenv("MORALIS_API_KEY"),
        params=params,
    )


def get_ens_by_address(address: str) -> dict:
    params = {"address": address}

    result = evm_api.resolve.resolve_address(
        api_key=os.getenv("MORALIS_API_KEY"),
        params=params,
    )

    return result.name


def get_address_by_ens(domain: str) -> str:
    params = {
        "domain": domain,
    }

    result = evm_api.resolve.resolve_e_n_s_domain(
        api_key=os.getenv("MORALIS_API_KEY"),
        params=params,
    )

    return result.address
