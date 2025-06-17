import math
import string

COMMON_PASSWORDS = set([
    'password', '123456', '123456789', 'qwerty', 'abc123', 'letmein', 'monkey', 'football', 'iloveyou', 'admin'
])

def calculate_entropy(password):
    charset = 0
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in string.punctuation for c in password):
        charset += len(string.punctuation)
    if charset == 0:
        return 0
    return round(len(password) * math.log2(charset), 2)

def check_dictionary(password):
    return password.lower() in COMMON_PASSWORDS

def analyze_password(password):
    entropy = calculate_entropy(password)
    is_common = check_dictionary(password)
    score = 0
    if entropy > 60 and not is_common:
        score = 3
    elif entropy > 40:
        score = 2
    elif entropy > 20:
        score = 1
    else:
        score = 0
    return {
        'entropy': entropy,
        'is_common': is_common,
        'score': score
    }

def feedback(result):
    if result['is_common']:
        return "Your password is too common. Choose something more unique."
    if result['score'] == 3:
        return "Strong password!"
    elif result['score'] == 2:
        return "Moderate password. Consider adding more unique characters."
    elif result['score'] == 1:
        return "Weak password. Use a mix of upper/lowercase, numbers, and symbols."
    else:
        return "Very weak password. Avoid dictionary words and short passwords."

def main():
    password = input("Enter a password to analyze: ")
    result = analyze_password(password)
    print(f"\nEntropy: {result['entropy']}")
    print(f"Common password: {'Yes' if result['is_common'] else 'No'}")
    print(f"Strength score: {result['score']} / 3")
    print(feedback(result))

if __name__ == "__main__":
    main()
