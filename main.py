from password_cracker import crack_sha1_hash
import test_module
import unittest

def main():
    """Main function for development and testing"""
    print("SHA-1 Password Cracker")
    print("=" * 40)
    
    # Test some of the provided examples
    print("\nTesting without salt:")
    print("-" * 20)
    
    test_cases = [
        ("b305921a3723cd5d70a375cd21a61e60aabb84ec", "sammy123"),
        ("c7ab388a5ebefbf4d550652f1eb4d833e5316e3e", "abacab"),
        ("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8", "password")
    ]
    
    for hash_val, expected in test_cases:
        result = crack_sha1_hash(hash_val)
        status = "✓" if result == expected else "✗"
        print(f"{status} {hash_val} -> {result} (expected: {expected})")
    
    print("\nTesting with salt:")
    print("-" * 20)
    
    salt_test_cases = [
        ("38e8a75f85b746778f11be8ba43c841e24a79341", "superman"),
        ("be2efdc8b319c980e1bb03ea48c5c949862c09bb", "q1w2e3r4t5"),
        ("4355a5f6b8fd55bd8af019717a37498e25d07892", "bubbles1")
    ]
    
    for hash_val, expected in salt_test_cases:
        result = crack_sha1_hash(hash_val, use_salts=True)
        status = "✓" if result == expected else "✗"
        print(f"{status} {hash_val} -> {result} (expected: {expected})")
    
    print("\nRunning unit tests:")
    print("-" * 20)
    
    # Run the unit tests
    suite = unittest.TestLoader().loadTestsFromModule(test_module)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == "__main__":
    main()