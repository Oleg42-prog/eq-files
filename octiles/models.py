import os
from dataclasses import dataclass
from typing import Self


@dataclass
class DiffResult:
    removed: list
    new: list
    equals: dict
    unequals: dict

    @classmethod
    def create_empty(cls) -> Self:
        return cls(
            removed=[],
            new=[],
            equals={},
            unequals={}
        )

    def __str__(self) -> str:
        return self.pretty(verbose=False)

    def pretty(self, verbose: bool = False, max_items: int = 10) -> str:
        def shorten_path(path: str) -> str:
            if verbose:
                return path
            dirname, basename = os.path.split(path)
            parent = os.path.basename(dirname)
            return os.path.join(parent, basename) if parent else basename

        def format_list(lst: list, label: str, icon: str) -> str:
            if not lst:
                return f"{icon} {label} (0): (empty)"
            lines = [f"{icon} {label} ({len(lst)}):"]
            count = 0
            for item in lst:
                if count >= max_items:
                    lines.append(f"  ... and {len(lst) - max_items} more")
                    break
                lines.append(f"  - {shorten_path(item)}")
                count += 1
            return "\n".join(lines)

        def format_dict(dct: dict, label: str, icon: str) -> str:
            if not dct:
                return f"{icon} {label} (0): (empty)"
            lines = [f"{icon} {label} ({len(dct)}):"]
            count = 0
            for key, (path_a, path_b) in dct.items():
                if count >= max_items:
                    lines.append(f"  ... and {len(dct) - max_items} more")
                    break
                lines.append(f"  {key} ->")
                lines.append(f"    A: {shorten_path(path_a)}")
                lines.append(f"    B: {shorten_path(path_b)}")
                count += 1
            return "\n".join(lines)

        parts = [
            format_list(self.removed, "Removed", "🗑️"),
            format_list(self.new, "New", "✨"),
            format_dict(self.equals, "Equals", "✅"),
            format_dict(self.unequals, "Unequals", "❌"),
        ]
        return "\n".join(parts)
