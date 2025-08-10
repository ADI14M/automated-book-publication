from scraping.scrape_chapter import scrape_and_screenshot
from agents.ai_writer import spin_chapter
from db.chromadb_setup import store_version
from rl.reward_engine import reward_function

if __name__ == "__main__":
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    text_path, _ = scrape_and_screenshot(url)
    
    with open(text_path, "r", encoding="utf-8") as f:
        original = f.read()
    
    rewritten = spin_chapter(original)
    reward = reward_function(original, rewritten)
    
    store_version(rewritten, meta={"version": "v1", "reward": reward})
    
    print(f"Chapter rewritten and stored with reward score: {reward:.4f}")
