# maybe

Toy project implementing Maybe/Just/Nothing

## Usage

```python
from typing import Optional
from .maybe import Maybe


def get_unknown_result() -> Optional[str]:
    return "beautiful"


result = (
    Maybe(get_unknown_result())
    .map(lambda v: v.strip().lower())
    .filter(lambda v: v.isalpha())
    .map(lambda v: f"Hello {v}!")
    .get_or_else("Hello world!")
)

for v in Maybe(get_unknown_result()):
    print(v)

if 10 in Maybe(get_unknown_result()):
    print("Found it!")

```
