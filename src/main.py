import sys
import os

# Add the src directory to the Python path to ensure imports work
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, current_dir)
sys.path.insert(0, parent_dir)

try:
    from approaches import (
        ChunkingProcessor,
        SummarizationProcessor,
        ReferenceBasedProcessor,
        HierarchicalProcessor,
        TokenAwareTruncationProcessor,
        StreamingProcessor
    )
    from utils import (
        format_result_output,
        validate_data_input,
        get_data_characteristics,
        save_results_to_file,
        load_sample_data
    )
except ImportError as e:
    print(f"Import error: {e}")
    print("Current working directory:", os.getcwd())
    print("Python path:", sys.path)
    print("Files in current directory:", os.listdir('.'))
    if os.path.exists('approaches'):
        print("Files in approaches directory:", os.listdir('approaches'))
    if os.path.exists('utils'):
        print("Files in utils directory:", os.listdir('utils'))
    raise

class DataProcessingManager:
    def __init__(self):
        self.processors = {
            'chunking': ChunkingProcessor(),
            'summarization': SummarizationProcessor(),
            'reference': ReferenceBasedProcessor(),
            'hierarchical': HierarchicalProcessor(),
            'truncation': TokenAwareTruncationProcessor(),
            'streaming': StreamingProcessor()
        }
    
    def process_with_approach(self, data, approach_name):
        """Process data using specified approach"""
        if not validate_data_input(data):
            raise ValueError("Invalid data input")
            
        if approach_name not in self.processors:
            raise ValueError(f"Unknown approach: {approach_name}. Available: {list(self.processors.keys())}")
        
        processor = self.processors[approach_name]
        
        # Method mapping for cleaner code
        method_mapping = {
            'chunking': processor.process_large_data_in_chunks,
            'summarization': processor.process_with_summarization,
            'reference': processor.process_with_reference,
            'hierarchical': processor.process_hierarchically,
            'truncation': processor.process_with_truncation,
            'streaming': processor.iterative_processing
        }
        
        return method_mapping[approach_name](data)
    
    def process_with_all_approaches(self, data):
        """Process data with all available approaches"""
        if not validate_data_input(data):
            return {"error": "Invalid data input"}
            
        results = {}
        for approach_name in self.processors.keys():
            try:
                results[approach_name] = self.process_with_approach(data, approach_name)
            except Exception as e:
                results[approach_name] = {"error": str(e)}
        return results
    
    def recommend_approach(self, data):
        """Recommend best approach based on data characteristics"""
        try:
            characteristics = get_data_characteristics(data)
            data_size = characteristics['size']
            
            if data_size < 500:
                return "No processing needed - data is small"
            elif data_size < 2000:
                return "summarization"
            elif data_size < 10000:
                return "chunking"
            else:
                return "streaming"
        except Exception as e:
            print(f"Error in recommendation: {e}")
            return "chunking"  # Default fallback
    
    def get_available_approaches(self):
        """Get list of available approaches"""
        return list(self.processors.keys())

def main():
    """Main function to demonstrate all approaches"""
    try:
        # Initialize the manager
        manager = DataProcessingManager()
        
        # Test with sample data from helpers
        test_cases = [
            ("Small Data", load_sample_data("small")),
            ("Medium Data", load_sample_data("medium")),
            ("Large Data", load_sample_data("large")),
            ("Mixed Data", load_sample_data("mixed"))
        ]
        
        print("=== Data Processing Approaches Demo ===\n")
        print(f"Available approaches: {manager.get_available_approaches()}\n")
        
        all_results = {}
        
        for name, data in test_cases:
            print(f"--- Processing {name} ---")
            
            try:
                characteristics = get_data_characteristics(data)
                print(f"Data characteristics: {characteristics}")
                
                recommendation = manager.recommend_approach(data)
                print(f"Recommended approach: {recommendation}")
                
                # Process with recommended approach
                if recommendation != "No processing needed - data is small":
                    result = manager.process_with_approach(data, recommendation)
                    print(format_result_output(result, recommendation))
                    all_results[name] = result
                else:
                    print("Data is small enough - no processing needed")
                    all_results[name] = {"method": "no_processing", "reason": "data_too_small"}
                    
            except Exception as e:
                print(f"Error processing {name}: {str(e)}")
                all_results[name] = {"error": str(e)}
            
            print("-" * 50)
        
        # Save results to file
        if all_results:
            save_message = save_results_to_file(all_results)
            print(f"\n{save_message}")
        else:
            print("\nNo results to save.")
            
    except ImportError as e:
        print(f"Import error: {e}")
        print("Make sure all approach files and utils files are properly created.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def test_single_approach():
    """Test a single approach interactively"""
    try:
        manager = DataProcessingManager()
        
        print("Available approaches:", manager.get_available_approaches())
        approach = input("Enter approach name: ").strip()
        
        if approach not in manager.get_available_approaches():
            print(f"Invalid approach. Choose from: {manager.get_available_approaches()}")
            return
        
        print("Available data types: small, medium, large, mixed")
        data_type = input("Enter data type: ").strip()
        
        data = load_sample_data(data_type)
        result = manager.process_with_approach(data, approach)
        print(format_result_output(result, approach))
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_single_approach()
    else:
        main()