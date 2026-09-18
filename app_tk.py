import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Sentiment Analyzer")
        self.root.geometry("640x560")
        self.root.minsize(560, 480)

        self.vader = SentimentIntensityAnalyzer()

        self._build_ui()

    def _build_ui(self):
        main = ttk.Frame(self.root, padding=12)
        main.pack(fill="both", expand=True)

        ttk.Label(main, text="Enter text to analyze:", font=("Segoe UI", 11, "bold")).pack(anchor="w")

        self.input_text = scrolledtext.ScrolledText(main, height=6, wrap="word", font=("Segoe UI", 11))
        self.input_text.pack(fill="both", expand=True, pady=(4, 8))
        self.input_text.bind("<Control-Return>", lambda e: self.analyze())

        controls = ttk.Frame(main)
        controls.pack(fill="x")

        self.analyze_btn = ttk.Button(controls, text="Analyze", command=self.analyze)
        self.analyze_btn.pack(side="left")

        self.clear_btn = ttk.Button(controls, text="Clear", command=self.clear)
        self.clear_btn.pack(side="left", padx=(8, 0))

        self.root.bind("<Control-a>", lambda e: self.analyze())

        self.results = scrolledtext.ScrolledText(main, height=14, wrap="word", state="disabled",
                                                 font=("Segoe UI", 11))
        self.results.pack(fill="both", expand=True, pady=(8, 0))

        ttk.Label(main, text="Tip: Press Ctrl+Enter or Ctrl+A to analyze.",
                  foreground="gray").pack(anchor="w", pady=(6, 0))

    def analyze(self):
        text = self.input_text.get("1.0", "end").strip()
        if not text:
            messagebox.showinfo("No Text", "Please enter some text to analyze.")
            return

        textblob = TextBlob(text)
        polarity, subjectivity = textblob.sentiment.polarity, textblob.sentiment.subjectivity

        vader_scores = self.vader.polarity_scores(text)
        compound = vader_scores["compound"]

        sentiment = lambda score: "Positive" if score > 0.05 else "Negative" if score < -0.05 else "Neutral"

        report = [
            "=" * 42,
            "  SENTIMENT ANALYSIS RESULTS",
            "=" * 42,
            f"TextBlob Polarity   : {polarity:+.3f}  ->  {sentiment(polarity)}",
            f"TextBlob Subjectivity: {subjectivity:.3f}  ->  {self._subjectivity_label(subjectivity)}",
            "-" * 42,
            f"VADER Compound      : {compound:+.3f}  ->  {sentiment(compound)}",
            f"  (Positive: {vader_scores['pos']*100:.1f}% | Neutral: {vader_scores['neu']*100:.1f}% | Negative: {vader_scores['neg']*100:.1f}%)",
            "-" * 42,
            "Overall: {} (agreed by both models)".format(self._overall(polarity, compound)),
            "=" * 42,
        ]

        self.results.config(state="normal")
        self.results.delete("1.0", "end")
        self.results.insert("1.0", "\n".join(report))
        self.results.config(state="disabled")

    def _subjectivity_label(self, score):
        if score < 0.33:
            return "Objective (factual)"
        if score < 0.66:
            return "Somewhat subjective"
        return "Highly subjective (opinion)"

    def _overall(self, polarity, compound):
        if self._sign(polarity) == self._sign(compound) and self._sign(polarity) != 0:
            label = "Positive" if polarity > 0 else "Negative"
            return f"{label} 👍"
        return "Mixed / Neutral 🤔"

    @staticmethod
    def _sign(score):
        return 1 if score > 0.05 else -1 if score < -0.05 else 0

    def clear(self):
        self.input_text.delete("1.0", "end")
        self.results.config(state="normal")
        self.results.delete("1.0", "end")
        self.results.config(state="disabled")
        self.input_text.focus_set()


def main():
    root = tk.Tk()
    SentimentAnalyzerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()