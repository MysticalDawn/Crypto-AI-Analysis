from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time


def setup():
    url = "https://cryptopanic.com/news/"
    print("🚀 Initializing Chrome WebDriver...")
    options = Options()
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    print("✅ WebDriver successfully initialized")
    print(f"🌐 Navigating to: {url}")
    driver.get(url)
    time.sleep(2)
    print("📄 Page loaded successfully")
    try:
        print("🍪 Looking for cookie consent button...")
        cookies_button = WebDriverWait(driver=driver, timeout=1).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Accept')]"))
        )
        cookies_button.click()
        print("✅ Cookie consent accepted")
    except Exception as e:
        print(f"❌ Error handling cookies: {e}")
        driver.quit()
        raise e
    return driver


def load_more(length_of_elements, driver):
    load_elements = driver.find_element(by=By.CLASS_NAME, value="btn-outline-primary")
    driver.execute_script("arguments[0].scrollIntoView();", load_elements)
    time.sleep(1)
    elements = driver.find_elements(
        by=By.CSS_SELECTOR, value="div.news-row.news-row-link"
    )
    return True if len(elements) > length_of_elements else False


def main():
    driver = setup()
    data_limit = 50000
    print(f"\n📊 Starting data collection (target: {data_limit} articles)...")
    elements = driver.find_elements(
        by=By.CSS_SELECTOR, value="div.news-row.news-row-link"
    )
    print(f"🔍 Found {len(elements)} articles initially")

    while (len(elements) < data_limit) and load_more(len(elements), driver):
        elements = driver.find_elements(
            by=By.CSS_SELECTOR, value="div.news-row.news-row-link"
        )
        print(f"📈 Loaded more articles... Current count: {len(elements)}")

    print(f"\n🎯 Data collection complete! Found {len(elements)} articles")
    print("=" * 60)
    results = []
    for i, element in enumerate(elements, 1):
        print(f"\n📰 Article {i}/{len(elements)}:")
        title = element.find_element(
            By.CSS_SELECTOR, "span.title-text span:nth-child(1)"
        ).text
        if title == "":
            print("  ⚠️  Title not visible, scrolling to element...")
            driver.execute_script(
                "arguments[0].scrollIntoView();",
                element.find_element(By.CSS_SELECTOR, "span.title-text"),
            )
            title = element.find_element(
                By.CSS_SELECTOR, "span.title-text span:nth-child(1)"
            ).text
        print(f"  📝 Title: {title}")
        print("  " + "-" * 50)
        results.append(title)
    print(f"\n✅ Successfully processed {len(elements)} articles")
    driver.quit()
    print("🔒 WebDriver closed successfully")
    with open("./data/raw/cryptopanic_results.pkl", "wb") as f:
        pickle.dump(results, f)
    print("✅ Cryptopanic data saved successfully")


main()
