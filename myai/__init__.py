from .client import MyAIClient, Client

# Optional extras: `import myai` must work on a base install (httpx only).
try:
    from .auth.wallet_auth import WalletAuth  # needs: pip install 'myai-sdk[wallet]'
except ImportError:  # pragma: no cover
    WalletAuth = None  # type: ignore
from .exceptions import InsufficientFundsError, NoProvidersError, PoCFailedError
try:
    from .openai_compat import MyAi, AsyncMyAi  # needs: pip install 'myai-sdk[openai]'
except ImportError:  # pragma: no cover
    MyAi = AsyncMyAi = None  # type: ignore

__version__ = "2.2.1"
__all__ = [
    # OpenAI-compatible
    "MyAi", "AsyncMyAi",
    # Agentic commerce
    "MyAIClient", "Client",
    # Wallet auth (v2.2)
    "WalletAuth",
    # Exceptions
    "InsufficientFundsError", "NoProvidersError", "PoCFailedError",
]
