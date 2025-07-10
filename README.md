

# Data Processing Approaches for Large Context

This project demonstrates different approaches to handle large context and data in prompts and processing scenarios. Each approach is implemented as a separate module with its own processing strategy.

## Project Overview

When dealing with large datasets or context that exceeds token limits, different processing strategies are needed. This project implements six distinct approaches to handle such scenarios effectively.

## Project Structure

```
chunking-approaches-project/
├── src/
│   ├── __init__.py
│   ├── main.py                    # Main application with DataProcessingManager
│   ├── approaches/
│   │   ├── __init__.py
│   │   ├── approach1.py          # Chunking Processor
│   │   ├── approach2.py          # Summarization Processor
│   │   ├── approach3.py          # Reference-Based Processor
│   │   ├── approach4.py          # Hierarchical Processor
│   │   ├── approach5.py          # Token-Aware Truncation Processor
│   │   └── approach6.py          # Streaming Processor
│   └── utils/
│       ├── __init__.py
│       └── helpers.py            # Utility functions for formatting and validation
├── data_storage/                 # Created automatically for reference-based storage
├── tests/
│   ├── __init__.py
│   └── test_approaches.py
├── requirements.txt
├── processing_results.json       # Generated after running demos
└── README.md
```

## Approaches Implemented

### 1. **Chunking Approach** (`approach1.py`)
- **Purpose**: Break large data into manageable chunks
- **Best for**: Very large datasets that can be processed in parts
- **Features**: 
  - Text and list chunking
  - Configurable chunk sizes
  - Sequential processing of chunks

### 2. **Summarization Approach** (`approach2.py`)
- **Purpose**: Extract key information and metrics from data
- **Best for**: Data where overview is more important than details
- **Features**:
  - Statistical analysis for numerical data
  - Sample extraction
  - Key metrics calculation

### 3. **Reference-Based Approach** (`approach3.py`)
- **Purpose**: Store large data externally and use references
- **Best for**: Data that needs to be accessed multiple times
- **Features**:
  - File-based storage with hash IDs
  - JSON serialization
  - Reference retrieval system

### 4. **Hierarchical Approach** (`approach4.py`)
- **Purpose**: Process data in multiple stages (overview → details)
- **Best for**: Complex data requiring multi-level analysis
- **Features**:
  - High-level overview analysis
  - Detailed section processing
  - Importance-based section identification

### 5. **Token-Aware Truncation** (`approach5.py`)
- **Purpose**: Smart truncation preserving important information
- **Best for**: Data slightly above token limits
- **Features**:
  - Token counting
  - Beginning/end preservation
  - Middle section summarization

### 6. **Streaming Approach** (`approach6.py`)
- **Purpose**: Iterative processing with context management
- **Best for**: Real-time or continuous data processing
- **Features**:
  - Context accumulation
  - Incremental processing
  - Memory-efficient streaming

## Setup Instructions

1. **Clone or download** the project files to your local machine

2. **Navigate to the project directory**:
   ```bash
   cd chunking-approaches-project
   ```

3. **Install dependencies** (if any are added to requirements.txt):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Demo
Run the full demonstration with all approaches:
```bash
python src/main.py
```

### Interactive Testing
Test individual approaches interactively:
```bash
python src/main.py test
```

### From Different Directories
If running from the project root:
```bash
python src/main.py
```

If running from the src directory:
```bash
cd src
python main.py
```

## Example Output

The application will demonstrate each approach with different data sizes:

```
=== Data Processing Approaches Demo ===

Available approaches: ['chunking', 'summarization', 'reference', 'hierarchical', 'truncation', 'streaming']

--- Processing Small Data ---
Data characteristics: {'type': 'str', 'size': 34, 'complexity': 'low'}
Recommended approach: No processing needed - data is small

--- Processing Medium Data ---
Data characteristics: {'type': 'list', 'size': 2950, 'complexity': 'medium'}
Recommended approach: chunking

--- CHUNKING APPROACH ---
Method: chunking
Original size: 2950 characters
Total chunks: 3
```

## Key Features

- **Automatic Approach Recommendation**: Based on data size and characteristics
- **Comprehensive Error Handling**: Graceful failure with detailed error messages
- **Result Persistence**: Automatically saves results to JSON file
- **Flexible Data Support**: Handles strings, lists, dictionaries, and mixed data
- **Modular Design**: Easy to extend with new approaches
- **Interactive Mode**: Test specific approaches with custom data

## File Descriptions

| File | Purpose |
|------|---------|
| `main.py` | Central application with DataProcessingManager class |
| `approach1.py` | ChunkingProcessor - splits data into manageable pieces |
| `approach2.py` | SummarizationProcessor - extracts key information |
| `approach3.py` | ReferenceBasedProcessor - external storage with references |
| `approach4.py` | HierarchicalProcessor - multi-stage analysis |
| `approach5.py` | TokenAwareTruncationProcessor - smart text truncation |
| `approach6.py` | StreamingProcessor - iterative processing |
| `helpers.py` | Utility functions for validation, formatting, and file operations |

## Extending the Project

To add a new approach:

1. Create `approach7.py` in the `approaches/` directory
2. Implement a processor class with a main processing method
3. Add the import to `approaches/__init__.py`
4. Update the processors dictionary in `main.py`
5. Add the method mapping in `process_with_approach()`

## Testing

Run tests (when implemented):
```bash
pytest tests/test_approaches.py
```

## Output Files

- `processing_results.json`: Contains results from demo runs
- `data_storage/`: Directory for reference-based storage files

## Requirements

- Python 3.6+
- No external dependencies required for basic functionality
- Standard library modules: `json`, `os`, `hashlib`, `statistics`, `typing`

## Use Cases

This project is ideal for:
- **AI/ML Applications**: Handling large prompts or datasets
- **Data Processing Pipelines**: Choosing optimal processing strategies
- **Text Analysis**: Managing large documents or corpora
- **API Development**: Implementing different data handling strategies
- **Educational Purposes**: Learning different data processing patterns

## Contributing

Feel free to:
- Add new processing approaches
- Improve existing algorithms
- Enhance error handling
- Add more comprehensive tests
- Improve documentation

Each approach demonstrates a different strategy for handling large data, making this project a comprehensive toolkit for data processing challenges.
```