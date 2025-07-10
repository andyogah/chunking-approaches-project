import statistics

class SummarizationProcessor:
    def __init__(self, max_sample_size=5):
        self.max_sample_size = max_sample_size
    
    def calculate_metrics(self, data):
        """Calculate key metrics from data"""
        if isinstance(data, list):
            if all(isinstance(x, (int, float)) for x in data):
                return {
                    "count": len(data),
                    "mean": statistics.mean(data),
                    "median": statistics.median(data),
                    "min": min(data),
                    "max": max(data)
                }
            else:
                return {
                    "count": len(data),
                    "types": list(set(type(x).__name__ for x in data))
                }
        elif isinstance(data, str):
            return {
                "length": len(data),
                "word_count": len(data.split()),
                "unique_chars": len(set(data))
            }
        else:
            return {
                "type": type(data).__name__,
                "string_length": len(str(data))
            }
    
    def get_sample_data(self, data):
        """Get sample records from the data"""
        if isinstance(data, list):
            sample_size = min(self.max_sample_size, len(data))
            return data[:sample_size]
        elif isinstance(data, str):
            return data[:200] + "..." if len(data) > 200 else data
        else:
            return str(data)[:200]
    
    def summarize_data(self, large_dataset):
        """Summarize large dataset into key information"""
        summary = {
            "total_records": len(large_dataset) if hasattr(large_dataset, '__len__') else 1,
            "key_metrics": self.calculate_metrics(large_dataset),
            "sample_records": self.get_sample_data(large_dataset),
            "data_type": type(large_dataset).__name__
        }
        return summary
    
    def process_with_summarization(self, data):
        """Process data using summarization approach"""
        if len(str(data)) > 500:  # If data is considered large
            summary = self.summarize_data(data)
            return {
                "method": "summarization",
                "summary": summary,
                "original_size": len(str(data)),
                "compressed": True
            }
        else:
            return {
                "method": "direct_processing",
                "data": data,
                "original_size": len(str(data)),
                "compressed": False
            }