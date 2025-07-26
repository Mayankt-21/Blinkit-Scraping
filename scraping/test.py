from my_scrapper import my_scrapper

def manual_script():
    # Sample hardcoded inputs for testing
    lat = "28.678051"
    lon = "77.314262"
    l0_cat = 'Munchies'
    l0_cat_id = '1237'
    l1_cat = 'Bhujia & Mixtures'
    l1_cat_id = '940'

    # Run the scraper with sample data
    df = my_scrapper(lat, lon, l0_cat, l0_cat_id, l1_cat, l1_cat_id,30)
    print(df.head())  # Optional: Show sample output

manual_script()
