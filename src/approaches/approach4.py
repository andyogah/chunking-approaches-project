class HierarchicalProcessor:
    def __init__(self):
        pass
    
    def analyze_overview(self, data):
        """Perform high-level analysis of data"""
        overview = {
            "data_type": type(data).__name__,
            "size": len(str(data)),
            "important_sections": []
        }
        
        if isinstance(data, list):
            # Identify important sections based on size or content
            for i, item in enumerate(data):
                if len(str(item)) > 100:  # Consider large items as important
                    overview["important_sections"].append({
                        "index": i,
                        "size": len(str(item)),
                        "type": type(item).__name__
                    })
        elif isinstance(data, str):
            # Split into paragraphs and identify important ones
            paragraphs = data.split('\n\n')
            for i, para in enumerate(paragraphs):
                if len(para) > 200:
                    overview["important_sections"].append({
                        "index": i,
                        "size": len(para),
                        "preview": para[:50] + "..."
                    })
        
        return overview
    
    def analyze_detail(self, section_info):
        """Perform detailed analysis on specific section"""
        return {
            "section_index": section_info.get("index"),
            "detailed_analysis": f"Detailed analysis of section {section_info.get('index')}",
            "word_count": section_info.get("size", 0) // 5,  # Rough estimate
            "complexity": "high" if section_info.get("size", 0) > 500 else "medium"
        }
    
    def process_hierarchically(self, data):
        """Process data in hierarchical stages"""
        # Stage 1: High-level analysis
        overview = self.analyze_overview(data)
        
        # Stage 2: Detailed analysis on important sections
        detailed_results = []
        for section in overview["important_sections"]:
            detailed_result = self.analyze_detail(section)
            detailed_results.append(detailed_result)
        
        return {
            "method": "hierarchical",
            "overview": overview,
            "detailed_analysis": detailed_results,
            "stages_completed": 2
        }