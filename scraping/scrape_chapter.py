from playwright.sync_api import sync_playwright
import os

def scrape_and_screenshot(url, save_dir="data/raw"):
    os.makedirs(save_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state("networkidle")
        
        content = page.inner_text("body")
        screenshot_path = os.path.join(save_dir, "chapter1.png")
        page.screenshot(path=screenshot_path, full_page=True)
        
        text_path = os.path.join(save_dir, "chapter1.txt")
        with open(text_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        browser.close()
        return text_path, screenshot_path
