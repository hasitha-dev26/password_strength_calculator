import re
import hashlib

def check_password_strength(password):
    score = 0
    feedback = []

    # 1. Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # 2. Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # 3. Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # 4. Digits check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    # 5. Special characters check
    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (@, $, !, %, *, ?, &).")

    # Determine strength level
    if score == 5:
        strength = "Very Strong 🟢"
    elif score >= 3:
        strength = "Moderate 🟡"
    else:
        strength = "Weak 🔴"

    return strength, feedback

def generate_hashes(password):
    # Calculate SHA-256 and MD5 hashes
    sha256_hash = hashlib.sha256(password.encode()).hexdigest()
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    return sha256_hash, md5_hash

def main():
    print("--- Password Strength & Hash Calculator ---")
    password = input("Enter a password to check: ")
    
    strength, feedback = check_password_strength(password)
    sha256_hash, md5_hash = generate_hashes(password)
    
    print("\n--- Results ---")
    print(f"Password Strength: {strength}")
    
    if feedback:
        print("\nAreas for Improvement:")
        for tip in feedback:
            print(f"- {tip}")
            
    print("\nCryptographic Hashes:")
    print(f"SHA-256: {sha256_hash}")
    print(f"MD5    : {md5_hash}")

if __name__ == "__main__":
    main()