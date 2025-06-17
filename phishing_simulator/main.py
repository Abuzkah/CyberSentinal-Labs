import random

PHISHING_TEMPLATES = [
    {
        'subject': 'Urgent: Account Verification Required',
        'body': 'Dear user,\n\nWe noticed suspicious activity on your account. Please verify your information immediately by clicking the link below.\n\n[Fake Link]\n\nThank you.'
    },
    {
        'subject': 'Congratulations! You have won a prize',
        'body': 'Hello,\n\nYou have been selected as a winner in our recent draw. Claim your prize by providing your details at the link below.\n\n[Fake Link]\n\nBest regards.'
    },
    {
        'subject': 'Password Expiry Notice',
        'body': 'Attention,\n\nYour password will expire soon. Reset it now to maintain access.\n\n[Fake Link]\n\nIT Support.'
    }
]

INDICATORS = [
    'Urgency',
    'Suspicious link',
    'Request for personal info',
    'Generic greeting',
    'Spelling/grammar errors'
]

def generate_email():
    template = random.choice(PHISHING_TEMPLATES)
    return template['subject'], template['body']

def analyze_email(subject, body):
    found = []
    if 'urgent' in subject.lower() or 'immediately' in body.lower():
        found.append('Urgency')
    if '[Fake Link]' in body:
        found.append('Suspicious link')
    if 'verify' in body.lower() or 'provide your details' in body.lower():
        found.append('Request for personal info')
    if 'dear user' in body.lower() or 'hello' in body.lower():
        found.append('Generic greeting')
    return found

def main():
    subject, body = generate_email()
    print(f"Subject: {subject}\n\n{body}\n")
    indicators = analyze_email(subject, body)
    print("Phishing Indicators Detected:")
    for ind in indicators:
        print(f"- {ind}")
    print("\nThis is a simulation. No emails are sent.")

if __name__ == "__main__":
    main()
