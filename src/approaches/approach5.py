class TokenAwareTruncationProcessor:
    def __init__(self, max_tokens=4000):
        self.max_tokens = max_tokens
    
    def count_tokens(self, text):
        """Simple token counting (word-based approximation)"""
        return len(str(text).split())
    
    def smart_truncate(self, text, max_tokens=None):
        """Truncate text while preserving important information"""
        max_tokens = max_tokens or self.max_tokens
        tokens = str(text).split()
        
        if len(tokens) <= max_tokens:
            return text
        
        # Keep beginning and end, summarize middle
        start_tokens = max_tokens // 3
        end_tokens = max_tokens // 3
        
        start = ' '.join(tokens[:start_tokens])
        end = ' '.join(tokens[-end_tokens:])
        middle_summary = f"... [content summarized: {len(tokens) - start_tokens - end_tokens} tokens] ..."
        
        return f"{start}\n{middle_summary}\n{end}"
    
    def process_with_truncation(self, data):
        """Process data with smart truncation"""
        text = str(data)
        token_count = self.count_tokens(text)
        
        if token_count > self.max_tokens:
            truncated = self.smart_truncate(text)
            return {
                "method": "token_aware_truncation",
                "original_tokens": token_count,
                "truncated_tokens": self.count_tokens(truncated),
                "truncated_data": truncated,
                "truncated": True
            }
        else:
            return {
                "method": "no_truncation_needed",
                "tokens": token_count,
                "data": data,
                "truncated": False
            }