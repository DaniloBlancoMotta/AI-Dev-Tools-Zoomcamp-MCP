import hashlib
from src.core.interfaces import MathServiceInterface, UtilityServiceInterface

class BasicUtilityService(MathServiceInterface, UtilityServiceInterface):
    def add(self, a: int, b: int) -> int:
        return a + b

    def hash_text(self, text: str) -> str:
        return hashlib.sha256(text.encode()).hexdigest()
