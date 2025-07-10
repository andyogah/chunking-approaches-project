import json
from typing import Any, Dict

def format_result_output(result: Dict[str, Any], approach_name: str) -> str:
    """Format processing results for clean output display"""
    output = f"\n--- {approach_name.upper()} APPROACH ---\n"
    output += f"Method: {result.get('method', 'unknown')}\n"
    
    if 'original_size' in result:
        output += f"Original size: {result['original_size']} characters\n"
    
    if 'total_chunks' in result:
        output += f"Total chunks: {result['total_chunks']}\n"
    
    if 'summary' in result:
        output += f"Summary: {json.dumps(result['summary'], indent=2)}\n"
    
    if 'error' in result:
        output += f"ERROR: {result['error']}\n"
    
    return output

def validate_data_input(data: Any) -> bool:
    """Validate if data is suitable for processing"""
    if data is None:
        return False
    if isinstance(data, (str, list, dict)):
        return len(str(data)) > 0
    return True

def get_data_characteristics(data: Any) -> Dict[str, Any]:
    """Analyze data characteristics for approach recommendation"""
    return {
        'type': type(data).__name__,
        'size': len(str(data)),
        'is_list': isinstance(data, list),
        'is_string': isinstance(data, str),
        'is_dict': isinstance(data, dict),
        'complexity': 'high' if len(str(data)) > 10000 else 'medium' if len(str(data)) > 1000 else 'low'
    }

def save_results_to_file(results: Dict[str, Any], filename: str = "processing_results.json") -> str:
    """Save processing results to a JSON file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, default=str)
        return f"Results saved to {filename}"
    except Exception as e:
        return f"Error saving results: {str(e)}"

def load_sample_data(data_type: str = "mixed") -> Any:
    """Generate sample data for testing different approaches"""
    if data_type == "small":
        return "This is a small piece of text for testing."
    elif data_type == "medium":
        return ["Item " + str(i) + " with some description text" for i in range(50)]
    elif data_type == "large":
        return "This is a very long text piece that will be repeated many times. " * 500
    elif data_type == "mixed":
        return {
            "text_data": "Sample text content",
            "list_data": [f"item_{i}" for i in range(20)],
            "nested_data": {"key1": "value1", "key2": ["a", "b", "c"]},
            "large_text": "Large content section. " * 100
        }
    else:
        return "Default sample data"