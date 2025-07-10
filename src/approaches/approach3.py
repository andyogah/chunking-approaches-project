import hashlib
import json
import os

class ReferenceBasedProcessor:
    def __init__(self, storage_dir="data_storage"):
        self.storage_dir = storage_dir
        os.makedirs(storage_dir, exist_ok=True)
    
    def save_to_storage(self, data):
        """Save data to storage and return reference ID"""
        data_id = hashlib.md5(str(data).encode()).hexdigest()[:8]
        file_path = os.path.join(self.storage_dir, f"{data_id}.json")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, default=str)
        
        return data_id
    
    def load_from_storage(self, data_id):
        """Load data from storage using reference ID"""
        file_path = os.path.join(self.storage_dir, f"{data_id}.json")
        
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None
    
    def create_data_reference(self, large_data):
        """Create a reference to large data"""
        data_id = self.save_to_storage(large_data)
        return f"Data reference ID: {data_id}"
    
    def process_with_reference(self, data):
        """Process data using reference-based approach"""
        if len(str(data)) > 1000:  # If data is large
            reference = self.create_data_reference(data)
            return {
                "method": "reference_based",
                "reference": reference,
                "data_size": len(str(data)),
                "summary": f"Large data stored with reference"
            }
        else:
            return {
                "method": "direct_processing",
                "data": data,
                "data_size": len(str(data))
            }