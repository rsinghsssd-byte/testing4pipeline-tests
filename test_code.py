import sys

def run_mock_tests():
    total_tests = 33
    failed = 0
    passed = 0

    print(head := f"--- Running {total_tests} Pipeline Tests ---")
    
    for i in range(1, total_tests + 1):
        if i % 2 != 0:
            print(f"❌ Test #{i}: FAILED (Simulated assertion error)")
            failed += 1
        else:
            print(f"✅ Test #{i}: PASSED")
            passed += 1

    print("-" * len(head))
    print(f"Results: {passed} Passed, {failed} Failed.")
    
    # Exit with a non-zero code if any tests fail so GitHub knows the pipeline failed
    if failed > 0:
        sys.exit(1)

if __name__ == "__main__":
    run_mock_tests()
