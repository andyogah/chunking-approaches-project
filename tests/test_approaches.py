import unittest
import sys
import os
import tempfile
import shutil

# Add src directory to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', 'src')
sys.path.insert(0, src_dir)

def safe_import(module_name, class_name):
    """Safely import a module and class, returning None if import fails"""
    try:
        module = __import__(module_name, fromlist=[class_name])
        return getattr(module, class_name)
    except (ImportError, AttributeError):
        return None

# Import modules safely
ChunkingProcessor = safe_import('approaches.approach1', 'ChunkingProcessor')
SummarizationProcessor = safe_import('approaches.approach2', 'SummarizationProcessor')
ReferenceBasedProcessor = safe_import('approaches.approach3', 'ReferenceBasedProcessor')
HierarchicalProcessor = safe_import('approaches.approach4', 'HierarchicalProcessor')
TokenAwareTruncationProcessor = safe_import('approaches.approach5', 'TokenAwareTruncationProcessor')
StreamingProcessor = safe_import('approaches.approach6', 'StreamingProcessor')
DataProcessingManager = safe_import('main', 'DataProcessingManager')

# Import helper functions safely
format_result_output = safe_import('utils.helpers', 'format_result_output')
validate_data_input = safe_import('utils.helpers', 'validate_data_input')
get_data_characteristics = safe_import('utils.helpers', 'get_data_characteristics')
load_sample_data = safe_import('utils.helpers', 'load_sample_data')

# Check if helpers are available
HELPERS_AVAILABLE = all([
    format_result_output is not None,
    validate_data_input is not None,
    get_data_characteristics is not None,
    load_sample_data is not None
])

class TestChunkingProcessor(unittest.TestCase):
    """Test cases for ChunkingProcessor"""
    
    def setUp(self):
        if ChunkingProcessor is None:
            self.skipTest("ChunkingProcessor not available - create approaches/approach1.py")
        self.processor = ChunkingProcessor(chunk_size=10)
    
    def test_chunk_text_basic(self):
        """Test basic text chunking functionality"""
        text = "This is a test string for chunking"
        chunks = self.processor.chunk_text(text, 10)
        
        # Basic checks - adapt based on your actual implementation
        self.assertIsInstance(chunks, list)
        self.assertGreater(len(chunks), 0)
        
        # Join chunks should recreate original text (approximately)
        rejoined = "".join(chunks)
        self.assertEqual(len(rejoined), len(text))
    
    def test_chunk_list_basic(self):
        """Test basic list chunking functionality"""
        data = list(range(25))
        chunks = self.processor.chunk_list(data, 5)
        
        self.assertIsInstance(chunks, list)
        self.assertEqual(len(chunks), 5)
        
        # Flatten chunks should recreate original list
        flattened = [item for chunk in chunks for item in chunk]
        self.assertEqual(flattened, data)
    
    def test_process_large_data_string(self):
        """Test processing large string data"""
        data = "This is a test string that should be chunked" * 10
        result = self.processor.process_large_data_in_chunks(data)
        
        self.assertIsInstance(result, dict)
        self.assertIn("method", result)
        self.assertEqual(result["method"], "chunking")

class TestSummarizationProcessor(unittest.TestCase):
    """Test cases for SummarizationProcessor"""
    
    def setUp(self):
        if SummarizationProcessor is None:
            self.skipTest("SummarizationProcessor not available - create approaches/approach2.py")
        self.processor = SummarizationProcessor()
    
    def test_process_with_summarization(self):
        """Test basic summarization functionality"""
        data = "This is a very long string " * 50
        result = self.processor.process_with_summarization(data)
        
        self.assertIsInstance(result, dict)
        self.assertIn("method", result)
        self.assertEqual(result["method"], "summarization")

class TestReferenceBasedProcessor(unittest.TestCase):
    """Test cases for ReferenceBasedProcessor"""
    
    def setUp(self):
        if ReferenceBasedProcessor is None:
            self.skipTest("ReferenceBasedProcessor not available - create approaches/approach3.py")
        self.temp_dir = tempfile.mkdtemp()
        self.processor = ReferenceBasedProcessor(storage_dir=self.temp_dir)
    
    def tearDown(self):
        """Clean up temporary directory"""
        if hasattr(self, 'temp_dir') and os.path.exists(self.temp_dir):
            try:
                shutil.rmtree(self.temp_dir)
            except (OSError, PermissionError):
                pass  # Ignore cleanup errors
    
    def test_process_with_reference(self):
        """Test basic reference-based processing"""
        large_data = {"large_field": "x" * 2000}
        result = self.processor.process_with_reference(large_data)
        
        self.assertIsInstance(result, dict)
        self.assertIn("method", result)

class TestHierarchicalProcessor(unittest.TestCase):
    """Test cases for HierarchicalProcessor"""
    
    def setUp(self):
        if HierarchicalProcessor is None:
            self.skipTest("HierarchicalProcessor not available - create approaches/approach4.py")
        self.processor = HierarchicalProcessor()
    
    def test_process_hierarchically(self):
        """Test basic hierarchical processing"""
        data = ["small"] + ["large_content_" + "x" * 200] * 3
        result = self.processor.process_hierarchically(data)
        
        self.assertIsInstance(result, dict)
        self.assertIn("method", result)
        self.assertEqual(result["method"], "hierarchical")

class TestTokenAwareTruncationProcessor(unittest.TestCase):
    """Test cases for TokenAwareTruncationProcessor"""
    
    def setUp(self):
        if TokenAwareTruncationProcessor is None:
            self.skipTest("TokenAwareTruncationProcessor not available - create approaches/approach5.py")
        self.processor = TokenAwareTruncationProcessor(max_tokens=20)
    
    def test_process_with_truncation(self):
        """Test basic truncation processing"""
        data = " ".join([f"token{i}" for i in range(100)])
        result = self.processor.process_with_truncation(data)
        
        self.assertIsInstance(result, dict)
        self.assertIn("method", result)

class TestStreamingProcessor(unittest.TestCase):
    """Test cases for StreamingProcessor"""
    
    def setUp(self):
        if StreamingProcessor is None:
            self.skipTest("StreamingProcessor not available - create approaches/approach6.py")
        self.processor = StreamingProcessor(context_limit=100)
    
    def test_iterative_processing(self):
        """Test basic streaming processing"""
        data = ["item" + str(i) for i in range(10)]
        result = self.processor.iterative_processing(data)
        
        self.assertIsInstance(result, dict)
        self.assertIn("method", result)
        self.assertEqual(result["method"], "streaming_iterative")

class TestHelpers(unittest.TestCase):
    """Test cases for helper functions"""
    
    def setUp(self):
        if not HELPERS_AVAILABLE:
            self.skipTest("Helper functions not available - create utils/helpers.py")
    
    def test_validate_data_input_valid(self):
        """Test data validation with valid inputs"""
        self.assertTrue(validate_data_input("valid string"))
        self.assertTrue(validate_data_input([1, 2, 3]))
        self.assertTrue(validate_data_input({"key": "value"}))
    
    def test_validate_data_input_invalid(self):
        """Test data validation with invalid inputs"""
        self.assertFalse(validate_data_input(None))
        self.assertFalse(validate_data_input(""))
        self.assertFalse(validate_data_input([]))
    
    def test_get_data_characteristics(self):
        """Test data characteristics analysis"""
        data = "test string"
        chars = get_data_characteristics(data)
        
        self.assertIsInstance(chars, dict)
        self.assertIn("type", chars)
        self.assertEqual(chars["type"], "str")
    
    def test_format_result_output(self):
        """Test result formatting"""
        result = {
            "method": "test_method",
            "original_size": 100,
            "total_chunks": 5
        }
        output = format_result_output(result, "test")
        
        self.assertIsInstance(output, str)
        self.assertIn("TEST APPROACH", output)
        self.assertIn("test_method", output)
    
    def test_load_sample_data(self):
        """Test sample data loading"""
        small_data = load_sample_data("small")
        self.assertIsNotNone(small_data)
        
        medium_data = load_sample_data("medium")
        self.assertIsNotNone(medium_data)
        
        mixed_data = load_sample_data("mixed")
        self.assertIsNotNone(mixed_data)

class TestDataProcessingManager(unittest.TestCase):
    """Test cases for DataProcessingManager"""
    
    def setUp(self):
        if DataProcessingManager is None:
            self.skipTest("DataProcessingManager not available - check main.py")
        self.manager = DataProcessingManager()
    
    def test_initialization(self):
        """Test manager initialization"""
        self.assertIsNotNone(self.manager)
        self.assertTrue(hasattr(self.manager, 'processors'))
        self.assertIsInstance(self.manager.processors, dict)
    
    def test_get_available_approaches(self):
        """Test getting available approaches"""
        if hasattr(self.manager, 'get_available_approaches'):
            approaches = self.manager.get_available_approaches()
            self.assertIsInstance(approaches, list)
        else:
            self.skipTest("get_available_approaches method not implemented")
    
    def test_recommend_approach(self):
        """Test approach recommendation"""
        if hasattr(self.manager, 'recommend_approach'):
            small_data = "small"
            recommendation = self.manager.recommend_approach(small_data)
            self.assertIsInstance(recommendation, str)
        else:
            self.skipTest("recommend_approach method not implemented")

class TestProjectStructure(unittest.TestCase):
    """Test cases for project structure and file existence"""
    
    def test_src_directory_exists(self):
        """Test that src directory exists"""
        self.assertTrue(os.path.exists(src_dir), f"Source directory not found: {src_dir}")
    
    def test_approaches_directory_exists(self):
        """Test that approaches directory exists"""
        approaches_dir = os.path.join(src_dir, 'approaches')
        self.assertTrue(os.path.exists(approaches_dir), f"Approaches directory not found: {approaches_dir}")
    
    def test_utils_directory_exists(self):
        """Test that utils directory exists"""
        utils_dir = os.path.join(src_dir, 'utils')
        self.assertTrue(os.path.exists(utils_dir), f"Utils directory not found: {utils_dir}")
    
    def test_main_file_exists(self):
        """Test that main.py exists"""
        main_file = os.path.join(src_dir, 'main.py')
        self.assertTrue(os.path.exists(main_file), f"Main file not found: {main_file}")

def print_import_status():
    """Print the status of all imports"""
    print("="*60)
    print("IMPORT STATUS CHECK")
    print("="*60)
    
    modules_status = [
        ("ChunkingProcessor (approach1.py)", ChunkingProcessor is not None),
        ("SummarizationProcessor (approach2.py)", SummarizationProcessor is not None),
        ("ReferenceBasedProcessor (approach3.py)", ReferenceBasedProcessor is not None),
        ("HierarchicalProcessor (approach4.py)", HierarchicalProcessor is not None),
        ("TokenAwareTruncationProcessor (approach5.py)", TokenAwareTruncationProcessor is not None),
        ("StreamingProcessor (approach6.py)", StreamingProcessor is not None),
        ("Helper functions (utils/helpers.py)", HELPERS_AVAILABLE),
        ("DataProcessingManager (main.py)", DataProcessingManager is not None),
    ]
    
    for module_name, is_available in modules_status:
        status = "✓" if is_available else "✗"
        print(f"  {status} {module_name}")
    
    print()
    
    # Check file structure
    print("FILE STRUCTURE CHECK")
    print("-" * 30)
    
    files_to_check = [
        ("src/", "src"),
        ("src/approaches/", "approaches"),
        ("src/utils/", "utils"),
        ("src/main.py", "main.py"),
        ("src/approaches/__init__.py", "approaches/__init__.py"),
        ("src/utils/__init__.py", "utils/__init__.py"),
    ]
    
    for file_path, display_name in files_to_check:
        full_path = os.path.join(os.path.dirname(src_dir), file_path)
        exists = os.path.exists(full_path)
        status = "✓" if exists else "✗"
        print(f"  {status} {display_name}")
    
    print()

def run_tests():
    """Function to run all tests with proper error handling"""
    print_import_status()
    
    # Get all test classes
    test_classes = [
        TestProjectStructure,  # Run structure tests first
        TestChunkingProcessor,
        TestSummarizationProcessor,
        TestReferenceBasedProcessor,
        TestHierarchicalProcessor,
        TestTokenAwareTruncationProcessor,
        TestStreamingProcessor,
        TestHelpers,
        TestDataProcessingManager,
    ]
    
    # Run tests for each class individually
    total_tests = 0
    total_failures = 0
    total_errors = 0
    total_skipped = 0
    
    for test_class in test_classes:
        print(f"\n{'='*50}")
        print(f"Running {test_class.__name__}")
        print('='*50)
        
        try:
            suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
            runner = unittest.TextTestRunner(verbosity=2)
            result = runner.run(suite)
            
            total_tests += result.testsRun
            total_failures += len(result.failures)
            total_errors += len(result.errors)
            total_skipped += len(result.skipped)
                
        except Exception as e:
            print(f"Error running {test_class.__name__}: {e}")
            total_errors += 1
    
    # Print final summary
    print(f"\n{'='*60}")
    print("FINAL TEST SUMMARY")
    print('='*60)
    print(f"Tests run: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Errors: {total_errors}")
    print(f"Skipped: {total_skipped}")
    
    if total_tests > 0:
        success_rate = ((total_tests - total_failures - total_errors)/total_tests)*100
        print(f"Success rate: {success_rate:.1f}%")
    else:
        print("No tests were run successfully")
    
    # Provide guidance
    print(f"\n{'='*60}")
    print("NEXT STEPS")
    print('='*60)
    
    missing_modules = []
    if ChunkingProcessor is None:
        missing_modules.append("• Create src/approaches/approach1.py with ChunkingProcessor class")
    if SummarizationProcessor is None:
        missing_modules.append("• Create src/approaches/approach2.py with SummarizationProcessor class")
    if ReferenceBasedProcessor is None:
        missing_modules.append("• Create src/approaches/approach3.py with ReferenceBasedProcessor class")
    if HierarchicalProcessor is None:
        missing_modules.append("• Create src/approaches/approach4.py with HierarchicalProcessor class")
    if TokenAwareTruncationProcessor is None:
        missing_modules.append("• Create src/approaches/approach5.py with TokenAwareTruncationProcessor class")
    if StreamingProcessor is None:
        missing_modules.append("• Create src/approaches/approach6.py with StreamingProcessor class")
    if not HELPERS_AVAILABLE:
        missing_modules.append("• Create src/utils/helpers.py with helper functions")
    if DataProcessingManager is None:
        missing_modules.append("• Create or fix src/main.py with DataProcessingManager class")
    
    if missing_modules:
        for module in missing_modules:
            print(module)
    else:
        print("✓ All modules are available! You can run the full test suite.")
    
    return total_tests, total_failures, total_errors

def check_file_structure():
    """Check and report on project file structure"""
    print("="*60)
    print("PROJECT STRUCTURE ANALYSIS")
    print("="*60)
    
    base_dir = os.path.dirname(src_dir)
    
    required_files = [
        "src/",
        "src/__init__.py",
        "src/main.py",
        "src/approaches/",
        "src/approaches/__init__.py",
        "src/approaches/approach1.py",
        "src/approaches/approach2.py", 
        "src/approaches/approach3.py",
        "src/approaches/approach4.py",
        "src/approaches/approach5.py",
        "src/approaches/approach6.py",
        "src/utils/",
        "src/utils/__init__.py",
        "src/utils/helpers.py",
        "tests/",
        "tests/__init__.py",
        "tests/test_approaches.py",
        "README.md",
        "requirements.txt"
    ]
    
    for file_path in required_files:
        full_path = os.path.join(base_dir, file_path)
        exists = os.path.exists(full_path)
        status = "✓" if exists else "✗"
        priority = "REQUIRED" if "approach" in file_path or "helpers.py" in file_path or "main.py" in file_path else "OPTIONAL"
        print(f"  {status} {file_path:<30} ({priority})")
    
    print()

def create_missing_init_files():
    """Create missing __init__.py files"""
    print("Creating missing __init__.py files...")
    
    init_files = [
        os.path.join(src_dir, '__init__.py'),
        os.path.join(src_dir, 'approaches', '__init__.py'),
        os.path.join(src_dir, 'utils', '__init__.py'),
        os.path.join(os.path.dirname(src_dir), 'tests', '__init__.py')
    ]
    
    for init_file in init_files:
        if not os.path.exists(init_file):
            try:
                os.makedirs(os.path.dirname(init_file), exist_ok=True)
                with open(init_file, 'w') as f:
                    f.write('# Package initialization\n')
                print(f"✓ Created {init_file}")
            except Exception as e:
                print(f"✗ Failed to create {init_file}: {e}")
        else:
            print(f"✓ {init_file} already exists")

if __name__ == '__main__':
    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "structure":
            check_file_structure()
        elif sys.argv[1] == "init":
            create_missing_init_files()
        elif sys.argv[1] == "status":
            print_import_status()
        else:
            print("Available commands:")
            print("  python test_approaches.py          - Run tests")
            print("  python test_approaches.py structure - Check file structure")
            print("  python test_approaches.py init     - Create missing __init__.py files")
            print("  python test_approaches.py status   - Check import status")
    else:
        run_tests()