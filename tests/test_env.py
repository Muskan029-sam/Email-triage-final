import unittest
from env import EmailTriageEnv
from baseline_agent import RuleBasedAgent

class TestEmailTriageEnv(unittest.TestCase):
    def setUp(self):
        self.env = EmailTriageEnv()
        self.agent = RuleBasedAgent()

    def test_reset(self):
        email = self.env.reset()
        self.assertIn("subject", email)
        self.assertIn("label", email)

    def test_step_spam(self):
        self.env.reset()
        state, reward, done = self.env.step("spam_filter")
        self.assertIsInstance(reward, int)

    def test_agent_spam(self):
        action = self.agent.act("You won a lottery! Unsubscribe here")
        self.assertEqual(action, "spam_filter")

if __name__ == "__main__":
    unittest.main()
