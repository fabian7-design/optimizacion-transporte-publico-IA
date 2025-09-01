import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from hypothesis import given, settings, strategies as st

from src.scrape import collect_data_offline
from src.nlp import analyze_data
from src.optimize import propose_optimizations

BASE = os.path.dirname(os.path.dirname(__file__))
CSV = os.path.join(BASE, "data", "sample_posts.csv")


def test_collect_data_offline():
    texts = collect_data_offline(CSV)
    assert isinstance(texts, list) and len(texts) > 0 and isinstance(texts[0], str)


@settings(deadline=None)  # evita error por límite de tiempo
@given(st.lists(st.text(min_size=0, max_size=200), min_size=0, max_size=200))
def test_analyze_data(texts):
    issues = analyze_data(texts)
    assert isinstance(issues, dict)
    for k, v in issues.items():
        assert isinstance(k, str) and isinstance(v, int)


@given(st.dictionaries(st.text(min_size=1, max_size=30),
                       st.integers(min_value=0, max_value=100)))
def test_propose_optimizations(issues):
    suggestions = propose_optimizations(issues, threshold=3)
    assert isinstance(suggestions, list)
    for s in suggestions:
        assert isinstance(s, str) and len(s) > 0
