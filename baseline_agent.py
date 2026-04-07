class RuleBasedAgent:
    def act(self, subject):
        subject = subject.lower()

        if "win" in subject or "free" in subject:
            return "spam_filter"
        elif "meeting" in subject or "deadline" in subject:
            return "prioritize"
        else:
            return "reply"
