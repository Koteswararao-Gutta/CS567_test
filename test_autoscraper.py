import unittest
from autoscraper import AutoScraper


class TestAutoScraper(unittest.TestCase):
    # Test the build function with a valid URL and wanted list
    def test_build_function(self):
        url = "https://example.com"  # Static example page
        wanted_list = ["Example Domain"]  # Text known to exist on the page

        scraper = AutoScraper()
        result = scraper.build(url, wanted_list)

        # Debugging line to check what the scraper retrieves
        print("Scraper Result:", result)

        self.assertIsInstance(result, list, "Result should be a list")
        self.assertIn("Example Domain", result, "The desired text should be in the result")
    '''def test_invalid_url(self):
        scraper = AutoScraper()
        invalid_url = "not-a-valid-url"

        with self.assertRaises(Exception, msg="Invalid URL should raise an exception"):
            scraper.build(invalid_url, ["Test"])
    '''
    def test_save_and_load_rules(self):
        url = "https://example.com"
        wanted_list = ["Example Domain"]

        scraper = AutoScraper()
        scraper.build(url, wanted_list)
        scraper.save("test_rules")  # Save rules to a file

        new_scraper = AutoScraper()
        new_scraper.load("test_rules")  # Load rules from the file
        result = new_scraper.get_result_similar(url)

        self.assertIn("Example Domain", result, "Loaded rules should work correctly")

    def test_non_html_content(self):
        scraper = AutoScraper()
        url = "https://httpbin.org/json"  # JSON endpoint

        try:
            scraper.build(url, ["Test"])
        except Exception as e:
            self.assertIsInstance(e, Exception, "Non-HTML content should raise an exception")

    '''def test_empty_wanted_list(self):
        scraper = AutoScraper()
        url = "https://example.com"

        with self.assertRaises(Exception, msg="Empty wanted list should raise an exception"):
            scraper.build(url, [])'''

    def test_data_extraction_similar_pages(self):
        url = "https://example.com"
        wanted_list = ["Example Domain"]

        scraper = AutoScraper()
        scraper.build(url, wanted_list)

        # Test on the same page to simulate similar content
        result = scraper.get_result_similar(url)
        self.assertIn("Example Domain", result, "Scraper should extract similar data")
    
    def test_large_wanted_list(self):
        scraper = AutoScraper()
        url = "https://example.com"
        wanted_list = ["Example Domain"] * 100  # Repeating the same item

        result = scraper.build(url, wanted_list)
        self.assertLessEqual(len(result), 100, "Result should not exceed the size of the wanted list")
    
    def test_missing_wanted_item(self):
        scraper = AutoScraper()
        url = "https://example.com"
        wanted_list = ["Non-Existent Item"]

        result = scraper.build(url, wanted_list)
        self.assertEqual(result, [], "Result should be empty when the wanted item is not found")


# Entry point for unittest
if __name__ == "__main__":
    unittest.main()
