# https://bytebytego.com/exercises/coding-patterns/two-pointers/is-palindrome-valid

def is_palindrome(s: str) -> bool:
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Use two pointers to check palindrome
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True