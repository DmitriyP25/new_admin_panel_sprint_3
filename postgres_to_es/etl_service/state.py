import abc
import json
import os
from typing import Any, Dict, Optional


class BaseStorage(abc.ABC):
    """Abstract base storage."""

    @abc.abstractmethod
    def save_state(self, state: Dict[str, Any]) -> None:
        """Save state in storage."""

    @abc.abstractmethod
    def get_state(self) -> Dict[str, Any]:
        """Get state from storage."""


class JsonFileStorage(BaseStorage):
    """Storage that save state in JSON file."""

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def save_state(self, state: Dict[str, Any]) -> None:
        """Save state in JSON storage."""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(state, file, ensure_ascii=False, indent=4)

    def get_state(self, key, default: Optional[str] = None) -> str:
        """Get state from JSON storage."""
        with open(self.file_path, 'r') as file:
            if os.path.getsize(self.file_path):
                json_data = json.load(file)
                if json_data:
                    return json_data[key]
            return default
