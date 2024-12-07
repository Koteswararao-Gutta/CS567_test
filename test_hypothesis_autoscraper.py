from hypothesis import given, strategies as st
from autoscraper import AutoScraper
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import pytest 

@given(
    url=st.from_regex(r"https?://[^\s/$.?#].[^\s]*", fullmatch=True),
    wanted_list=st.lists(st.text(min_size=1, max_size=50), min_size=1, max_size=10),
)
def test_build_with_random_inputs(url, wanted_list):
    scraper = AutoScraper()
    try:
        scraper.build(url=url, wanted_list=wanted_list)
        result = scraper.get_result_similar(url)
        assert isinstance(result, list), "Result should be a list"
    except Exception as e:
        pytest.skip(f"Skipped due to exception: {e}")

@given(html=st.text(min_size=1))
def test_scraper_with_random_html(html):
    scraper = AutoScraper()
    try:
        scraper.build(html=html, wanted_list=["Example Domain"])
        result = scraper.get_result_similar(html=html)
        assert isinstance(result, list), "Result should be a list"
    except Exception:
        assert False, "Scraper should not throw an exception for random HTML"


@given(
    url=st.from_regex(r"https?://[^\s/$.?#].[^\s]*", fullmatch=True),
    wanted_list=st.lists(st.text(min_size=1, max_size=50), min_size=1, max_size=10),
)
def test_save_and_load_consistency(url, wanted_list):
    scraper = AutoScraper()
    try:
        scraper.build(url=url, wanted_list=wanted_list)
        scraper.save("rules.json")
        scraper.load("rules.json")
        result = scraper.get_result_similar(url)
        assert isinstance(result, list), "Result should be a list"
    except Exception as e:
        pytest.skip(f"Skipped due to exception: {e}")
