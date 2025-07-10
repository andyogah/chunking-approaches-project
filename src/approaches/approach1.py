class ChunkingProcessor:
    def __init__(self, chunk_size=1000):
        self.chunk_size = chunk_size
    
    def chunk_text(self, text, chunk_size=None):
        """Split text into chunks of specified size"""
        size = chunk_size or self.chunk_size
        return [text[i:i + size] for i in range(0, len(text), size)]
    
    def chunk_list(self, data_list, chunk_size=None):
        """Split list into chunks of specified size"""
        size = chunk_size or self.chunk_size
        return [data_list[i:i + size] for i in range(0, len(data_list), size)]
    
    def process_chunk(self, chunk):
        """Process a single chunk of data"""
        return {
            "chunk_size": len(chunk),
            "chunk_type": type(chunk).__name__,
            "processed": True,
            "summary": f"Processed {len(chunk)} items"
        }
    
    def process_large_data_in_chunks(self, data):
        """Process large data by breaking it into chunks"""
        if isinstance(data, str):
            chunks = self.chunk_text(data)
        elif isinstance(data, list):
            chunks = self.chunk_list(data)
        else:
            chunks = self.chunk_text(str(data))
        
        results = []
        for i, chunk in enumerate(chunks):
            result = self.process_chunk(chunk)
            result["chunk_index"] = i
            results.append(result)
        
        return {
            "method": "chunking",
            "total_chunks": len(chunks),
            "chunk_results": results,
            "original_size": len(str(data))
        }