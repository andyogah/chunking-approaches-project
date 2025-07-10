# File: /python-approaches-project/python-approaches-project/src/approaches/__init__.py


from .approach1 import ChunkingProcessor
from .approach2 import SummarizationProcessor
from .approach3 import ReferenceBasedProcessor
from .approach4 import HierarchicalProcessor
from .approach5 import TokenAwareTruncationProcessor
from .approach6 import StreamingProcessor

__all__ = [
    'ChunkingProcessor',
    'SummarizationProcessor', 
    'ReferenceBasedProcessor',
    'HierarchicalProcessor',
    'TokenAwareTruncationProcessor',
    'StreamingProcessor'
]