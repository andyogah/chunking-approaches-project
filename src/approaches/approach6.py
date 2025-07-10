class StreamingProcessor:
    def __init__(self, context_limit=1000):
        self.context_limit = context_limit
    
    def update_context(self, current_context, new_result):
        """Update accumulated context with new result"""
        # Keep only the most recent context within limit
        updated = f"{current_context}\n{str(new_result)}"
        
        if len(updated) > self.context_limit:
            # Keep only the latest part of the context
            words = updated.split()
            if len(words) > self.context_limit // 5:  # Rough word limit
                updated = ' '.join(words[-(self.context_limit // 5):])
        
        return updated
    
    def process_with_context(self, data_chunk, context):
        """Process a single chunk with accumulated context"""
        return {
            "chunk_data": str(data_chunk)[:100] + "..." if len(str(data_chunk)) > 100 else str(data_chunk),
            "context_length": len(context),
            "processed_at": "timestamp_placeholder",
            "has_context": len(context) > 0
        }
    
    def create_data_stream(self, large_data, chunk_size=100):
        """Convert large data into a stream of chunks"""
        if isinstance(large_data, list):
            for i in range(0, len(large_data), chunk_size):
                yield large_data[i:i + chunk_size]
        elif isinstance(large_data, str):
            for i in range(0, len(large_data), chunk_size):
                yield large_data[i:i + chunk_size]
        else:
            # For other types, convert to string and stream
            data_str = str(large_data)
            for i in range(0, len(data_str), chunk_size):
                yield data_str[i:i + chunk_size]
    
    def iterative_processing(self, data):
        """Process data incrementally with streaming"""
        data_stream = self.create_data_stream(data)
        accumulated_context = ""
        results = []
        
        for i, data_chunk in enumerate(data_stream):
            result = self.process_with_context(data_chunk, accumulated_context)
            result["chunk_index"] = i
            accumulated_context = self.update_context(accumulated_context, result)
            results.append(result)
        
        return {
            "method": "streaming_iterative",
            "total_chunks": len(results),
            "final_context_length": len(accumulated_context),
            "chunk_results": results
        }