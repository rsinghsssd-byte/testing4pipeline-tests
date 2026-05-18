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
# dead_code_examples.py

import math # Dead code: Imported but never used
import os   # Dead code: Imported but never used

def unreachable_after_return():
    """Demonstrates code that can never run because it follows a return."""
    print("This will execute.")
    return True
    
    # --- DEAD CODE BELOW ---
    print("This is dead code because it's after a return statement.")
    x = 10
    y = 20
    return x + y

def never_called_function():
    """This entire function is dead code because it is never invoked."""
    unused_variable = "I am lonely"
    for i in range(5):
        pass
    return unused_variable

def unused_variables():
    """Demonstrates variables that take up memory but are never read."""
    active_var = 100
    
    # --- DEAD CODE BELOW ---
    dead_var_1 = 42
    dead_var_2 = "This string goes nowhere"
    list_of_nothing = [1, 2, 3]
    
    return active_var

def impossible_conditions():
    """Demonstrates code hidden behind conditions that will never evaluate to True."""
    if False:
        # --- DEAD CODE BELOW ---
        print("You will never see this.")

    x = 5
    if x > 10:
        # --- DEAD CODE BELOW ---
        print("x is greater than 10")
    elif x < 0:
        # --- DEAD CODE BELOW ---
        print("x is negative")
    else:
        print("x is exactly 5")

def loop_anomalies():
    """Demonstrates unreachable code inside loops."""
    while True:
        print("Breaking immediately!")
        break
        # --- DEAD CODE BELOW ---
        print("This is unreachable after the break statement.")

    for i in range(10):
        if i % 2 == 0:
            continue
            # --- DEAD CODE BELOW ---
            print(f"This is unreachable after the continue statement for {i}.")

class NeverInstantiatedClass:
    """This entire class is dead code as no objects are ever created from it."""
    def __init__(self):
        self.value = 0

    def do_nothing(self):
        pass

def meaningless_operations():
    """Demonstrates operations that are executed but have zero effect on the program."""
    x = 10
    
    # --- DEAD CODE BELOW ---
    x + 5                           # Calculated but not assigned to anything
    "Just a random string literal"  # Evaluated but not used or printed
    x = x                           # Redundant assignment
    
    return x

if __name__ == "__main__":
    # We call some functions to make the script runnable, 
    # but the dead code inside them (and the uncalled functions) remains dead.
    unreachable_after_return()
    unused_variables()
    impossible_conditions()
    loop_anomalies()
    meaningless_operations()
