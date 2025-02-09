import re


class EQGrader:

    def __init__(self):
        self.score_weights = {
            # Core empathy indicators (50% of total weight)
            "empathy_tokens_present": 0.2,
            "emotional_cues_present": 0.2,
            "perspective_taking": 0.1,
            # Support indicators (30% of total weight)
            "solution_offering": 0.1,
            "active_listening": 0.1,
            "validation_presence": 0.1,
            # Language characteristics (20% of total weight)
            "personal_pronouns": 0.05,
            "gentle_language": 0.05,
            "follow_up_questions": 0.1,
        }

        # Penalty weights for negative features
        self.penalty_weights = {
            "dismissive_language": -0.3,
            "judgment_presence": -0.2,
            "toxic_positivity": -0.2,
            "solution_forcing": -0.15,
            "self_centering": -0.15,
        }

        self.empathy_tokens = [
            "understand",
            "hear you",
            "must be",
            "sounds like",
            "appreciate",
            "recognize",
            "acknowledge",
        ]

        self.emotional_cues = [
            "feel",
            "feeling",
            "emotion",
            "difficult",
            "challenging",
            "overwhelming",
            "frustrated",
        ]

        self.dismissive_phrases = [
            "just",
            "simply",
            "easy",
            "get over it",
            "not that bad",
            "could be worse",
        ]

        self.judgment_phrases = [
            "should have",
            "your fault",
            "obviously",
            "clearly",
            "always",
            "never",
        ]

        self.toxic_positivity = [
            "everything happens for a reason",
            "look on the bright side",
            "stay positive",
            "it's all good",
        ]

    def calculate_score(self, text: str) -> tuple[float, dict[str, float]]:
        text = text.lower()
        scores = {}

        # Calculate positive scores
        scores["empathy_tokens_present"] = (
            sum(1 for token in self.empathy_tokens if token in text)
            * self.score_weights["empathy_tokens_present"]
        )
        scores["emotional_cues_present"] = (
            sum(1 for cue in self.emotional_cues if cue in text)
            * self.score_weights["emotional_cues_present"]
        )
        scores["perspective_taking"] = (
            text.count("you might") + text.count("you may") + text.count("you feel")
        ) * self.score_weights["perspective_taking"]
        scores["personal_pronouns"] = (
            text.count("you") + text.count("your")
        ) * self.score_weights["personal_pronouns"]
        scores["follow_up_questions"] = (
            text.count("?") * self.score_weights["follow_up_questions"]
        )

        # Calculate penalty scores
        penalties = {}
        penalties["dismissive_language"] = (
            sum(1 for phrase in self.dismissive_phrases if phrase in text)
            * self.penalty_weights["dismissive_language"]
        )
        penalties["judgment_presence"] = (
            sum(1 for phrase in self.judgment_phrases if phrase in text)
            * self.penalty_weights["judgment_presence"]
        )
        penalties["toxic_positivity"] = (
            sum(1 for phrase in self.toxic_positivity if phrase in text)
            * self.penalty_weights["toxic_positivity"]
        )

        # Combine scores and penalties
        total_score = sum(scores.values()) + sum(penalties.values())
        normalized_score = max(0, min(1, total_score))
        breakdown = {**scores, **penalties}
        return normalized_score, breakdown
